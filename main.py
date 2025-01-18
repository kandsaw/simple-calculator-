import art


def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def dev(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":dev
}

# print(operations["*"](4,8))
# #
def calculater():
    print(art.logo)
    should_accumulate =True
    f_num=float(input("can you please inter the first number:\n"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator=input("can you please neter the operator you want to performe :\n")
        l_num=float(input("can you enter the second number:\n"))

        result=operations[operator](int(f_num),int(l_num))
        print(f"the result of {f_num} {operator} { l_num} is: {result} ")

        user_want=input("do you want to continue working with the previous result?\n")
        user_wants=user_want.lower()
        if user_wants=="yes":
            f_num = result

        else:
            should_accumulate = False
            print("\n"*100)
            calculater()

calculater()



















