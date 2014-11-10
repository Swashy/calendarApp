from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")
        self.set_default_size(250,120)

        self.grid = Gtk.Grid()
        self.add(self.grid)
#        self.grid.set_row_spacing(10)
#        self.grid.set_column_spacing(10)



        self.num = 5
        self.button1 = Gtk.Button(label=self.num)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.num = self.num **2

        self.button2 = Gtk.Button(label=self.num)
        self.button2.connect("clicked", self.on_button2_clicked)
        self.num = self.num **2

        self.grid.attach(self.button1,25,25,2,2)#C, R, W, H
        self.grid.attach(self.button2, 23, 25, 2, 2)


    def on_button1_clicked(self, widget):
        print("Button 1 clicked!!")
    
    def on_button2_clicked(self, widget):
        print("Button 2 clicked!!")

win = GridWindow()
label = Gtk.Label.new_with_mnemonic("HerpaDerp!")
win.grid.attach(label,50,50,2,1)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
