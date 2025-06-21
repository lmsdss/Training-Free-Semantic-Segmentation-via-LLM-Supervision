def openai_imagenet_template(classname):
    return [temp.format(classname) for temp in pascal_voc_imagenet_templates]

def openai_imagenet_template_sub(classname, subclassname):
    print([temp.format(subclassname, classname) for temp in imagenet_templates_sub])
    return [temp.format(subclassname, classname) for temp in imagenet_templates_sub]


pascal_voc_imagenet_templates = [   # ALL  58.30   simseg    60.61  num10   61.65  num  7
    'a photo of one {}.',  # 0.5689   =====    58.68   num10      59.37  num7
    'a photo of a cool {}.',  # 0.5685    =====  57.44  num10    58.22   num7
    'a photo of a weird {}.',  # 0.5660   ======  58.02  num10   58.89  num7
    'a photo of a nice {}.',  # 0.5655 =====   58.09  num10    58.84   num7
    'a jpeg corrupted photo of a {}.',  # 0.5615  =====   58.31  num10  59.19  num7   T6
    'a pixelated photo of a {}.',  # 0.5588   =====   58.44  num10   59.16  num7   T3
    'a photo of a {}.',  # 0.5581   =====            58.48   num10   59.44   num7   T4
    'a cropped photo of the {}.',  # 0.5492  =====   57.39   num10    58.11   num7   T5
    'a bright photo of a {}.',  # 0.5482  =====     57.62    num10   58.45  num7    T7
    'a cropped photo of a {}.',  # 0.5472   =====   57.17    num10   58.32  num7   T8
    'a bad photo of the {}.',  # 0.5452  =====   57.24     num10   57.39  num7    T9
    'a drawing of a {}.',  # 0.5418    =====   57.54   num10    57.69  num7     T1
    'a photo of the cool {}.',  # 0.5405 =====   54.89   num10   56.03  num7    T2
]

# 'a photo of many {}.',  # 0.5173     =====            55.51         num7         T10    chuwai
# 'a tattoo of a {}.',  # 0.5382       =====     55.39   num7   T11    chuwai
# 'a photo of many {}.'
# pascal_voc_imagenet_templates_v2 = [
#     'a photo of one {}.',  # 0.5689
#     'a photo of a cool {}.',  # 0.5685
#     'a photo of a weird {}.',  # 0.5660
#     'a photo of a nice {}.',  # 0.5655
#     'a jpeg corrupted photo of a {}.',  # 0.5615
#     'a pixelated photo of a {}.',  # 0.5588
#     'a photo of a {}.',  # 0.5581
#     'a good photo of a {}.',  # 0.5535
#     'a photo of the weird {}.',  # 0.5519
#     'itap of a {}.',  # 0.5511
# ]

imagenet_templates0904 = [  #
    'a photo of a {}, which (is/has/etc) aks@, pg2f',  # 0.5006
    'a photo of a {}, which (is/has/etc) jmhj, !J#m',  # 0.4941
    'a photo of a {}, which (is/has/etc) foot loud',  # 0.5362
    'a photo of a {}, which (is/has/etc) life ring',  # 0.5224
]

coco_imagenet_templates = [
    'a photo of a weird {}.',  # 0.2703
    'a jpeg corrupted photo of a {}.',  # 0.2634
    'a photo of a {}.',  # 0.2634
    'a photo of the weird {}.',  # 0.2627
    'a photo of one {}.',  # 0.2616
    'a low resolution photo of a {}.',  # 0.2609
    'a bad photo of a {}.',  # 0.2604
]

pascal_context_imagenet_templates = [
    'a photo of a nice {}.',  # 0.2577
    'a jpeg corrupted photo of the {}.',  # 0.2569
    'a photo of the nice {}.',  # 0.2568
    'a bad photo of the {}.',  # 0.2563
    'a jpeg corrupted photo of a {}.',  # 0.2562
    'a good photo of the {}.',  # 0.0.2561
    'itap of a {}.',  # 0.2557
    'a photo of one {}.',  # 0.2548
    'a photo of a {}.',  # 0.2526
    'a photo of the cool {}.',  # 0.2509
    'a good photo of a {}.',  # 0.2501
]
imagenet_templates = [
    'a bad photo of a {}.',  # 0.5434  / 0.2474/ 0.2604
    'a photo of many {}.',  # 0.5173 /  0.2474 / 0.2494
    'a sculpture of a {}.',  # 0.4799  / 0.2176 / 0.2418
    'a photo of the hard to see {}.',  # 0.4995 / 0.2227 / 0.2267
    'a low resolution photo of the {}.',  # 0.5014 / 0.2283/  0.2363
    'a rendering of a {}.',  # 0.5304 / 0.2343/ 0.2516
    'graffiti of a {}.',  # 0.4922  / 0.2367  # 0.2365
    'a bad photo of the {}.',  # 0.5452 / 0.2563/  0.2510
    'a cropped photo of the {}.',  # 0.5492 / 0.2391/ 0.2535
    'a tattoo of a {}.',  # 0.5382 / 0.2201/ 0.2557
    'the embroidered {}.',  # 0.4974 / 0.2305/ 0.2404
    'a photo of a hard to see {}.',  # 0.5035 /0.2197/  0.2307
    'a bright photo of a {}.',  # 0.5482 /0.2432/ 0.2546
    'a photo of a clean {}.',  # 0.5148 / 0.2451/ 0.2476
    'a photo of a dirty {}.',  # 0.5042 / 0.2353/ 0.2402
    'a dark photo of the {}.',  # 0.4577 / 0.2263 / 0.2190
    'a drawing of a {}.',  # 0.5418 /0.2415/ 0.2578
    'a photo of my {}.',  # 0.5129 /0.2488/ 0.2263
    'the plastic {}.',  # 0.4885 /0.2248 /0.2332
    'a photo of the cool {}.',  # 0.5405 /  0.2509/ 0.2444
    'a close-up photo of a {}.',  # 0.2492/ 0.2397/ 0.2492
    'a black and white photo of the {}.',  # 0.5309 / 0.2382/ 0.2408
    'a painting of the {}.',  # 0.5077 / 0.2370 / 0.2447
    'a painting of a {}.',  # 0.5245 / 0.2317/ 0.2519
    'a pixelated photo of the {}.',  # 0.5394 /0.2433/ 0.2471
    'a sculpture of the {}.',  # 0.4827/ 0.2171/0.2412
    'a bright photo of the {}.',  # 0.5278/ 0.2411/0.2477
    'a cropped photo of a {}.',  # 0.5472/ 0.2416/0.2555
    'a plastic {}.',  # 0.5206 / 0.2218/0.2437
    'a photo of the dirty {}.',  # 0.4554/ 0.2223/0.2260
    'a jpeg corrupted photo of a {}.',  # 0.5615/0.2562/0.2634
    'a blurry photo of the {}.',  # 0.5073/0.2402/0.2367
    'a photo of the {}.',  # 0.5055/0.2487/0.2389
    'a good photo of the {}.',  # 0.5203/0.2561/0.2448
    'a rendering of the {}.',  # 0.4869/ 0.2235/0.2360
    'a {} in a video game.',  # 0.4925/0.2265/ 0.2440
    'a photo of one {}.',  # 0.5689/0.2548/0.2616
    'a doodle of a {}.',  # 0.5152/ 0.2283/ 0.2417
    'a close-up photo of the {}.',  # 0.5124/0.2399/0.2381
    'a photo of a {}.',  # 0.5581/0.2526/0.2634
    'the origami {}.',  # 0.4710/0.2068/0.2333/
    'the {} in a video game.',  # 0.4944/0.2359/0.2366
    'a sketch of a {}.',  # 0.5216/0.2355/0.2430
    'a doodle of the {}.',  # 0.5164/0.2297/0.2370
    'a origami {}.',  # 0.4806/0.2038/0.2384
    'a low resolution photo of a {}.',  # 0.5030/0.2429/0.2609
    'the toy {}.',  # 0.4881/0.2044/0.2262
    'a rendition of the {}.',  # 0.5286/0.2401/0.2544
    'a photo of the clean {}.',  # 0.4648/0.2259/0.2246
    'a photo of a large {}.',  # 0.5452/0.2449/0.2582
    'a rendition of a {}.',  # 0.5112/0.2379/0.2512
    'a photo of a nice {}.',  # 0.5655/0.2577/0.2487
    'a photo of a weird {}.',  # 0.5660/0.2433/0.2703
    'a blurry photo of a {}.',  # 0.5247/0.2431/0.2504
    'a cartoon {}.',  # 0.5342/0.2110/0.2465
    'art of a {}.',  # 0.4650/0.2155/0.2384
    'a sketch of the {}.',  # 0.5097/0.2431/0.2350
    'a embroidered {}.',  # 0.4990/0.2164/0.2410
    'a pixelated photo of a {}.',  # 0.5588/0.2448/0.2568
    'itap of the {}.',  # 0.5338/0.2477/0.2480
    'a jpeg corrupted photo of the {}.',  # 0.5440/0.2569/0.2489
    'a good photo of a {}.',  # 0.5535/0.2501/0.2582
    'a plushie {}.',  # 0.4729/0.2062/0.2266
    'a photo of the nice {}.',  # 0.5437/0.2568/0.2425
    'a photo of the small {}.',  # 0.5035/0.2256/0.2331
    'a photo of the weird {}.',  # 0.5519/0.2498/0.2627
    'the cartoon {}.',  # 0.5063/0.2011/0.2375
    'art of the {}.',  # 0.4824/0.2173/0.2276
    'a drawing of the {}.',  # 0.5296/0.2471/0.2478
    'a photo of the large {}.',  # 0.5442/0.2458/0.2519
    'a black and white photo of a {}.',  # 0.5490/0.2391/0.2499
    'the plushie {}.',  # 0.4699/0.2049/0.2224
    'a dark photo of a {}.',  # 0.4689/0.2292/0.2321
    'itap of a {}.',  # 0.5511/0.2557/0.2558
    'graffiti of the {}.',  # 0.4859/0.2343/0.2433
    'a toy {}.',  # 0.5113/0.2116/0.2320
    'itap of my {}.',  # 0.5269/0.2396/0.2416
    'a photo of a cool {}.',  # 0.5685/0.2468/0.2565
    'a photo of a small {}.',  # 0.5100/0.2244/0.2463
    'a tattoo of the {}.',  # 0.5328/0.2149/0.2566
]

imagenet_templates_sub = [
    'a bad photo of a {} belonging to the {} category.',  # 0.5434  / 0.2604
    'a photo of many {} belonging to the {} category.',  # 0.5173 / 0.2494
    'a sculpture of a {} belonging to the {} category.',  # 0.4799  / 0.2418
    'a photo of the hard to see {} belonging to the {} category.',  # 0.4995  / 0.2267
    'a low resolution photo of the {} belonging to the {} category.',  # 0.5014 /  0.2363
    'a rendering of a {} belonging to the {} category.',  # 0.5304 / 0.2516
    'graffiti of a {} belonging to the {} category.',  # 0.4922  / 0.2365
    'a bad photo of the {} belonging to the {} category.',  # 0.5452 /  0.2510
    'a cropped photo of the {} belonging to the {} category.',  # 0.5492 /  0.2535
    'a tattoo of a {} belonging to the {} category.',  # 0.5382 / 0.2557
    'the embroidered {} belonging to the {} category.',  # 0.4974 / 0.2404
    'a photo of a hard to see {} belonging to the {} category.',  # 0.5035 / 0.2307
    'a bright photo of a {} belonging to the {} category.',  # 0.5482 / 0.2546
    'a photo of a clean {} belonging to the {} category.',  # 0.5148 / 0.2476
    'a photo of a dirty {} belonging to the {} category.',  # 0.5042 / 0.2402
    'a dark photo of the {} belonging to the {} category.',  # 0.4577 / 0.2190
    'a drawing of a {} belonging to the {} category.',  # 0.5418 / 0.2578
    'a photo of my {} belonging to the {} category.',  # 0.5129 / 0.2263
    'the plastic {} belonging to the {} category.',  # 0.4885 / 0.2332,
    'a photo of the cool {} belonging to the {} category.',  # 0.5405 /  0.2444
    'a close-up photo of a {} belonging to the {} category.',  # 0.2492
    'a black and white photo of the {} belonging to the {} category.',  # 0.5309 / 0.2408
    'a painting of the {} belonging to the {} category.',  # 0.5077 / 0.2447
    'a painting of a {} belonging to the {} category.',  # 0.5245 / 0.2519
    'a pixelated photo of the {} belonging to the {} category.',  # 0.5394 / 24.71
    'a sculpture of the {} belonging to the {} category.',  # 0.4827
    'a bright photo of the {} belonging to the {} category.',  # 0.5278
    'a cropped photo of a {} belonging to the {} category.',  # 0.5472
    'a plastic {} belonging to the {} category.',  # 0.5206
    'a photo of the dirty {} belonging to the {} category.',  # 0.4554
    'a jpeg corrupted photo of a {} belonging to the {} category.',  # 0.5615
    'a blurry photo of the {} belonging to the {} category.',  # 0.5073
    'a photo of the {} belonging to the {} category.',  # 0.5055
    'a good photo of the {} belonging to the {} category.',  # 0.5203
    'a rendering of the {} belonging to the {} category.',  # 0.4869
    'a {} belonging to the {} category in a video game.',  # 0.4925
    'a photo of one {} belonging to the {} category.',  # 0.5689
    'a doodle of a {} belonging to the {} category.',  # 0.5152
    'a close-up photo of the {} belonging to the {} category.',  # 0.5124
    'a photo of a {} belonging to the {} category.',  # 0.5581
    'the origami {} belonging to the {} category.',  # 0.4710
    'the {} belonging to the {} category in a video game.',  # 0.4944
    'a sketch of a {} belonging to the {} category.',  # 0.5216
    'a doodle of the {} belonging to the {} category.',  # 0.5164
    'a origami {} belonging to the {} category.',  # 0.4806
    'a low resolution photo of a {} belonging to the {} category.',  # 0.5030
    'the toy {} belonging to the {} category.',  # 0.4881
    'a rendition of the {} belonging to the {} category.',  # 0.5286
    'a photo of the clean {} belonging to the {} category.',  # 0.4648
    'a photo of a large {} belonging to the {} category.',  # 0.5452
    'a rendition of a {} belonging to the {} category.',  # 0.5112
    'a photo of a nice {} belonging to the {} category.',  # 0.5655
    'a photo of a weird {} belonging to the {} category.',  # 0.5660
    'a blurry photo of a {} belonging to the {} category.',  # 0.5247
    'a cartoon {} belonging to the {} category.',  # 0.5342
    'art of a {} belonging to the {} category.',  # 0.4650
    'a sketch of the {} belonging to the {} category.',  # 0.5097
    'a embroidered {} belonging to the {} category.',  # 0.4990
    'a pixelated photo of a {} belonging to the {} category.',  # 0.5588
    'itap of the {} belonging to the {} category.',  # 0.5338
    'a jpeg corrupted photo of the {} belonging to the {} category.',  # 0.5440
    'a good photo of a {} belonging to the {} category.',  # 0.5535
    'a plushie {} belonging to the {} category.',  # 0.4729
    'a photo of the nice {} belonging to the {} category.',  # 0.5437
    'a photo of the small {} belonging to the {} category.',  # 0.5035
    'a photo of the weird {} belonging to the {} category.',  # 0.5519
    'the cartoon {} belonging to the {} category.',  # 0.5063
    'art of the {} belonging to the {} category.',  # 0.4824
    'a drawing of the {} belonging to the {} category.',  # 0.5296
    'a photo of the large {} belonging to the {} category.',  # 0.5442
    'a black and white photo of a {} belonging to the {} category.',  # 0.5490
    'the plushie {} belonging to the {} category.',  # 0.4699
    'a dark photo of a {} belonging to the {} category.',  # 0.4689
    'itap of a {} belonging to the {} category.',  # 0.5511
    'graffiti of the {} belonging to the {} category.',  # 0.4859
    'a toy {} belonging to the {} category.',  # 0.5113
    'itap of my {} belonging to the {} category.',  # 0.5269
    'a photo of a cool {} belonging to the {} category.',  # 0.5685
    'a photo of a small {} belonging to the {} category.',  # 0.5100
    'a tattoo of the {} belonging to the {} category.',  # 0.5328
]
