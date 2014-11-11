# w = d + m + c + y, mod 7


def leapyear(y):
    if (y % 4 == 0 and  y % 100 != 0) or (y % 400 == 0):
        return True
    else: return False
# 1/2/2014
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Kraitchik.27s_algorithm
def calc(day,month,year):
    #Month
    mVar = ["NULL",(1,1),(2,4),(3,3),(4,6),(5,1),(6,4),(7,6),
            (8,2),(9,5),(10,0),(11,3),(12,5)]
    m = mVar[month][1]

    loop = True
    twodigyear = year
    while loop == True:
        if twodigyear<100:
            loop = False
        else:
            twodigyear = twodigyear-100
    
    #century = year - twodigyear
    stringyear = str(year)
    century = int(stringyear[0:2])


    cVar = [(0,0),(1,5),(2,3),(3,1)]
    
    c = (century//100)%4
    c = cVar[c][1]

    yVar={0:[0,6,17,23,28,34,45,51,56,62,73,79,84,90],
          1:[1,7,12,18,29,35,40,46,57,63,68,74,85,91,96],
          2:[2,13,19,24,30,41,47,52,58,69,75,80,86,97],
          3:[3,8,14,25,31,36,42,53,59,64,70,81,87,92,98],
          4:[9,15,20,26,37,43,48,54,65,71,76,82,93,99],
          5:[4,10,21,27,32,38,49,55,60,66,77,83,88,94],
          6:[5,11,16,22,33,39,44,50,61,67,72,78,89,95]}


    for i in yVar.keys():
        if twodigyear in yVar[i]:
            y = i
    # 3
    print(day, m, c, y)
    dayOfWeek = (day + m + c + y) % 7

    #Compensate for Kraitchicks strange algorithm where the 0 = Saturday
    #and 6 is Friday.
#                      0     1     2     3     4     5     6
# kraitchicknames = ("Sat","Sun","Mon","Tue","Wed","Thu","Fri")
# mynames         = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    print("before",dayOfWeek)
    if dayOfWeek == 0:
        dayOfWeek = 6
    else:
        dayOfWeek = dayOfWeek-1
    print("after",dayOfWeek)

    return dayOfWeek, leapyear(year)

if __name__ == "__main__":
    names = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    anum = ""
    while True:
        anum = ""
        date = []
        inp = input("Enter a date. (Format d/m/y): ")
        if inp[0] == 'q':
            break
        for i in inp:
            if i == "/":
                date.append(int(anum))
                anum = ""
            else:
                anum = anum + i
        date.append(int(anum))
        print(date)
        dayOfWeek = calc(date[0],date[1],date[2])
        print(dayOfWeek,names[dayOfWeek[0]],"\n")
