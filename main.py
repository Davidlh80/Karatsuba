def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    num1 = str(x)
    num2 = str(y)
    n = max(len(num1), len(num2))
    half = n // 2

    a = x // 10**half
    b = x % 10**half
    c = y // 10**half
    d = y % 10**half

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    result = ac * 10**(2*half) + (ad_bc * 10**half) + bd

    return result

def main():
    x = int(input("Valor x: "))
    y = int(input("Valor y: "))
    
    print(f"Multiplicando {x} por {y}: {karatsuba(x, y)}")

main()