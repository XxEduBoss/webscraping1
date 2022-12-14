from datos_bbdd import *
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp






def mostrar_datos_tabla(tabla):


    # Cargar los datos
    lista_perros = consultar_datos()

    for perro in lista_perros:

        tabla.row_data.append(perro)



def cargar_formulario(panel3):

    panel3.clear_widgets()

    formulario = GridLayout(cols=1, rows=4, padding=30, spacing=30)

    input_nombre = MDTextField(hint_text="Nombre", mode="round", max_text_length=100, helper_text="Ingrese el nombre del pienso")

    input_precio = MDTextField(hint_text="Precio", mode="round", max_text_length=6, helper_text="Ingrese el precio del pienso")

    input_marca = MDTextField(hint_text="Marca", mode="round", max_text_length=100, helper_text="Ingrese la marca del pienso")

    formulario.add_widget(input_nombre)
    formulario.add_widget(input_precio)
    formulario.add_widget(input_marca)
    panel3.add_widget(formulario)



def guardar_en_bbdd(formulario):

    nuevo_pienso = dict()

    nuevo_pienso["nombre"] = formulario.children[0].children[2].text
    nuevo_pienso["precio"] = formulario.children[0].children[1].text
    nuevo_pienso["marca"] = formulario.children[0].children[0].text


    #Llamar al método -> insertar (nuevo_pienso)
    insertar_dato_nuevo(nuevo_pienso)



def insertar_dato_nuevo( nuevo_pienso):



    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="transfermarkt",
                            user="root",
                            password="1234",
                            autocommit=True)

    cursor = conexion.cursor()

    script_insert ="insert into perros (imagen, nombre, precio, marca)" "values (%s, %s, %s, %s)"



    cursor.execute(script_insert, ("https://sinimagen.es",
                                   nuevo_pienso["nombre"],
                                   nuevo_pienso["precio"],
                                   nuevo_pienso["marca"]))

    print("Nuevo pienso insertado con éxito")




class Aplicacion(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"


        ventana = Screen(name="Pienso Perros")


        tabla = MDDataTable(
            padding=20,
            check=True,
            size_hint=(1, 1),
            size=(1, 1),
            use_pagination=True,
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=10,
            rows_num=6,
            pagination_menu_height='200dp',
            background_color_header='#8AF5FF',
            background_color_cell='#00E9FF',
            pagination_menu_pos='center',
            background_color_selected_cell='#00A8FF',
            column_data=[
                ("[size=24][color=#349DA7]id[/color][/size]", dp(20)),
                ("[size=24][color=#349DA7]nombre[/color][/size]", dp(80)),
                ("[size=24][color=#349DA7]precio[/color][/size]", dp(20)),
                ("[size=24][color=#349DA7]marca[/color][/size]", dp(50)),
            ]
        )




        panel = BoxLayout(orientation='vertical', spacing=5)


        panel2 = BoxLayout(orientation='horizontal', spacing=5, size_hint=(1, 0.15), padding=5)


        panel3 = BoxLayout(orientation='vertical', size_hint=(1, 1))




        boton1 = Button(text="Cargar", background_color=(1, 1, 0, 1), color=(1, 2, 0, 2), background_disabled_down='#00A8FF')
        boton1.bind(on_press=lambda a: insertar_datos())

        boton2 = Button(text="Mostrar", background_color=(1, 1, 0, 1), color=(1, 2, 0, 2))
        boton2.bind(on_press=lambda a: mostrar_datos_tabla(tabla))

        boton3 = Button(text="Nuevo", background_color=(1, 1, 0, 1), color=(1, 2, 0, 2))
        boton3.bind(on_press=lambda a: cargar_formulario(panel3))

        boton4 = Button(text="Guardar", background_color=(1, 1, 0, 1), color=(1, 2, 0, 2))
        boton4.bind(on_press=lambda a: guardar_en_bbdd(panel3))





        panel2.add_widget(boton1)
        panel2.add_widget(boton2)
        panel2.add_widget(boton3)
        panel2.add_widget(boton4)


        panel.add_widget(panel2)
        panel3.add_widget(tabla)
        panel.add_widget(panel3)


        ventana.add_widget(panel)


        return ventana


Aplicacion().run()
