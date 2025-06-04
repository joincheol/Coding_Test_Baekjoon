while(True):
    n = int(input())
    word = []
    if(n == 0):
        break
    for i in range(n):
        word.append(input())
    word.sort(key=str.lower)
    print(word[0])