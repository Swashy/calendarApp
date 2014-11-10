from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)
        buttons = []
        self.set_default_size(300,200)
        for i in range(0,7):
            buttons.append(Gtk.Button("Button"))
            buttons[i].set_vexpand(True)
            buttons[i].set_hexpand(True)


#        button1 = Gtk.Button(label="Button 1")
#        button2 = Gtk.Button(label="Button 2")
#        button3 = Gtk.Button(label="Button 3")
#        button4 = Gtk.Button(label="Button 4")
#        button5 = Gtk.Button(label="Button 5")
#        button6 = Gtk.Button(label="Button 6")#

        grid.add(buttons[0])
        grid.attach(buttons[1], 1, 0, 2, 1)
        grid.attach_next_to(buttons[2], buttons[0], Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(buttons[3], buttons[2], Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(buttons[4], 1, 2, 1, 1)
        grid.attach_next_to(buttons[5], buttons[4], Gtk.PositionType.RIGHT, 1, 1)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
