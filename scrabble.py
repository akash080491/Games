def scrabble_score(word):
    score={"a":1,"c":3,"b":3,"e":1,"d":2,"g":2,
           "f":4,"i":1,"h":4,"k":5,"j":8,"m":3,
           "l":1,"o":1,"n":1,"q":10,"p":3,"s":1,
           "r":1,"u":1,"t":1,"w":4,"v":4,"y":4,
           "x":8,"z":10}
    sum=0
    a=0
    for i in word:
        sum=sum+(score[i])
        
    return(sum)

point1=0
chance=5
counter =1
print("*********************Welcome to Scrabble*********************")
print("Rules\n\t 1) You have 5 chances. \n\t 2) To Win - You need to score 50.")
while(chance>0):
    word=input("Please enter the "+ str(counter) + "st word - ")
    point=scrabble_score(word)
    print("Your Score is", point)
    point1=point1+point
    print("Game Point is = ", point1)
    if(point1>=50):
        print("You Won")
        break
    counter=counter+1
    chance=chance-1

else:
        print("You Loose")

print("\n\t\t\t\t\t\tThanks for Playing")