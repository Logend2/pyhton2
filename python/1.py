
import random
 
def a():
    fl = []
    fl1 = []
    file = open('-3.txt')
    i = 0
    for line in file:
        i += 1
        if i > 100:
            i = 0
            break
        
        fl.append(line)
        
    file.close()
    
    while i < 233:
        a = random.randint(0,len(fl))
        f = open("--3.txt","a+")
        if a < len(fl):
            if fl[a] not in fl1:
                print(fl[a])
                f.write(fl[a])
                fl1.append(fl[a])
                f.close()
        if i > 233:
            break
    f.close()
a()
