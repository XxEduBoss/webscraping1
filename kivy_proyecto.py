from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from datos_bbdd import *


def cargar_datos_tabla(tabla):

    # Cargar los datos
    lista_perros = consultar_datos()

    for perro in lista_perros:

        tabla.row_data.append(perro)



class Aplicacion(MDApp):

    def build(self):

        ventana = Screen(name="Pienso Perros")

        tabla = MDDataTable(
            pos_hint={'center_x': 0.5},
            check=True,
            size_hint=(0.7, 0.7),
            use_pagination=True,
            column_data=[
                ("id", dp(20)),
                ("nombre", dp(80)),
                ("precio", dp(20)),
                ("marca", dp(50)),
            ]
        )

        panel = BoxLayout(orientation='vertical', spacing=5)

        panel2 = BoxLayout(orientation='horizontal', spacing=5, size_hint=(1, 0.15))

        panel3 = BoxLayout(orientation='vertical', size_hint=(1, 1))

        boton1 = Button(text="Cargar")
        boton1.bind(on_press=lambda a: insertar_datos())
        boton2 = Button(text="Mostrar")
        boton2.bind(on_press=lambda a: cargar_datos_tabla(tabla))
        boton3 = Button(text="Buscar")
        boton4 = Button(text="Eliminar")
        boton4.bind(on_press=lambda a: panel3.remove_widget())

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
