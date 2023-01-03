# 中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱百鸡问题”：
# 一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，现在要用百钱买百鸡，请问公鸡、母鸡、小鸡各多少只？

# g m x
# g+m+x=100
# g*5+m*3+x/3=100
# x % 3 = 0

# 公鸡 rooster
# 母鸡 hen
# 小鸡 chick

for rooster in range(100):
    for hen in range(100):
        for chick in range(100):
            if rooster + hen + chick == 100:
                if chick % 3 == 0:
                    if rooster*5+hen*3+chick/3==100:
                        print("公鸡：%d，母鸡：%d，小鸡：%d"%(rooster,hen,chick))
