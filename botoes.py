from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior


# Nas classes abaixo, para o texto funcionar como botão, o "ButtonBehavior" TEM QUE VIR PRIMEIRO.
class ImageButton(ButtonBehavior, Image):
    pass

class LabelButton(ButtonBehavior, Label):
    pass