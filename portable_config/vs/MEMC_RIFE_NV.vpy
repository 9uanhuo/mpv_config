### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4.6) 补帧，性能要求较高，N卡专用

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# 用户选项 #
############

H_Pre = 1440
Lt_D2k = False
Model = 40
Sc_Mode = 1
Fps_Num = 2
T_Tta = False
Ext_Proc = True
Gpu = 0
Gpu_T = 2
St_Eng = False
Ws_Size = 0
Lk_Fmt = False
## 整数，预降低处理源高度（填你的显示器高度）
## <True|False> 是否对超过DCI2K分辨率的源进行补帧
## <40|46|48> 使用的模型
## <0|1|2> 场景切换检测的模式，0为禁用
## <2|3|4> 补帧倍率
## <True|False> 是否使用ensemble版模型
## <True|False> 是否使用外部的填充裁切处理（禁用将强制锁定为静态引擎）
## 使用的显卡序号，0为排序一号
## <1|2|3> 显卡线程数
## <True|False> 是否使用静态引擎（需要对不同分辨率的源各进行预处理）；动态引擎自适应不同分辨率（QVGA→DCI4K）
## 整数，约束显存（MiB），静态引擎的最小值为128（动态引擎自动双倍），设为低于此数的值即最大化利用
## <True|False> 锁定像素格式为yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.RIFE_NV(clip, lt_d2k=Lt_D2k, model=Model, sc_mode=Sc_Mode, fps_num=Fps_Num, t_tta=T_Tta, ext_proc=Ext_Proc, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)

clip.set_output()
