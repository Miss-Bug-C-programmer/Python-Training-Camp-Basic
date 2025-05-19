"""
练习: if-elif-else 条件语句

描述：
根据学生的成绩判断其等级。
- 成绩 >= 90: 优秀
- 成绩 >= 80: 良好
- 成绩 >= 70: 中等
- 成绩 >= 60: 及格
- 成绩 < 60: 不及格

请补全下面的函数，实现成绩等级判断。
"""

def check_grade(score):
    """
    根据分数返回等级
    
    参数:
    - score: 学生分数，0-100的整数
    
    返回:
    - 对应的等级：优秀、良好、中等、及格、不及格
    """
    # 请在下方编写代码
    if score >= 90:
        return "优秀"
    if 80 <= score < 90:
        return "良好"
    if 70 <= score < 80:
        return "中等"
    if 60 <= score < 70:
        return "及格"

    if score < 60:
        return "不及格"
    pass 