print("Welcome to The Quiz Game Of Computers!")
print("This game will be of 5 points and for each correct answer you will get 1 point")
print("No negative marking!!!")

print("Lets Begin!!!")

points = 0;

que1 = input("1.Full form of CPU : ")
if que1.lower() == 'central processing unit':
    print('Correct')
    points += 1
else:
    print("Wrong")

que2 = input("2.Mouse is an _______ to the computer : ")
if que2.lower() == 'input':
    print('Correct')
    points += 1
else:
    print("Wrong")
que3 = input("3.Monitor is an input device or output device? : ")
if que3.lower() == 'output device':
    print('Correct')
    points += 1
else:
    print("Wrong")
que4 = input("4.Full form of RAM : ")
if que4.lower() == 'random access memory':
    print('Correct')
    points += 1
else:
    print("Wrong")
que5 = input("5.What does hard drive do? : ")
if que5.lower() == 'store data':
    print('Correct')
    points += 1
else:
    print("Wrong")

print("Your Score = ",points)
print((points/5)*100,"% Scored")
if points >=2.5:
    print("Well done")
else:
    print("Not well")
