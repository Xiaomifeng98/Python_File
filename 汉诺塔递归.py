def hanoi(n, x, y, z):
    if n == 1:
        print("将第", n, "块从", x, "移动到", z)
    else:
        hanoi(n - 1, x, z, y)  #将前n - 1个盘子从x移动到y上
        print("将第", n, "块从", x, "移动到", z)  #将最底下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z)  #将y上的n - 1个盘子移动到z上

n = int(input("请输入汉诺塔的层数："))
hanoi(n, 'X', 'Y', 'Z')
