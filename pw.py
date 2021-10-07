import string
import random

master = string.ascii_letters + string.digits
boolchanger = int(input("Press 1 to enable punctuations, any other digit to disable: "))
length = int(input("Enter the length of your password: "))
list_length = int(input("Enter the amount of passwords you want: "))
use_punctuation = False
pw = ''
pw_list = []

if(boolchanger == 1):
    use_punctuation = True

if(use_punctuation):
    master += string.punctuation

for k in range(list_length):
    for i in range(length):
        pw += master[random.randint(0,len(master)-1)]
    pw_list.append(pw)
    pw = ''

print(pw_list)
