numbers = list(range(1, 101))

for fives in numbers:
    if fives % 5 + 1 == True:
        print("chicken")
    elif fives % 7 + 1 ==True:
        print("monkey")
    elif fives % 7 + 1 & fives % 5 + 1 == True:
        print("chickenmonkey")
    elif fives:
        print(fives)