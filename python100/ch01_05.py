# 小明有5本新书，要借给A、B、C三位小朋友，若每人每次只能借1本，则可以有多少种不同的借法？

count = 0
for a in range(1,6):
    for b in range(1,6):
        for c in range(1, 6):
            if a != b and a != c and b != c:
                print('A:%2d B:%2d C:%2d'%(a,b,c),end=' || ')
                count += 1
                if count % 4 == 0:
                    print()

print('共有%d种借阅方法' % count)


