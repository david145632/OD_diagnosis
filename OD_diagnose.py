#! /usr/bin/python3

# 显示免责声明
print('本网页由XXX共同开发,主要用途是为职业病诊断参考,所得结论不具有法律意义,请知悉!')

# 使用者提交相关信息,
print('请提供诊断所需相关信息！输入 q 退出。')
usr_info = {}
name = input('请输入您的姓名: ')
if name == 'q':
    exit(0)
usr_info['name'] = name
age = input('请输入您的年龄（整数）： ')
if age == 'q':
    exit(0)
while True:
    try:
        age = int(age)
        if 1 <= age <= 100:
            break
        else:
            age = input('请输入1-100之间的整数： ')
            if age == 'q':
                exit(0)
    except ValueError:
        age = input('请输入您的年龄（整数）： ')
        if age == 'q':
            exit(0)
usr_info['age'] = age
while True:
    gender = input('请输入您的性别（男/女）: ')
    if gender == 'q':
        exit(0)
    elif gender in ['男', '女']:
        break
    else:
        print('输入有误，请重新输入！')
        continue
title = '先生' if gender == '男' else '女士'
usr_info['gender'] = gender
while True:
    work_year = input('您接触噪声的工龄是否满三年？（是/否） ')
    if work_year == 'q':
        exit(0)
    elif work_year in ['是', '否']:
        break
    else:
        print('输入有误，请重新输入！')
        continue
usr_info['work_year'] = work_year
# 输入纯音测听的结果


# 将信息保存到文件user_data.txt
data = open('user_data.txt', 'a', encoding='utf-8')
data.write(str(usr_info)+'\n')
data.close()

# 根据用户提供的信息,对疾病做出判断


# 输出参考结论
print(f'{name}{title}, 根据您提供的信息，初步判断您是否患某病?')
