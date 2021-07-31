import pandas as pd
import numpy as np

# 输入 三次纯音测听结果 年龄 性别
pta1r = [20, 25, 40, 45, 50, 60]
pta1l = [20, 25, 40, 50, 75, 75]
pta2r = [15, 25, 40, 45, 45, 65]
pta2l = [25, 25, 40, 55, 75, 85]
pta3r = [20, 25, 40, 50, 45, 55]
pta3l = [25, 25, 35, 55, 70, 80]
age = 38    # 18-80
gender = 1  # 0：女 or 1：男
# 输入有效性的检验  还应注意三次检查的时间间隔至少3天

# 读取校正矩阵
adjust = pd.read_csv("corr.csv")
# print('原始校正矩阵', adjust)
adjust_male = adjust[['male500', 'male1000', 'male2000', 'male3000', 'male4000', 'male6000']]
adjust_female = adjust[['female500', 'female1000', 'female2000', 'female3000', 'female4000', 'female6000']]
adjust_now = 0
if gender == 0:
    adjust_now = adjust_female.iloc[int(age/10)]  # int()取整数  .iloc 位置函数
elif gender == 1:
    adjust_now = adjust_male.iloc[int(age/10)]
else:
    print('性别输入有误！')
    adjust_now = 0

pta_table = [pta1r, pta1l, pta2r, pta2l, pta3r, pta3l]
pta_table = np.array(pta_table)
print('输入的听力结果', pta_table)
print('校正值：', adjust_now)
# 校正
list = [0, 1, 2, 3, 4, 5]
for i in list:
    pta_table[i] = pta_table[i]-adjust_now
print('校正的听力结果', pta_table)

r500 = min(pta_table[0][0], pta_table[2][0], pta_table[4][0])
r1000 = min(pta_table[0][1], pta_table[2][1], pta_table[4][1])
r2000 = min(pta_table[0][2], pta_table[2][2], pta_table[4][2])
l500 = min(pta_table[1][0], pta_table[3][0], pta_table[5][0])
l1000 = min(pta_table[1][1], pta_table[3][1], pta_table[5][1])
l2000 = min(pta_table[1][2], pta_table[3][2], pta_table[5][2])

rm500 = np.mean([pta_table[0][0], pta_table[2][0], pta_table[4][0]])
rm1000 = np.mean([pta_table[0][1], pta_table[2][1], pta_table[4][1]])
rm2000 = np.mean([pta_table[0][2], pta_table[2][2], pta_table[4][2]])
lm500 = np.mean([pta_table[1][0], pta_table[3][0], pta_table[5][0]])
lm1000 = np.mean([pta_table[1][1], pta_table[3][1], pta_table[5][1]])
lm2000 = np.mean([pta_table[1][2], pta_table[3][2], pta_table[5][2]])

r3000 = min(pta_table[0][3], pta_table[2][3], pta_table[4][3])
r4000 = min(pta_table[0][4], pta_table[2][4], pta_table[4][4])
r6000 = min(pta_table[0][5], pta_table[2][5], pta_table[4][5])
l3000 = min(pta_table[1][3], pta_table[3][3], pta_table[5][3])
l4000 = min(pta_table[1][4], pta_table[3][4], pta_table[5][4])
l6000 = min(pta_table[1][5], pta_table[3][5], pta_table[5][5])

hight = np.array([[r3000, r4000, r6000, l3000, l4000, l6000]])
# print(hight)
BHFTA = round(np.mean(hight))
# print(round(np.mean(hight)))
print('BHFTA=', BHFTA)

# BHFTA >=40 继续
# MTMV left and right
MTMV_right = round(np.mean([r500, r1000, r2000])*0.9 + r4000*0.1)  # 是否需要四舍五入取整
print('mtmv_right =', MTMV_right)
MTMV_left = round(np.mean([l500, l1000, l2000])*0.9 + l4000*0.1)
print('mtmv_left =', MTMV_left)

# output diagnosis and disability
diagnosis = "无噪声聋"

if BHFTA < 40:
    diagnosis = "无噪声聋"
elif min(MTMV_right, MTMV_left) >= 56:
    diagnosis = "重度噪声聋"
elif min(MTMV_right, MTMV_left) >= 41:
    diagnosis = "中度噪声聋"
elif min(MTMV_right, MTMV_left) >= 26:
    diagnosis = "轻度噪声聋"
else:
    diagnosis = "无噪声聋"
print('参考诊断结果为：', diagnosis)

# disability 听力障碍伤残鉴定
hearing_right = np.mean([rm500, rm1000, rm2000])  # 是否需要取整
hearing_left = np.mean([lm500, lm1000, lm2000])
hearing_both_mean = (min(hearing_right, hearing_left)*4 + max(hearing_right, hearing_left))/5
print('双耳平均听阈:', hearing_both_mean, '右耳听力:', hearing_right, '左耳听力:',  hearing_left)
disability = "无伤残"

if hearing_both_mean >= 91:
    disability = "四级伤残"
elif hearing_both_mean >= 81:
    disability = "五级伤残"
elif hearing_both_mean >= 71:
    disability = "六级伤残"
elif hearing_both_mean >= 56:
    disability = "七级伤残"
elif hearing_both_mean >= 41 or max(hearing_right, hearing_left) >= 91:
    disability = "八级伤残"
elif hearing_both_mean >= 31 or max(hearing_right, hearing_left) >= 71:
    disability = "九级伤残"
elif hearing_both_mean >= 26 or max(hearing_right, hearing_left) >= 56:
    disability = "十级伤残"
else:
    disability = "无伤残"
print('参考伤残鉴定：', disability)

# save the data


