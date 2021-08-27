import random,time

def paus():
    for i in range(0,3):
        time.sleep(1)
        print(".\n",end='',flush=True)

def comp(one,two):
    li=[]
    for digit in one:
        x=-1
        for dig in two:
            x=x+1
            if dig == digit:
                # t=two.index(dig)
                # li.append(t)
                li.append(x)
                break
    y=len(li)
    if y==3:
        if li[0]==0 and li[1]==1 and li[2]==2:
            return "nice! spot-on!"
        else:
            return "nice, but numbers are jumbled up"
    elif y==2:
        if (li[0]==0 and li[1]==1):
            return "nice! got two digits right in the correct order"
        elif (li[0]==1 and li[1]==2):
            return "nice! got two digits right in the correct order"
        else:
            return "got two right, but not in the correct order"
    elif y==1:
        return "got one of them right"
    else:
        return "failed"

#i=random.randint(100,999)
i=345
print("---Welcome to the number guessing game!---\n",end='',flush=True)
paus()
print("---I have thought of a number already---\n",end='',flush=True)
paus()
print("Can you guess what it is???\n",end='',flush=True)
paus()
i=str(i)
user_input=input("Enter here...\n")
user_input=str(user_input)
z=comp(i,user_input)
print (z)
while True:
    if z != "nice! spot-on!":
        try_again=input("\nWant to try again? - enter Y/N\n")
        if try_again=="Y":
            user_again_inputs=input("Enter here...\n")
            user_again_inputs=str(user_again_inputs)
            z=comp(i,user_again_inputs)
            print(z)
        else:
            break
    else:
        break
