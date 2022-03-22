import PySimpleGUI as sg
import requests, json

class App:
    def __init__(self):

        sg.theme('DarkAmber')

        # Cria o layout da tela
        layout = [  [sg.Text('CEP'), sg.Input(size=(30,0), key='CEP')],
                    [sg.Button('Buscar')],
                    [sg.Output(size=(60,20))]  ]  

        self.screen = sg.Window('Buscador CEP', layout)

    def consultacep(self, cep):

        url = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        if url.status_code == 200:
            print("Success !")
        elif url.status_code == 400:
            print("Error")

        address_data = url.json()

        return address_data

    def start_window(self):
        while True:

            self.button, self.values = self.screen.Read()

            try:
                if self.button == sg.WIN_CLOSED:
                    break
                elif self.button == 'Buscar':
                    valores = self.consultacep(self.values['CEP'])
                    for k, v in valores.items():
                        print(k.upper() , ':' ,v)
            
            except:
                print("Error, função não definida")

fc = App()
fc.start_window()
