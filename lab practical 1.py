#Corey Pierce
#Practical 1

#Section 2

file_contents = [line.strip().split(" ,") for line in open("passwords.txt", "r")] #I have no idea why my stip and Splits arent working

#Section 3
print("The current possible passwords are:\n", "-" *15)
print(file_contents)
print("( 25 possible)")
def possible_pass():

    while True:

        for line in file_contents[24]:
            print(" ".join(file_contents))
            print
            
#Since my strip and split didnt seem to work I tried using .join
        break

    return possible_pass()
        
#I used break to stop the file contents from printing

#section 4


#clue 1
print("Clue 1: The password is at least 6 characters long.\n")
print("The current possible passwords are:\n", "-" * 15)
clue1 = [i[0] for i in file_contents if len(i) >= 6]
print(clue1)
print("(21 possible)")

print()

#clue 2    
print("Clue 2: The password contains at least one letter.\n")
print("The current possible passwords are:\n", "-" * 15)
clue2 = [i for i in clue1 if len([let for let in i if let.isalpha()]) >= 1]
print(clue2)
print("(15 possible)")
   
print()

#clue 3
print("Clue 3: The password starts with a consonant and the third letter is a vowel.\n")
print("The current possible passwords are:\n", "-" * 15)
vowel = ["a","e","i","o","u"]
consonant = ["q","w","r","t","y","p","s","d","f","g",
              "h","j","k","l","z","x","c","v","b","n","m"]
clue3 = [i for i in clue2 if len([let for let in i if let[0]
                                                 in consonant and let[2]  in vowel])]
print(clue3)

print()
#clue 4 
print("Clue 4: The password has no more than half as many vowels as it does consonants.\n")
print("The current possible passwords are:\n", "-" * 15)
clue4 = [i for i in clue3 if len([let for let in i if let in consonant]) >= 2 *
         len([let for let in i if let in consonant])]

print(clue4)                                              
#BONUS - Section 5

print()

print("Bonus: The password has the same letter twice in a row.\n")
print("Password found!\n", "-" * 15)
clue5 = [i for i in clue4 if len([let for let in i if let[i] == let[i]])]
print(clue5)

print(possible_pass())
   

#I think my Clues are good but I could not find out how to place them in the list
        


