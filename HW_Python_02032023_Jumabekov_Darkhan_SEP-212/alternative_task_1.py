import random

def gallows():
    words = ["программа", "макака", "прекрасный", "оладушек"]
    word = random.choice(words)
    answerList = []

    for element in word:
        answerList.append("_")

    remainingLetters = len(word)
    attempts = remainingLetters*2
    while remainingLetters > 0:
        if attempts < 1:
            break
        print(f'attempts = {attempts}')
        print(*answerList)
        guess = input("Угадайте букву: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Введите одиночную букву")
        else:
            attempts -= 1
            if not answerList.__contains__(guess):
                for i in range(len(word)):
                    if word[i] == guess:
                        answerList[i] = guess
                        remainingLetters -= 1
    print(*answerList)
    print(f"Отлично, было загадано слово {word}")