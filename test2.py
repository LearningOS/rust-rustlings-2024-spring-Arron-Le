from math import exp 

def f(x):
    return (x - 3*x**2 + 2*x**3 + exp(x))**0.5

def romberg_integration(f, a, b, n_max, tolerance):
    # 使用自适应步长的Romberg积分方法
    h = b - a  # 计算初始步长
    R = [[0] * n_max for _ in range(n_max)]  # 初始化Romberg表格
    R[0][0] = (h / 2) * (f(a) + f(b))  # 计算第一行第一列的值（梯形法则）

    for n in range(1, n_max):  # 从第二行开始迭代
        h /= 2  # 步长减半
        sum_f = sum(f(a + (2*k - 1) * h) for k in range(1, 2**(n-1)))  # 计算当前行梯形法则的函数值之和

        R[n][0] = 0.5 * R[n-1][0] + h * sum_f  # 更新当前行第一列的值

        for m in range(1, n+1):  # 填充Romberg表格的其余部分
            if m == 1:
                R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1])  # 第二列使用不同的公式
            else:
                R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / ((4**(m-1)) - 1)  # 从第三列开始使用Romberg公式

        if abs(R[n][n] - R[n-1][n-1]) < tolerance:  # 检查是否满足精度要求
            return R[n][n]  # 如果满足，返回当前的近似积分值

    return R[n_max-1][n_max-1]  # 如果没有满足精度要求，返回最后一次迭代的结果


a, b = 0, 2
n_max = 10  # 最大迭代次数
tolerance = 1e-5  # 精度容差

integral_value = romberg_integration(f, a, b, n_max, tolerance) 
print(f"近似积分值为：{integral_value:.8f}")  