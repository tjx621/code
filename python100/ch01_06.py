# 中国有句俗语叫“三天打鱼两天晒网”。
# 某人从1990年1月1日起便开始“三天打鱼两天晒网”，
# 问这个人在以后的某一天中是“打鱼”还是“晒网”。

# 判断是否为闰年。是，则返回1；否，则返回0
def runYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0


# 计算指定日期距离1990年1月1日的天数
def countDay(currentDay):
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDay = 0

    year = 1990
    while year < currentDay['year']:
        if runYear(year) == 1:
            totalDay += 366
        else:
            totalDay += 365
        year += 1

    if runYear(currentDay['year']) == 1:
        perMonth[2] += 1
    i = 0
    while i < currentDay['month']:
        totalDay += perMonth[i]
        i += 1

    totalDay += currentDay['day']

    return totalDay


if __name__ == '__main__':
    while True:
        print('please input date, such as 1999 1 31 : ')
        year, month, day = [int(i) for i in input().split()]
        today = {'year': year, 'month': month, 'day': day}

        totalDay = countDay(today)
        print("%d年%d月%d日与1990年1月1日相差%d天" % (year, month, day, totalDay))

        result = totalDay % 5
        if 0 < result < 4:
            print("今天打鱼")
        else:
            print("今天晒网")
