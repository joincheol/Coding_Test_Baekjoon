while(True):
    try:
        n = list(input())
        a, A, num, space = 0,0,0,0
        for i in range(len(n)):
            if(n[i]==" "):
                space += 1
            elif(n[i].islower()):
                a += 1
            elif(n[i].isupper()):
                A += 1
            elif(n[i].isdigit()):
                num += 1
        print(a, A, num, space)
    except EOFError:
        break