import sys
import random

def getAns(AnsNum):
    if AnsNum ==1:
        return 'It is certain'
    elif AnsNum == 2:
        return 'It is Decidedly so'
    elif AnsNum == 3:
        return 'Yes'
    elif AnsNum == 4:
        return 'Reply hazy try again'
    elif AnsNum == 5:
        return 'Ask again later'
    elif AnsNum == 6:
        return 'Concentrate and ask again'
    elif AnsNum == 7:
        return 'My reply is no'
    elif AnsNum == 8:
        return 'Outlook not so good'
    elif AnsNum == 9:
        return 'Very doubtful'
    
r = random.randint(1,9) //It evaluates to a random integer between 1 and 9 (including 1 and 9 themselves), and this value is stored in a variable named r.
fortune = getAns(r) //Program execution moves to GetAns function
print(fortune)
