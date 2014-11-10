from gi.repository import Gtk, Gdk
import time
import calculateDay

class calenderWindow(Gtk.Window):
    def __init__(self):
        self.curDa = int(time.strftime('%d'))
        self.curMo = int(time.strftime('%m'))
        self.curYe = int(time.strftime('%Y'))
        Gtk.Window.__init__(self, title="Work Calendar V.0.1")

        self.monthNames=("NULL","January","February","March","April","May","June","July","August","September","October","November","December")
        self.names = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")

#~~~~~~~Window setup
        self.set_default_size(448,302)
        self.set_gravity(3)

#~~~~~~~Master grid setup
        self.masterGrid = Gtk.Grid()

#~~~~~~~Text View and editor
        self.dayEditor = Gtk.TextView()



#~~~~~~~Calender Grid setup
        self.days = []
        self.calGrid = Gtk.Grid()
        self.calTitle = Gtk.Grid()
        self.month = Gtk.Label(self.monthNames[self.curMo])
        self.calendarLeft = Gtk.Button.new_from_icon_name("go-next-rtl",1)
        self.calendarRight = Gtk.Button.new_from_icon_name("go-next",1)

#~~~~~~~Connect to Callbacks!
        self.button1 = Gtk.Button("Print Dimensions")
        self.button1.connect("clicked", self.printDimensions)
        self.calendarLeft.connect("clicked", self.calendarMove,0)
        self.calendarRight.connect("clicked", self.calendarMove,1)

    def populateGrid(self):
     #attach params are (Widget, Left of Column, Top of Row, W, H)
        self.add(self.masterGrid)
        self.masterGrid.attach(self.calGrid,1,1,1,1)
        self.masterGrid.attach(self.button1,0,1,1,1)
        self.masterGrid.attach(self.dayEditor,0,2,1,1)
        self.masterGrid.attach(self.calTitle,1,0,1,1)
        self.calTitle.attach(self.month,0,0,5,1)
        self.calTitle.attach_next_to(self.calendarLeft,self.month,Gtk.PositionType.LEFT,1,1)
        self.calTitle.attach_next_to(self.calendarRight,self.month,Gtk.PositionType.RIGHT,1,1)


        self.calTitle.attach_next_to(Gtk.Label(self.names[0],hexpand=True),self.calendarLeft,Gtk.PositionType.BOTTOM,1,1)
        for i in range(1,7):
            self.calTitle.attach(Gtk.Label(self.names[i],hexpand=True),i,1,1,1)

    def printDimensions(self, button):
        dim = self.get_size()
        print(dim)
        Gtk.main_quit()

    def calendarMove(self, button, direction):
        for i in reversed(range(1,len(self.days)+1)):
            self.days[i-1].destroy()
            self.days.pop(i-1)
        if direction == 0:
            self.curMo = self.curMo-1
            self.setupCalendar(self.curMo, self.curYe)
        else:
            self.curMo = self.curMo+1
            self.setupCalendar(self.curMo, self.curYe)
        self.month.set_label(self.monthNames[self.curMo])
        self.show_all()

    def setupCalendar(self,curMo,curYe):
        print(curMo,curYe)
#        def makeDay(number,arrayCount,count):    

        self.days = []
        monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        names = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")

        dayOfWeek,leap = calculateDay.calc(1,curMo,curYe)
        print("First day of this month is",names[dayOfWeek])

        if leap == True:
            monthdays[1] = 29
        arrayCount = 0
        count = 1
        firstWeek = True
        nextCount = 1
        # For loop for each week. Dispay 6 weeks in the calendar.
        for i in range(0,6):
            curCol = 0
            #On the first week,
            if firstWeek == True:
                #Get amount of days to display. If the weekday is 3(Wednesday)
                #then we have three previous days to display.
                lastmonth = monthDays[curMo-1] #get last month days
                #Say we have October(31), minus 3(Wednesday) would be 27.
                #So for range 28, 29, 30, append the days
                for l in range( (lastmonth-dayOfWeek+1) ,lastmonth+1):
                    self.days.append(Gtk.ListBox.new())
                    self.days[arrayCount].set_vexpand(True)
                    self.days[arrayCount].set_hexpand(True)
                    day = Gtk.Label(l)
                    day.override_color(0,Gdk.RGBA(red=1,green=1,blue=1,alpha=0.2))
                    self.days[arrayCount].insert(day,1)
                    #self.days[arrayCount].insert(Gtk.Label(names[curCol]),1)
                                         #widget,left of column, top of row
                    self.calGrid.attach(self.days[arrayCount],curCol,i,1,1)
                    arrayCount+=1
                    curCol +=1
                #For the rest of the days,
                for j in range(dayOfWeek, 7):
                    self.days.append(Gtk.ListBox.new())
                    self.days[arrayCount].set_vexpand(True)
                    self.days[arrayCount].set_hexpand(True)
                    self.days[arrayCount].insert(Gtk.Label(count),1)
                    #self.days[arrayCount].insert(Gtk.Label(names[curCol]),1)
                    self.calGrid.attach(self.days[arrayCount],curCol,i,1,1)
                    arrayCount+=1
                    #Keep track of what day we're on.
                    count+=1
                    curCol +=1
                firstWeek = False

            # If we've finished the first sloppy week, do the middle ones!
            elif firstWeek == False and count < monthDays[curMo]:
                for l in range(0,7):
                    # If we've reached the end of the month, get out of here!
                    if count > monthDays[curMo]:
                        continue
                    self.days.append(Gtk.ListBox.new())
                    self.days[arrayCount].set_vexpand(True)
                    self.days[arrayCount].set_hexpand(True)
                    self.days[arrayCount].insert(Gtk.Label(count),1)
                    #self.days[arrayCount].insert(Gtk.Label(names[curCol]),1)
                    self.calGrid.attach(self.days[arrayCount],curCol,i,1,1)
                    arrayCount+=1
                    #Keep track of what day we're on.
                    count+=1
                    curCol +=1
            # Doing the last week from where we left off.
            if count >= monthDays[curMo]:
                for l in range(curCol,7):
                    self.days.append(Gtk.ListBox.new())
                    day = Gtk.Label(nextCount)
                    self.days[arrayCount].set_vexpand(True)
                    self.days[arrayCount].set_hexpand(True)
                    day.override_color(0,Gdk.RGBA(red=1,green=1,blue=1,alpha=0.2))
                    self.days[arrayCount].insert(day,1)
                    #self.days[arrayCount].insert(Gtk.Label(names[curCol]),1)
                    self.calGrid.attach(self.days[arrayCount],curCol,i,1,1)
                    arrayCount+=1
                    #Keep track of what day we're on.
                    nextCount +=1
                    curCol +=1
                
                
                    
def main():

    win = calenderWindow()
    win.populateGrid()
    win.setupCalendar(int(time.strftime('%m')),int(time.strftime('%Y')))

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
main()

