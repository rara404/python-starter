import random
from datetime import datetime

def ex1():
    sum = 0;
    number = []
    for x in range(10):
        number.append(random.randint(0,100))
        sum += number[x]

    print(number)
    print('The sum is: ', sum)



def ex2():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    print("Volume is: ", (height*width*length))

def ex3():
    inputString = input('Enter list of numbers: ')
    list = inputString.split(',')
    if list[0] == list[-1]:
        print('True')
    else:
        print('False')


def ex4():
    sentence = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    sentenceList = sentence.split(' ')
    count = 0
    for words in sentenceList:
        if words == 'Python':
            count += 1

    print(count)


def ex5():
    myList = [1,2,3]
    mySet = {3,4,5}

    mySet.update(myList);
    print(mySet)



def ex6():
    myList = [11, 100, 101, 999, 1001]
    myList.reverse()

    print(myList)


def ex7():
    number = random.randint(1, 100)

    if number < 10:
        print(number, ': You Lose.')
    elif number < 50:
        print(number, ': Try Again.')
    else:
        print(number, ': You Win.')


def ex8():
    myList = [6,2,7,3,77,7,1]
    min = None

    for x in myList:
        if min == None or x < min:
            min = x

    print(min)

def ex9():

    myString = input('Enter String: ')

    if myString.isupper():
        print('True')
    else:
        print('False')





def ex10():
    myString = input('Enter String: ')
    vowel = 0
    const = 0

    for x in myString:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            vowel += 1
        else:
            const += 1

    print('Vowels: ', vowel)
    print('Consonants: ', const)

def ex11():
    todaysDate = datetime.today().strftime('%m/%d/%Y')
    f = open('output.txt', 'w')
    f.write(f"Todays date is: {todaysDate} .")
    f.close()
def ex12():
    userinput = input("Enter integer: ")
    if "." in userinput:
        print(f"ERROR: {userinput} is not an integer.")
    else:
        userinput =int(userinput)*(-1)
        print(userinput)

def ex13():
    while(True):
        num1 = input("Enter first integer: ")
        if num1 == 'exit':
            break
        num2 = input("Enter second integer: ")
        if num2 == 'exit':
            break
        print("Answer: ", (int(num1)+int(num2)))







if __name__ == '__main__':
     # ex1()
     # ex2()
     # ex3()
     # ex4()
     # ex5()
     # ex6()
     # ex7()
     # ex8()
     # ex9()
     # ex10()
     # ex11()
     # ex12()
     ex13()



