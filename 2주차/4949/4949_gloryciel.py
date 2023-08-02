while(True):
    stack=[]
    now = input()
    flag = True
    if(now =='.'):
        break
    for i in range(0,len(now)):
        if(now[i]=='('):
            stack.append('(')

        if(now[i]=='['):
            stack.append('[')

        if(now[i]==')'):
            if(len(stack)!=0 and stack[-1]=='('):
                del stack[-1]
            else:
                print("no")
                break

        if(now[i]==']'):
            if(len(stack)!=0 and stack[-1]=='['):
                del stack[-1]
            else:
                print("no")
                break

        if(len(stack)==0 and i == len(now)-2):
            print("yes")

        elif(len(stack)!=0 and i== len(now)-2):
            print("no")
