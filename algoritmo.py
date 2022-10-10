import random

def trap(mi, Mi, md, Md, V):
    
    if V < mi:
        return 0

    if V > md:
        return 0

    if V > Mi and V < Md:
        return 1

    if V <= Mi and V >= mi:
        vI = abs(V-mi)/abs(Mi-mi)
        return vI
        

    if V >= Md and V <= md:
        vI = abs(V - md)/abs(Md-md)
        return vI



vel = random.randint(0,750)
print(vel)
while (True):
    if vel < 5:
        break

    prettySoft = trap(110, 130, 180, 150, vel) * 15
    strong = trap(0, 0, 50, 30, vel) * 50
    soft = trap(30, 50, 130, 110, vel) * 35
    mostSoft = trap(150, 180, 750, 750, vel) * 5

    breaking = mostSoft + prettySoft + soft + strong

    print("Breaking:")
    print(breaking)
    
    vel -= breaking
    print(vel)
