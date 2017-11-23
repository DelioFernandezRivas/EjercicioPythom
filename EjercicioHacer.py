import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class EjercicioHacer(Gtk.Window):
    def __init__(self):


        Caja1= Gtk.Box()
        self.add(Caja1)
        DatosBasicos=Gtk.Frame("Datos Basicos")
        self.add(DatosBasicos)

        Alineamiento = Gtk.Alignment()
        Label1 = Gtk.Label("Nombre")
        Label2 = Gtk.Label("Descripcion")

        Label4 = Gtk.Label("Foto")

        Entry1 = Gtk.Entry()
        Entry2= Gtk.Entry()

        Grind1= Gtk.Grid()

        Entry3 = Gtk.Entry()
        Button1 = Gtk.Button("Elegir")
        checkbutton1 =Gtk.CheckButton("Añadir Contador de visitas")

        DatosBasicos.add(Alineamiento,Label1,Label2,Entry1,Entry2,Grind1,checkbutton1)
        Grind1.add(Label4,Entry3,Button1)



        Caja3= Gtk.Box()
        Caja3.add(Label2)
        Caja3.add






        Marco2 = Gtk.Frame()
        self.add(Marco2)

        Caja1.add(DatosBasicos)
        Caja1.add(Marco2)


        Caja3

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
   EjercicioHacer()
   Gtk.main()
