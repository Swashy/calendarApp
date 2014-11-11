from gi.repository import Gtk, Gdk
import time
from calculateDayGaussian import calc
import genCalendar

class calendarWindow(Gtk.Window):
    def __init__(self):
        self.yearSub = 0
        self.monthSub = 0

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



#~~~~~~~Calendar Grid setup
        self.days = []
        self.calGrid = Gtk.Grid()
        self.calTitle = Gtk.Grid()
        self.month = Gtk.Label(self.monthNames[self.curMo]+str(self.curYe))
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

        self.dePopulateCalendar()
        if direction == 0:
            self.curMo -=1
        elif direction == 1:
            self.curMo +=1

        if self.curMo > 12:
            self.curYe +=1
            self.curMo -= 12

        if self.curMo < 1:
            self.curYe -=1
            self.curMo += 12
        
        #print(self.monthSub, self.yearSub)
        print("Current month is ",self.curMo+self.monthSub,"and year is",self.curYe-self.yearSub)
        daysOfMonth = genCalendar.getDays(self.curMo+self.monthSub,self.curYe-self.yearSub)
        self.populateCalendar(daysOfMonth)

        #Refresh Screen!
        self.show_all()

    def setupCalendar(self,curMo,curYe):
        curColumn = 0
        curRow = 0
        for i in range(42):
            if curColumn > 6:
                curColumn = 0
                curRow+=1
            self.days.append(Gtk.ListBox(vexpand=True,hexpand=True))
#            self.days[i].insert(Gtk.Label(),1)
            self.calGrid.attach(self.days[i],curColumn,curRow,1,1)
            curColumn +=1
        
        #After setting up our listboxes in the right spots of the
        #7 X 6 grid, call populate grid with the current month.
        daysOfMonth = genCalendar.getDays(self.curMo,self.curYe)
        self.populateCalendar(daysOfMonth)

    # Inserts calendar days into the listboxes of calGrid
    def populateCalendar(self,d):
        self.month.set_label(self.monthNames[self.curMo]+" "+str(self.curYe))
        count = 0
        for i in self.days:
            try:
                i.insert(Gtk.Label(d[count][0]),1)
            except:
                print("!!",count,"!!!","\n",len(d))
            count+=1
    def dePopulateCalendar(self):
        for i in self.days:
            for widget in i:
                i.remove(widget)

                
                    
def main():

    win = calendarWindow()
    win.populateGrid()
    win.setupCalendar(int(time.strftime('%m')),int(time.strftime('%Y')))

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
main()

