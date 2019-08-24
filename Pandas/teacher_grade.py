import pandas as pd

teacher_csv = "./teacher_grade_input.csv"

obj = pd.read_csv(teacher_csv)

# 删除几个留学生
# 直接把留学生姓名匹配的那一行删除
obj=obj[~obj['学生姓名'].isin(['赵宇童'])]
obj=obj[~obj['学生姓名'].isin(['王莉游'])]
obj=obj[~obj['学生姓名'].isin(['阿雅卡'])]
obj=obj[~obj['学生姓名'].isin(['都乐'])]
obj=obj[~obj['学生姓名'].isin(['郝悦'])]
obj=obj[~obj['学生姓名'].isin(['马克西姆'])]

# 统计某一列的所有不同元素
teacher_list = pd.unique(obj['语文选课老师'])
class_name_list = pd.unique(obj['语文选课'])

# 新建表头，为了后面不断加行
new_df = pd.DataFrame(columns=('教学班', '教师', '参考人数',\
    '均分', '95分以上', '比例', '90分以上', '比例', '85分以上',\
    '比例', '60分以上', '比例', '前100匹配度', '前100非匹配学生'))

def check_back_leg(data_piece):
    back_leg_list = []
    total = back_leg = 0
    # 按行遍历一个DataFrame
    for index, row in data_piece.iterrows():
        if row['总成绩排名'] <= 100:
            total = total + 1
            if row['语文排名'] > 150:
                back_leg = back_leg + 1
                back_leg_list.append(row['学生姓名'])
    
    if back_leg == 0:
        back_leg_ratio = 0
        back_leg_content = '无'
    else:
        back_leg_ratio = back_leg / total
        back_leg_content = back_leg_list
    return back_leg_ratio, back_leg_content


i = 0
for t in teacher_list:
    for c in class_name_list:
        # 在大的DataFrame里通过特定的列值筛选出一些行
        data_piece = obj[(obj['语文选课老师']==t) & (obj['语文选课']==c)]
        total_stu = data_piece.shape[0]  # 行数
        if (total_stu == 0):
            continue
        avg_grad = sum(data_piece['语文成绩'])/total_stu
        over_95_stu = data_piece[data_piece['语文成绩'] >= 95].shape[0]
        over_95_ratio = over_95_stu / total_stu
        over_90_stu = data_piece[data_piece['语文成绩'] >= 90].shape[0]
        over_90_ratio = over_90_stu / total_stu
        over_85_stu = data_piece[data_piece['语文成绩'] >= 85].shape[0]
        over_85_ratio = over_85_stu / total_stu
        over_60_stu = data_piece[data_piece['语文成绩'] >= 60].shape[0]
        over_60_ratio = over_60_stu / total_stu

        back_leg_ratio, back_leg_content = check_back_leg(data_piece)

        row_all = [c, t, total_stu,\
            avg_grad, over_95_stu, over_95_ratio,\
            over_90_stu, over_90_ratio,\
            over_85_stu, over_85_ratio,\
            over_60_stu, over_60_ratio,\
            1 - back_leg_ratio, "，".join(back_leg_content)]
        new_df.loc[i] = row_all  # 往新的表里添加行
        i = i + 1
new_df.to_csv("./result.csv", index=False, sep=',')
