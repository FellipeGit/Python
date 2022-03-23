import PySimpleGUI as sg
import random, string


class App:
    def __init__(self):

        sg.theme('DarkAmber')

        layout = [  [sg.Text('Password length'), sg.Combo(values=list(range(31)), key='size', default_value=1, size=(3,1))],
                    [sg.Text('Include uppercase letters'), sg.Checkbox('',default=True,key='upper', enable_events=True)],
                    [sg.Text('Include lowercase letters'), sg.Checkbox('',default=True,key='lower', enable_events=True)],
                    [sg.Text('Include numbers'), sg.Checkbox('',default=True,key='number', enable_events=True)],
                    [sg.Text('Include symbols'), sg.Checkbox('',default=True,key='symbol', enable_events=True)],
                    [sg.Button('LEEEETSSS GOOOOOOO')],
                    [sg.Output(size=(50,10))]  ] 

        self.screen = sg.Window('Password Generator', layout)

    def generate_password(self, size, hasUpper, hasLower, hasNumber, hasSymbol):

        chars = ''

        if hasUpper == True:
            chars += string.ascii_uppercase
        if hasLower == True:
            chars += string.ascii_lowercase
        if hasNumber == True:
            chars += string.digits
        if hasSymbol == True:
            chars += string.punctuation

        rnd = random.SystemRandom() #os.urandom

        result = (''.join(rnd.choice(chars) for i in range(size)))

        return result

    def start_window(self):
        while True:

            self.button, self.values = self.screen.read()

            try:
                if self.button == sg.WIN_CLOSED:
                    break
                elif self.button == 'LEEEETSSS GOOOOOOO':
                    valores = self.generate_password(self.values['size'], self.values['upper'], self.values['lower'], self.values['number'], self.values['symbol'])
                    print(valores)
            
            except:
                print("Error, function not defined")


fc = App()
fc.start_window()
