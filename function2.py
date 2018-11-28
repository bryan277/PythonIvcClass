
def load()->(str, int, int, int):
    name = input("Enter your name")
    num1 = int(input("Enter value 1 "))
    num2 = int(input("enter value 2 "))
    num3 = int(input("Enter value 3 "))
    return name, num1, num2, num3

def calc(num1:int, num2:int, num3:int)->(int, float):
    sum=num1+num2+num3
    avg=sum/3
    return sum,avg

def output(name:str, num1:int, num2:int, num3:int, sum:int, avg:float):
    print("Your name is", name)
    print("The numbers are", num1, num2, num3)
    print("The sum and average is", sum, avg)

def main():
    name, num1, num2, num3=load()
    sum, avg = calc(num1, num2, num3)
    output(name, num1, num2, num3, sum, avg)

if __name__=="__main__":
    main()
