import calculateDay, time

def getDays(curMo,curYe):
    monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    weekNames = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    rows = []
    firstDay = calculateDay.calc(1,curMo,curYe)
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
    lastDays = (lastMonthDays - firstDay[0]) + 1
    row1 = []
    for i in range(lastDays,lastMonthDays+1):
        row1.append((i,1))
    count = 1
    while len(row1) < 7:
        row1.append((count,0))
        count+=1
    rows.append(row1)

    #From the last day of row1, till the end of the current month....
    tempRow = []
    for i in range(row1[-1][0]+1, monthDays[curMo]+1):
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
        for i in range(rows[-1][-1][1]+1, 999):
            if len(tempRow) >= 7:
                rows.append(tempRow)
                break
            tempRow.append((i,1))

    return rows















