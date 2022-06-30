''' изменения в программе:
1) добавленны дополнительные две попытки, за счет увелечения количества моделек повешенного'''
import random
HANGMAN_PICS = ['''
    +===+
        |
        |
        |
       ===''','''
    +===+
    0   |
        |
        |
       ===''','''
    +===+
    0   |
    |   |
        |
       ===''','''
    +===+
    0   |
   /|   |
        |
       ===''','''
    +===+
    0   |
   /|\  |
        |
       ===''','''
    +===+
    0   |
   /|\  |
   /    |
       ===''','''
    +===+
    0   |
   /|\  |
   / \  |
       ===''','''
    +===+
   [0   |
   /|\  |
   / \  |
       ===''','''
    +===+
   [0]  |
   /|\  |
   / \  |
       ==='''] 
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра глубь гусь жаба зебра змея 
индюк кит кобра коза козел койот корова кролик крыса курица лама ласка лебедь лис лиса лосось лось лягушка
медведь моллюск моль мул муравей мышь норка обезьяна овца окунь олень орел панда паук питон 
попугай пума семга скунс собака сова тигр тритон утка форель хорек черепаха ястреб ящерица'''.split()

def getRandomWord(wordList):
    # эта ф-ия возращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_'*len(secretWord)
    
    for i in range(len(secretWord)): #заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
                
    for letter in blanks: #Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()
    
def getGuess(alreadyGuessed):
    # Возращает букву, введенную игроком. Это ф-ия проверяет, что игрок ввел только одну букву и больше ничего
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print ('Пожайлуста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожайлуста, введите БУКВУ')
        else:
            return guess

def playAgain():
    # эта ф-ия возращает значение True, если хочет сыграть в противном случае возращает False.
    print ('Хотите сыграть ещё? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters =''
correctLetters =''
secretWord = getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    
    #позволяет игроку ввести букву
    guess=getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters=correctLetters + guess       
        #проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - " ' + secretWord + '"! Вы угадали')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Проверяет, первысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' +
                  str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) +
                  '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True
            # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters =''
            correctLetters =''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        
        

