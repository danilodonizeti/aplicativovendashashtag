from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests



GUI = Builder.load_file("main.kv")
class MainApp(App):
    id_usuario = 1

    def build(self):
        return GUI

    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

'''
É PRECISO INSTALAR O MÓDULO SSL PARA INTEGRAR COM O FIREBASE: https://slproweb.com/products/Win32OpenSSL.html
Após correção voltar para a aula "Pegando informações do Banco de Dados"
Link da aula: https://hashtag.eadplataforma.com/lesson/detail/15/4262/
Tempo da aula: 3:40
'''


'''
    def on_start(self):
        requisicao = requests.get(f"https://aplicativovendashash-431d3-default-rtdb.firebaseio.com/")
       print(requisicao.json())
'''



MainApp().run()
