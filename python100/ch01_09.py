# 二分查找

if __name__ == "__main__":
    a = [1, 12, 56, 59, 78, 89, 90]
    b = 12

    low = 0
    high = len(a) - 1
    k = -1

    while low <= high:
        mid = (low + high) // 2
        if b < a[mid]:
            high = mid - 1
        elif b > a[mid]:
            low = mid + 1
        else:
            k = mid
            break

    if k >= 0:
        print("m = %d , index = %d" % (b, k))
    else:
        print("Not be found!")
