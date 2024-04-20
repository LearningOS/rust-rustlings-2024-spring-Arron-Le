import numpy as np

def f(x):
  """被积函数"""
  return np.sqrt(x - 3 * x**2 + 2 * x**3 + np.exp(x))

def composite_trapezoidal(f, a, b, n):
  """复合梯形算法"""
  h = (b - a) / n
  x = np.linspace(a, b, n + 1)
  y = f(x)
  integral = h * (y[0] + y[-1]) / 2 + h * np.sum(y[1:-1])
  return integral

def main():
  """主函数"""
  a = 0
  b = 2
  tol = 1e-5
  n = 2
  integral_old = composite_trapezoidal(f, a, b, n)

  while True:
    n *= 2
    integral_new = composite_trapezoidal(f, a, b, n)
    if abs(integral_new - integral_old) < tol:
      break
    integral_old = integral_new

  print(f"迭代步数: {np.log2(n)}")
  print(f"最终步长: {h}")
  print(f"积分值: {integral_new}")

if __name__ == "__main__":
  main()