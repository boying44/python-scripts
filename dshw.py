# from thesaurus import Word

other = set(["group ticket",
"know age", "know cabin",
"title",
"fare class",
"deck",
"ethnicity",
])
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

    if s in age:
        age.remove(s)
        points["age"] += 1
    elif s in family:
        family.remove(s)
        points["family"] += 1
    elif s in other:
        other.remove(s)
        points["other"] +=1
    else:
        print("Nope")

    score = points["other"] + min(points["family"], 2) + min(points["age"], 3)
    print("Score:", score)



#if points > 5 give them flag

# toupdate = other
# newfeatures = set()
# for w in toupdate:
#     myWord = Word(w)
#     try:
#         for s in myWord.synonyms(relevance=3):
#             newfeatures.add(s)
#     except:
#         pass

# print(list(newfeatures))

# toupdate.update(newfeatures)
# print(list(toupdate))