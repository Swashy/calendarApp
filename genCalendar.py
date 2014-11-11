#!/usr/bin/python3

import time
import calculateDays

def getDays(curMo,curYe):
    monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    weekNames = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    rows = []
    firstDay, leap = calculateDays.calcWeekDay(1,curMo,curYe)
    if leap == True:
        monthDays[2] = 29
    else:
        monthDays[2] = 28
    if curMo == 1:
        lastMonthDays = monthDays[12]
        nextMonthDays = monthDays[curMo+1]
    elif curMo == 12:
        lastMonthDays = monthDays[curMo-1]
        nextMonthDays = monthDays[1]
    else:
        lastMonthDays = monthDays[curMo-1]
        nextMonthDays = monthDays[curMo+1]
    
    '''
    Get the first week. Calculate the previous month's days to display by
    subtracting the "number" of the first weekday (e.g. sun=0, mon=1)
    from last month's days.
    So if we had month days of 31, and the first weekday was "6", we would get
    25, which is incorrect so we add 1 to get 26.
    Thus, the first week would look like this:

    26, 27, 28, 29, 30 ,31, 1

    Returned from this function are lists of tuples, where [0] element is the
    day number, and [1] is whether that day is the current month(0), or the last
    month (1) so we can color them accordingly.

    NOTE TO SELF:
    '''
    lastDays = (lastMonthDays - firstDay) + 1
    row1 = []
    # Edge-case, if the last day is sunday, then getting the amount of
    #days to add from the last month won't work.
    if firstDay == 0:
        for i in range(lastMonthDays-6,lastMonthDays+1):
            row1.append((i,1))
        rows.append(row1)
    else:
        for i in range(lastDays,lastMonthDays+1):
            row1.append((i,1))
        count = 1
        while len(row1) < 7:
            row1.append((count,0))
            count+=1
        rows.append(row1)

    #From the last day of row1, till the end of the current month....
    tempRow = []
    last = row1[-1][0]+1
    #If the last day of the last row was not the start of our month,
    #that is to say the whole first week was last month, set it to 1
    if row1[-1][0]+1 > 7:
        last = 1
    for i in range(last, monthDays[curMo]+1):
        if len(tempRow) == 7:
            rows.append(tempRow)
            tempRow = []
        tempRow.append((i,0))
    
    #Finally, get the last week(s) If our last week is under 7 days, it rolls
    #over to here.
    count = 1
    while len(tempRow) < 7:
        tempRow.append((count,1))
        count +=1
    rows.append(tempRow)
    tempRow = []

    # Are we missing a sixth week?
    if len(rows) < 6:
        # From the last day of the last week in rows, till whenever
        # we have 7 days....
        # First number in our range is crazy because I have slice an element
        # out of a tuple in a list, which is in a list... haha.
        for i in range(rows[-1][-1][0]+1, 999):
            if len(tempRow) >= 7:
                rows.append(tempRow)
                break
            tempRow.append((i,1))

    sequentialRows = []
    for i in rows:
        for l in i:
            sequentialRows.append(l)

    return sequentialRows

if __name__ == "__main__":
    x = getDays(11,2013)
    print(x)
    firstDay, leap = calculateDays.calcWeekDay(1,2,2014)
    print("First day is", firstDay)














