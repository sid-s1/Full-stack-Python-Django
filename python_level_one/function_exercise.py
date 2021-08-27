def array_check(nums):
    i=0
    while (i+2)<len(nums):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
        i=i+1
    return False

def string_splicing(str):
    print(str[::2])

def end_other(one,two):
    one=one.lower()
    two=two.lower()
    x=len(one)-1
    y=len(two)-1
    a=[]
    b=[]
    while x>=0:
        a.append(one[x])
        x=x-1
    while y>=0:
        b.append(two[y])
        y=y-1
    if(len(one)<len(two)):
        deft=len(one)
    else:
        deft=len(two)
    x=0
    c=0
    while x<deft:
        if(a[x]==b[x]):
            c=c+1
        x=x+1
    print (c==deft)

def doub_char(str):
    new_str=""
    for char in str:
        new_str=new_str+char+char
    print(new_str)

def check_teen(a):
    if(a==15 or a==16):
        return a
    elif (a>=13 and a<=19):
        return 0
    else:
        return a
def no_teen_sum(a,b,c):
    sum=0
    sum=sum+check_teen(a)+check_teen(b)+check_teen(c)
    print(sum)
no_teen_sum(2,15,1)
