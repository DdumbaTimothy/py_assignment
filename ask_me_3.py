name=input("What is your name please")
print(f"Hello {name}, how are you?")

if name=="Jack"or name=="Jackie":
    print(f"Hello {name}")
    print(f"Goodbye {name}")
else:
    print("Hello friend!")
    age=int(input("How old are you?"))
if age < 18:
    print("you are below the working age.")
elif age >18 and age <25:
    print("you are of age to look for a job.")
elif age >=25 and age <30:
    print("you should be having a job.")
elif age >30 and age <60:
    print("you should think of having a family.")
elif age <90 and age >=60:
    print("you should retire.")
else:
    print(f"Goodbye {name}.")
    print(f"You are {age} years ols.")
    print(f"You are an alien in nature.")