print("Think a number from 1 to 1000 and I'll guess it in max. 10 tries.")
print("Press Enter")


def guess_num():                                              # get the answer from user
    possible_answer = ["too small", "too big", "you won"]
    while True:
         answer = input("""Chose one of the options below:    
- too small,
- too big, 
- you won
""").lower()
         if answer in possible_answer:                         # check if the answer is correct
            break
         else:
             print("Wrong answer")
    return answer


def check():
    min_num = 0
    max_num = 1000
    input()
    answer = ""
    i = 1
    while answer != "you won":                                   # loop to check answers
        if i <= 10:                                              # checking if user is not cheating
            guess = int((max_num - min_num) / 2) + min_num
            print(f"Zgaduję: {guess}")
            answer = guess_num()
            i = i + 1
            if answer == "too big":
                max_num = guess
            elif answer == "too small":
                min_num = guess
            else:
                 print("You Won!")
        else:
            print("Don't cheat")
            break


check()


