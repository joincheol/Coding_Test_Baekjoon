call = input()
time = 0

for i in range(len(call)):
    if(call[i] in "ABC"):
        time += 3
    elif(call[i] in "DEF"):
        time += 4
    elif(call[i] in "GHI"):
        time += 5
    elif(call[i] in "JKL"):
        time += 6
    elif(call[i] in "MNO"):
        time += 7
    elif(call[i] in "PQRS"):
        time += 8
    elif(call[i] in "TUV"):
        time += 9
    elif(call[i] in "WXYZ"):
        time += 10

print(time)