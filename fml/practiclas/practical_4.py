#!/usr/bin/env python3
import sys
selector = ""
gender = int(input("\nSelect Gender:\n  1. Male\n  2. Female\n\nYour Input: "))
if gender not in [1,2]:
    print("you entered wrong number retry ")
    sys.exit()
else:
    if gender == 1 :
        selector += "m"
    elif gender == 2 :
        selector += "f"
age = int(input("\nenter your age :"))
if age >= 10 and age <= 15 :
    selector += "1"
elif age >= 16 and age <= 20 :
    selector += "2"
elif age >= 21 and age <= 25 :
    selector += "3"
else:
    print("\nSorry you age is out of our current dataset range")
    sys.exit()
group = {
    "m1" : "apple",
    "f1" : "banana",
    "m2" : "orange",
    "f2":"mango",
    "m3": "banana",
    "f3" : "mango",
}
print(f"\nYour favorite fruit might be: {group[selector]}")


