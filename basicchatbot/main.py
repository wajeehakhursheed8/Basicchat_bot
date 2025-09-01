import random as rd

#greeting function

def greeting():
    mylist1=['Hi','Hello','Hey There!']
    gout=rd.choice(mylist1)
    print(gout)

def seeoff():
    mylist2=['Bye','GoodBye!','SeeYou!']
    seeout=rd.choice(mylist2)
    print(seeout)

def talk():
    mylist3=['I am fine, Thankyou!','I am Good, Thankyou!','I am doing great, Thankyou!']
    talkout=rd.choice(mylist3)
    print(talkout)

print("WELCOME TO BASIC CHATBOT! ")
user_in=input().lower().strip() #this will take initial/first input eg hi 

while True:
    if user_in == '':
        print('Sorry! plz type something!')
    if user_in in  ('hello','hello!','hi'):
        greeting()
    elif user_in in ('how are you','how are you?','are you okey?'):
        talk()
    elif user_in in ('bye','goodbye!','goodbye','byebye'):
        seeoff()
        break
    else:
        print("Sorry! i dont understand, please try :'hi', 'how are you' or 'bye' Thankyou!")
        
    
    user_in=input("What would you like to say something?").lower().strip() #this will take next input 
    
    






