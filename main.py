

import random 

list = ["crazy","wonder","director","normal"]
marks = 0


while True:

  for word in list:
     scrabble_word = "".join(random.sample(word, k=len(word)))
     print(f"scrambled word: {scrabble_word}")
     answer = input("guess the word: ")


     if answer == word:
        print("correct!!")
        marks = marks + 5
       

     else:
       attempts = 2
       print("wrong answer :(")
       while attempts <= 3:
          answer = input(f"guess the word: attempts left {attempts}/3: ")
          if answer == word:
            marks = marks + 5
            print("good job! correct.")
            break
  
          elif answer != word:
            print("wrong answer :(")
            attempts = attempts + 1
        

       if attempts == 4:
         print("game end")
         break

  break
            

print("your total marks are: ", marks)

    
 

