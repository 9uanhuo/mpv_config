### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### NL-means降噪，N卡专用版
### 另有着色器版本，例如 ../shaders/nlmeans.glsl

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# 用户选项 #
############

Blur_M = 2
Frame_Num = 1
Rad_Sw = 2
Rad_Snw = 2
Nr_Lv = 3.0
Gpu = 0
Gpu_T = 2
## <0|1|2> 分离模式。0为不使用
## 整数，降噪帧数
## 整数，搜索窗口半径
## 整数，近邻窗口半径
## 浮点，降噪强度
## 指定显卡序号，0为排序一号
## <1|2|3> 显卡线程数

clip = k7f.NLM_NV(clip, blur_m=Blur_M, frame_num=Frame_Num, rad_sw=Rad_Sw, rad_snw=Rad_Snw, nr_lv=Nr_Lv, gpu=Gpu, gpu_t=Gpu_T)

clip.set_output()
