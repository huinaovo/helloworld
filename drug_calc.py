#简单的药物剂量计算器一枚
print('---Welcome to use drug calculator1.0 ---')
#定义已知
weight = float(input("please enter the weight of your mouse(g):")) #单位：g
dose = float(input("please enter the dosage to be administered(ml/kg):")) #单位：ml/kg
total_drug = (weight / 1000)*dose
#输出结果
print('----------------------------------------')
print(f"The amount of drug you need to weigh is {total_drug}mg.QAQ")