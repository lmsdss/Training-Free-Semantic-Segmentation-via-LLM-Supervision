import json
import clip
import random
import math
from sentence_transformers import SentenceTransformer
import numpy as np
import torch
import argparse


def get_CLIP_inputs_from_dict(cl_set_dict, ord_class):
    '''
    cl_set_dict: any dict that is of the form {class: [list of class words]}
    ord_class: ORDERED list of classnames that must match dataset
    '''
    counter = 0
    sub_to_super = {}
    # subcs = set(subcs)
    subclasses = []
    for idx, cl in enumerate(ord_class):
        subs = cl_set_dict[cl]
        for sub in subs:
            subclasses.append(sub)
            assert subclasses[counter] == sub
            sub_to_super[counter] = idx
            counter += 1

    return subclasses, sub_to_super


def filter_too_similar_to_cls(sub_classes, classes, sim_cutoff=0.95, device="cuda", print_prob=1):
    # first check simple text matches
    print(len(sub_classes))
    sub_classes = list(sub_classes)
    # sub_classes = sorted(sub_classes)

    mpnet_model = SentenceTransformer('/Label-free-CBM/all-mpnet-base-v2')
    class_features_m = mpnet_model.encode(classes)
    concept_features_m = mpnet_model.encode(sub_classes)
    dot_prods_m = class_features_m @ concept_features_m.T
    dot_prods_c = _clip_dot_prods(classes, sub_classes)
    # weighted since mpnet has highger variance
    dot_prods = (dot_prods_m + 3 * dot_prods_c) / 4

    to_delete = []
    for i in range(len(classes)):
        for j in range(len(sub_classes)):
            prod = dot_prods[i, j]  # prod = dot_prods[i,j]
            if prod >= sim_cutoff and i != j:  # un_similar   similar
                if j not in to_delete:
                    to_delete.append(j)
                    if random.random() < print_prob:  # dot_prods[i,j]
                        print(
                            "Class:{} - sub_classes:{}, sim:{:.3f} - Deleting {}".format(classes[i], sub_classes[j], dot_prods[i, j], sub_classes[j]))
                        print("".format(sub_classes[j]))

    to_delete = sorted(to_delete)[::-1]

    for item in to_delete:
        sub_classes.pop(item)
    print(len(sub_classes))
    return sub_classes


def filter_too_similar(sub_classes, sim_cutoff=0.46, device="cuda", print_prob=1):
    print(len(sub_classes))
    mpnet_model = SentenceTransformer('/home/robot/swf/Label-free-CBM/all-mpnet-base-v2')
    concept_features = mpnet_model.encode(sub_classes)

    dot_prods_m = concept_features @ concept_features.T
    dot_prods_c = _clip_dot_prods(sub_classes, sub_classes)

    dot_prods = (dot_prods_m + 3 * dot_prods_c) / 4

    to_delete = []
    for i in range(len(sub_classes)):
        for j in range(len(sub_classes)):
            prod = dot_prods[i, j]
            if prod <= sim_cutoff and i != j:  # un_similar   similar
                if i not in to_delete and j not in to_delete:
                    to_print = random.random() < print_prob
                    # Deletes the concept with lower average similarity to other sub_classes - idea is to keep more general sub_classes
                    if np.sum(dot_prods[i]) < np.sum(dot_prods[j]):
                        to_delete.append(i)
                        if to_print:
                            print("{} - {} , sim:{:.4f} - Deleting {}".format(sub_classes[i], sub_classes[j], dot_prods[i, j], sub_classes[i]))
                    else:
                        to_delete.append(j)
                        if to_print:
                            print("{} - {} , sim:{:.4f} - Deleting {}".format(sub_classes[i], sub_classes[j], dot_prods[i, j], sub_classes[j]))

    to_delete = sorted(to_delete)[::-1]
    for item in to_delete:
        sub_classes.pop(item)
    print(len(sub_classes))
    return sub_classes


def _clip_dot_prods(list1, list2, device="cuda", clip_name="ViT-B/16", batch_size=500):
    "Returns: numpy array with dot products"
    clip_model, _ = clip.load(clip_name, device=device)
    text1 = clip.tokenize(list1).to(device)
    text2 = clip.tokenize(list2).to(device)

    features1 = []
    with torch.no_grad():
        for i in range(math.ceil(len(text1) / batch_size)):
            features1.append(clip_model.encode_text(text1[batch_size * i:batch_size * (i + 1)]))
        features1 = torch.cat(features1, dim=0)
        features1 /= features1.norm(dim=1, keepdim=True)

    features2 = []
    with torch.no_grad():
        for i in range(math.ceil(len(text2) / batch_size)):
            features2.append(clip_model.encode_text(text2[batch_size * i:batch_size * (i + 1)]))
        features2 = torch.cat(features2, dim=0)
        features2 /= features2.norm(dim=1, keepdim=True)

    dot_prods = features1 @ features2.T
    return dot_prods.cpu().numpy()


name = 'pascal_voc'
with open(f'data/label_category/{name}.txt', 'r') as f:
    categories = f.readlines()
seg_categories = [label.strip() for label in categories]

with open(f"/label_sets/pascal_voc/top5.json", "r") as f:
    sub2super = json.load(f)

# 
sub_classes = [subclass for subclasses in sub2super.values() for subclass in subclasses]

# 
parser = argparse.ArgumentParser(description='GPT Subclass Processor')

parser.add_argument('--sub_sim_cutoff', type=float, default=0.46, help='Similarity cutoff threshold')
parser.add_argument('--sub_to_sup_sim_cutoff', type=float, default=0.46, help='Similarity cutoff threshold')

args = parser.parse_args()

sub_sim_cutoff = args.sub_sim_cutoff
sub_to_sup_sim_cutoff = args.sub_to_sup_sim_cutoff

sub_classes_filter1 = filter_too_similar(sub_classes, sub_sim_cutoff)
# sub_classes_filter2 = filter_too_similar_to_cls(sub_classes, seg_categories, sub_to_sup_sim_cutoff)

filtered_superclass_dict = {}
for superclass, subclasses in sub2super.items():
    filtered_subclasses = [subclass for subclass in sub_classes_filter1 if subclass in subclasses]
    filtered_superclass_dict[superclass] = filtered_subclasses

save_name = "label_sets/pascal_voc/0925/top5_filter.json"


with open('final_mean_iou.txt', 'a') as file:
    # 
    file.write("sub_sim_cutoff:")
    file.write(str(sub_sim_cutoff) + '\n')  # 

with open(save_name, "w") as json_file:
    json.dump(filtered_superclass_dict, json_file)
