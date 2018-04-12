#!/usr/bin/env python3
from difflib import get_close_matches

flag = os.environ.get("FLAG")

other = set(["group ticket", "know age", "know cabin", "title", "fare class","deck","ethnicity",])
family = set(["family size", "number of family members", "alone", "small family", "large family", "group"])
age = set(['aged', 'teenager', 'youngster', 'minor', 'offspring', 'kid', 'youth', 'juvenile', 'midlife', 'ancient', 'middle-age', 'adult', 'middle age', 'elderly', 'adolescent', 'old', 'child', 'young'])

points = {
    "other": 0,
    "family": 0,
    "age": 0,
}

#get inputs
score = 0
while score < 6:
    s = input("Enter feature: ")

    inAge = get_close_matches(s, age, cutoff=0.8)
    inFamily = get_close_matches(s, family, cutoff=0.8)
    inOther = get_close_matches(s, other, cutoff=0.8)

    if len(inAge):
        for e in inAge:
            age.remove(e)
        points["age"] += 1
    elif len(inFamily):
        for e in inFamily:
            family.remove(e)
        points["family"] += 1
    elif len(inOther):
        for e in inFamily:
            other.remove(e)
        points["other"] +=1
    else:
        print("Nope")

    score = points["other"] + min(points["family"], 2) + min(points["age"], 3)
    print("Age:", min(points["age"], 3))
    print("Other:", points["other"])
    print("Family:", min(points["family"], 2))
    print("Total Score:", score)
    print("-----------")

print(flag)