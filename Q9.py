score1 = input("Enter first exam score: ")
score2 = input("Enter second exam score: ")

score1 = int(score1)
score2 = int(score2)

if score1 >= 50 and score2 >= 50:
    print("You passed!")
else:
    print("You need to retake some exams")
