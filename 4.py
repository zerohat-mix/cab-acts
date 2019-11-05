"""Необходимо написать рекурсивный алгоритм для нахождения НОД
и НОК двух чисел. Два числа вводятся вручную во время
выполнения программы."""


n = int(input('Введите первое число = '))
m = int(input('Введите второе число = '))

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def mcd(n,m):
    return (n/gcd(n,m))*m

print("НОД = ", gcd(n, m))
print("НОК = ", mcd(n, m))
