[CVPRW'24]Training-Free Semantic Segmentation via LLM-Supervision


## Links
Here are [[`Paper`](https://arxiv.org/abs/2404.00701)].


## Checkpoints
SimSeg checkpoints: [Google Drive](https://drive.google.com/drive/folders/1p2hO6LK1usO3q-S8ZtCK8jLaT941WPNW?usp=sharing)  
Please save the `.pth` files under the `ckpts/` folder.

```none
SimSeg
├── ckpts
│   ├── simseg.vit-b.pth
│   ├── simseg.vit-s.pth
```


## Dataset

We follow the [MMSegmentation Dataset Preparation](https://github.com/open-mmlab/mmsegmentation/blob/master/docs/en/dataset_prepare.md) to download and setup the test sets.     
It is recommended to arrange the dataset as the following.  
If your folder structure is different, you may need to change the corresponding paths in config files.

```none
├── data
│   ├── label_category
│   │   ├── pascal_voc.txt
│   │   ├── pascal_context.txt
│   │   ├── coco_stuff.txt
│   ├── VOCdevkit
│   │   ├── VOC2012
│   │   │   ├── JPEGImages
│   │   │   ├── SegmentationClass
│   │   │   ├── ImageSets
│   │   │   │   ├── Segmentation
│   │   │   │   │   ├── train.txt
│   │   │   │   │   ├── val.txt
│   │   ├── VOC2010
│   │   │   ├── JPEGImages
│   │   │   ├── SegmentationClassContext
│   │   │   ├── ImageSets
│   │   │   │   ├── SegmentationContext
│   │   │   │   │   ├── train.txt
│   │   │   │   │   ├── val.txt
│   │   │   ├── trainval_merged.json
│   ├── coco_stuff164k
│   │   ├── images
│   │   │   ├── train2017
│   │   │   ├── val2017
│   │   ├── annotations
│   │   │   ├── train2017
│   │   │   ├── val2017
```


### Pascal VOC

Pascal VOC 2012 could be downloaded from [here](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar).


### Pascal Context

The training and validation set of Pascal Context could be download from [here](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar). 

To split the training and validation set from original dataset, you may download `trainval_merged.json` from [here](https://codalabuser.blob.core.windows.net/public/trainval_merged.json).

Please install [Detail API](https://github.com/zhanghang1989/detail-api) and then run the following command to convert annotations into proper format.

```shell
python tools/convert_datasets/pascal_context.py data/VOCdevkit data/VOCdevkit/VOC2010/trainval_merged.json
```


### COCO Stuff

For COCO Stuff 164k dataset, please run the following commands to download and convert the augmented dataset.

```shell
# download
mkdir coco_stuff164k && cd coco_stuff164k
wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuffthingmaps_trainval2017.zip

# unzip
unzip train2017.zip -d images/
unzip val2017.zip -d images/
unzip stuffthingmaps_trainval2017.zip -d annotations/

# --nproc means 8 process for conversion, which could be omitted as well.
python tools/convert_datasets/coco_stuff164k.py data/coco_stuff164k --nproc 8
```

The details of this dataset could be found at [here](https://github.com/nightrome/cocostuff#downloads).


## Environment
Requirements:
- Python 3.7
- Pytorch 1.10.0
- torchvision 0.11.1
- cuda 11.3
  
Install requirements:
```shell
pip install -r requirements.txt
pip install git+https://github.com/lucasb-eyer/pydensecrf.git

mim install mmcv-full==1.7.0
```


## Evaluation
After
1. Downloading pre-trained checkpoints.
2. Preparing evaluation data.   

The models could be evaluated by running the following scripts.   

#### Pascal VOC
```shell
python3 -m torch.distributed.launch --nproc_per_node=1 --master_port=65533 seg_evaluation_chils.py  --ckpt_path=ckpts/simseg.vit-s.pth --cfg=configs/clip/simseg.vit-s.yaml  --subclass_path=/label_sets/pascal_context/top5.json   --top_cls_num=60  data.valid_name=[pascal_context]
```


## Citation
If you use this paper in your research, please use the following BibTeX entry.

```BibTeX
@article{sun2024training,
  title={Training-Free Semantic Segmentation via LLM-Supervision},
  author={Sun, Wenfang and Du, Yingjun and Liu, Gaowen and Kompella, Ramana and Snoek, Cees GM},
  journal={arXiv preprint arXiv:2404.00701},
  year={2024}
}
```

## License
See [LICENSE](LICENSE) for details.
