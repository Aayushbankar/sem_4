selector = ""

gender = int(input("enter your gender  \n 1 for male  \n 2 for female \n your input : "))

if gender not in [1,2]:
    print("you entered wrong number retry ")
else:
    if gender == 1 :
        gender = "m" 
        selector += gender
    elif gender == 2 :
        gender = "f"
        selector += gender

age = int(input("enter your age :"))
if age >= 10 and age <= 15 :
    selector += "1"
if age >= 16 and age <= 20 :
    selector += "2"
if age >= 21 and age <= 25 :
    selector += "3"


group = {
    "m1" : "apple",
    "f1" : "banana",
    "m2" : "orange",
    "f2":"mango ",
    "m3": "banana",
    "f3" : "mango"
}


print(f"your favourite fruit might be : {group[selector]}")