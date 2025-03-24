import PySimpleGUI as sg


layout = [[sg.Text("Hola"), sg.Input()],
          [sg.Text("Mundo")],
          [sg.Button("Ok")]]

window = sg.Window("Demo", layout, margins=(100,100)).read()
