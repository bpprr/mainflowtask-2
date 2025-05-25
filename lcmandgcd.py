a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD using Euclidean Algorithm
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

g = gcd(a, b)
lcm = abs(a * b) // g

print("GCD:", g)
print("LCM:", lcm)
