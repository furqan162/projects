
first = input("First= ")
second = input("Second= ")
operator = input("operator=  ")
if operator == "+":
    print(int(first) + int(second))
elif operator == "-":
    print(int(first)-int(second))
elif operator == "*":
    print(int(first)*float(second))
elif operator == "/":
    print(int(first)/int(second))
elif operator == "//":
    print(int(first)//int(second))
elif operator == "%":
    print(int(first)%int(second))
else:
    print("wrong operator")
