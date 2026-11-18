#简单的药物剂量计算器一枚,加入退出、循环、防报错
print('---Welcome to use drug calculator2.0(enter q to exit) ---')
#定义已知
while True:
    weight_input = input("please enter the weight of your mouse(g):") #单位：g
    if weight_input.lower() == "q":
        print("The program has ended.Wishing you a successful experiment.Bye~!")
        break
    #打破循环，然后检查剂量值
    dose_input = input("please enter the dosage to be administered(ml/kg):") #单位：ml/kg
    if dose_input.lower() == "q":
            print("The program has ended.Wishing you a successful experiment.Bye~!")
            break
    #开始处理数据并防止报错
    try:
        weight=float(weight_input)
        dose=float(dose_input)
        total_drug = (weight / 1000)*dose
#输出结果
        print('----------------------------------------')
        print(f"The amount of drug you need to weigh is {total_drug}mg.^w^")
    except ValueError:
        print("你给我输入的啥呀这是！不是纯数字不给算喵")