a, b, c = map(int, input().split())

def Sum(num1, num2):
    if num2 == 1:
        return num1 % c
    value = Sum(num1, num2//2)
    if num2 % 2 ==0:
        return (value*value)%c
    else:
        return (value*value*num1)%c
print(Sum(a, b))