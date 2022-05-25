import random

class Calculator():
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    
    def average(self):
        x = []
        for i in range(0, 25):
            num = random.randint(1, 30)
            x.append(num)
        return sum(x) / len(x)
        
    def isPrime(self, x):
        if x > 1:
            for i in range(2, int(x/2)+1):
                if (x % i) == 0:
                    print("It is not a prime number")
                    break
            else:
                print("It is a prime number")

        else:
            print("It is not a prime number")
    def cosign(self):
        pass


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(3, 5))
    print(calc.subtract(10, 9))
    print(calc.multiply(12, 4))
    print(calc.average())
    print(calc.isPrime(25))