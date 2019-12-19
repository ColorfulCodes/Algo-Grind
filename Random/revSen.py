def revSentence(x):
    x= x.split()
    punc = ".!?;"
    front = 0
    end = len(x)-1
    while front < end:
        fp=""
        ep=""
        if x[front][-1] in punc:
               fp =x[front][-1]
               x[front]= x[front][:-1]
        elif x[end][-1] in punc: 
            ep =x[end][-1]
            x[end]= x[end][:-1]
        temp = x[front] + ep
        x[front] = x[end]+ fp
        x[end] = temp
        front+= 1
        end-= 1
    return ' '.join(x)

print(revSentence("I like eggs. And  Ice cream!"))