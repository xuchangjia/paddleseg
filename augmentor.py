import Augmentor
 
#注意此处两个文件夹中图片名必须完全一致，包括后缀名
p = Augmentor.Pipeline('/home/bzl/Documents/rk_seg/PaddleSeg/data/seg_data') #images中是原图像
# p.ground_truth('/home/bzl/Documents/rk_seg/PaddleSeg/data/indoor_lunjiao_seg/mask') #labels中是掩码图像

# # 图像左右互换： 按照概率0.5执行
# p.flip_left_right(probability=1)
# p.process()

# p.flip_top_bottom(probability=1)
# p.process()

# # 图像放大缩小： 按照概率0.8执行，面积为原始图0.85倍
# p.zoom_random(probability=1, percentage_area=0.7)
# p.process()
 
# # #scale_factor表示缩放比例，只能大于1，且为等比放大。
# p.scale(probability=1, scale_factor=1.3)
# p.process()
 
# # #小块变形
# p.random_distortion(probability=1,grid_width=10,grid_height=10, magnitude=20)
# p.process()

# #随机裁剪(random_crop)
# p.crop_random(probability=1, percentage_area=0.8, randomise_percentage_area=True)
# p.process()

# # 透视变换
# p.skew(probability=1, magnitude=0.8)
# p.process()

# # # 剪切
# p.shear(probability=1, max_shear_left=15, max_shear_right=15)
# p.process()

##   变化小

# # 图像旋转： 按照概率0.8执行，范围在0-25之间
# p.rotate(probability=1, max_left_rotation=25, max_right_rotation=25)
# p.process()

# #随机亮度增强/减弱，min_factor, max_factor为变化因子，决定亮度变化的程度，可根据效果指定
# p.random_brightness(probability=1, min_factor=0.7, max_factor=1.2)
# p.process()
 
#随机颜色/对比度增强/减弱
# p.random_color(probability=1, min_factor=0.0, max_factor=1.5)
# p.process()

# p.random_contrast(probability=1, min_factor=0.7, max_factor=1.2)
# p.process()
 
# #随机剪切(shear)  max_shear_left，max_shear_right为剪切变换角度  范围0-25
# p.shear(probability=1, max_shear_left=10, max_shear_right=10)
# p.process()
 
 
# #随机翻转(flip_random)
# p.flip_random(probability=1)
# p.process()

# 旋转90
p.rotate90(probability=0.5)

# # 遮挡(暂时不需要)
# p.random_erasing(probability=1, rectangle_area=0.2)
# p.process() 

# 最终扩充的数据样本数可以更换为100。1000等
p.sample(10)

