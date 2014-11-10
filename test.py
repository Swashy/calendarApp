from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button1.set_hexpand(True)
        button1.set_vexpand(True)
        button2 = Gtk.Button(label="Button 2")
        button2.set_hexpand(True)
        button2.set_vexpand(True)
        button3 = Gtk.Button(label="Button 3")
        button3.set_hexpand(True)
        button3.set_vexpand(True)
        button4 = Gtk.Button(label="Button 4")
        button4.set_hexpand(True)
        button4.set_vexpand(True)
        button5 = Gtk.Button(label="Button 5")
        button5.set_hexpand(True)
        button5.set_vexpand(True)
        button6 = Gtk.Button(label="Button 6")
        button6.set_hexpand(True)
        button6.set_vexpand(True)

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
