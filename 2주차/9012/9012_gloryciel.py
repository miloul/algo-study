T = int(input())

while(T>0):
    T -= 1
    yes =True
    stack=[]
    string = input()
    for i in range(0,len(string)):
        if(string[i]=='('):
            stack.append('(')
        else:
            if(len(stack)==0):
                print("NO")
                yes = False
                break

            else:
                del stack[-1]

    if(yes):
        if(len(stack)==0):
            print("YES")
        else:
            print("NO")
