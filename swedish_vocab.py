import csv
import random

with open('english_to_swedish_test.csv', 'r', newline='', encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)[0:]
    print(headers[0].upper() + " ~ " + headers[1].upper())
    print('-' * 20)

    score = 0
    lives = 3

    for row in reader:
        engWord = row[0]
        swdWord = row[1]
        print("\n")
        guess = input("What is \"" + engWord + "\" in Swedish? ")

        if guess == swdWord:
            score += 1
            print("CORRECT!")
            print("SCORE: " + str(score))
            print("LIVES REMAINING: " + str(lives))
        else:
            lives -= 1
            if lives == 0:
                print("NOPE!")
                print("CORRECT ANSWER: " + row[1])
                print("SCORE: " + str(score))
                print("*** GAME OVER ***")
                break
            else:
                print("NOPE!")
                print("CORRECT ANSWER: " + row[1])
                print("SCORE: " + str(score))
                print("LIVES REMAINING: " + str(lives))

csvFile.close()