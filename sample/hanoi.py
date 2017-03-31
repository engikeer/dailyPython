def move(n, a, b, c):  # N代表盘子个数，A、B、C代表三根柱子
    if n == 1:
        # A上只有一个盘子
        # 将A上的盘子放在C上
        print('move', a, '-->', c)

    else:
        # A上有N（N>1）个盘子
        # 1.把A上面的N-1个盘子借助C放到B上
        move(n-1, a, c, b)
        # 2.把A最下面的盘子放在C上
        print('move', a, '-->', c)
        # 3.把B上的N-1个盘子借助A放在C上（调用步骤1的函数）
        move(n-1,b,a,c)

n = int(input('请输入汉诺塔的层数:'))
move(n, 'A', 'B', 'C')
