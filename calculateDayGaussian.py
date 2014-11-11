import time
from math import floor

def leapyear(y):
    if (y % 4 == 0 and  y % 100 != 0) or (y % 400 == 0):
        return True
    else: return False

def calc(curDa,curMo,curYe):

    
    if curMo == 1 or curMo == 2:
        curYe = curYe - 1

    m = ((curMo + 9) % 12) + 1
    print("m is:",m)

    y = str(curYe)
    c = y[0:2]
    y = y[2:4]

    d = curDa

    m = float(m)
    y = float(y)
    c = float(c)
    d = float(d)

    w = (d + (floor((2.6*m)-0.2)) + y + (floor(y/4)) + (floor(c/4)) - (2*c))
    w = w%7
    return int(w), leapyear(curYe)
    

#For direct testing
if __name__ == "__main__":
    weekNames = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    monthNames=("NULL","January","February","March","April","May","June","July","August","September","October","November","December")

    w = calc(1,1,2015)[0]
    print("First day of",monthNames[1],2015, "is", weekNames[w])

    w = calc(1,2,2015)[0]
    print("First day of",monthNames[2],2015, "is", weekNames[w])
    #for i in range(1,13):
    #    w = calc(1,i,2014)[0]
    #    print("First day of",monthNames[i], "is", weekNames[w],w)

def derp():
    monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    weekNames = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
#    M = int(time.strftime('%m'))
#    Y = int(time.strftime('%Y'))
#    D = int(time.strftime('%d'))
    D = 10
    M = 11
    Y = 2014
    while True:
        if D >= monthDays[M]:
            if M == 12:
                print("Next Year!")
                Y = Y+1
                D = 1
                M = 1
            else:
                print("Next Month!")
                D = 1
                M +=1
        else:
            D +=1
        x = calc(D,M,Y)
        x = int(x[0])
#        if x == 6:
#            x = 0
#        else:
#            x = x+1
        print(weekNames[x],x," ",D,M,Y)
        time.sleep(1)
