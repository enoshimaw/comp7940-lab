def print_factor(x):
    """
    Exercise 2: 函数定义
    打印一个数字的所有因数
    """
    print(f"Factors of {x}:")
    for i in range(2, x):
        if x % i == 0:
            print(i)
    print("-" * 20) # 打印一条分隔线

def main():
    # Exercise 1: 简单的循环 (针对数字 52633)
    print("Exercise 1 Output:")
    x = 52633
    for i in range(2, x):
        if x % i == 0:
            print(i)
    print("-" * 20)

    # Exercise 3: 列表遍历
    print("Exercise 3 Output:")
    l = [52633, 8137, 1024, 999]
    for num in l:
        print_factor(num)

if __name__ == '__main__':
    main()