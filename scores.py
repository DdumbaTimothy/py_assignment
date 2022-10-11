st= None;
while st !="stop":
    score = float(input("Please enter your score:"))
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
    st = input("Enter stop to discontinue and any other value to continue.")