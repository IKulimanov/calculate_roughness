from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

from kivy.config import Config
#Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 600)
Config.set('graphics', 'width', 600)


class MyApp(App):
    def build(self):
        bl = BoxLayout()
        material = BoxLayout()

        view_type = BoxLayout()

        checkbox_type_m1 = CheckBox()
        checkbox_type_m1.bind(active=self.on_check_type_material)

        checkbox_type_m2 = CheckBox()
        checkbox_type_m2.bind(active=self.on_check_type_material)

        checkbox_view_outer = CheckBox()
        checkbox_view_outer.bind(active=self.on_check_view_outer)

        checkbox_view_inter = CheckBox()
        checkbox_view_inter.bind(active=self.on_check_view_inter)

        material.add_widget(checkbox_type_m1)
        material.add_widget(checkbox_type_m2)
        view_type.add_widget(checkbox_view_outer)
        view_type.add_widget(checkbox_view_inter)

        bl.add_widget(material)
        bl.add_widget(view_type)

        return bl


    def on_check_type_material(self, checkbox, value):
        if value:
            print("t")
        else:
            print("a")

    def on_check_view_outer(self, checkbox, value):
        if value:
            print("v")
        else:
            print("s")

    def on_check_view_inter(self, checkbox, value):
        if value:
            print("v")
        else:
            print("s")