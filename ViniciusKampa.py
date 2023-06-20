import PySimpleGUI as sg

sg.theme('DarkGrey3')

layout = [
    [sg.Input(size=(20,1), key='expressao', justification='right', readonly=True), sg.Button('C')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+') ],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-') ],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*') ],
    [sg.Button('0'), sg.Button('.'), sg.Button('/'), sg.Button('=') ],
]

window = sg.Window('Calculadora', layout)

clear = ''

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '=':
        expressao = values['expressao']

        try:
            resultado = eval(expressao)
            sg.Popup(f'O resultado é: {resultado}')
        except:
            sg.Popup('Expressão inválida!')

    elif event in '0123456789.+-*/':
        window['expressao'].update(values['expressao'] + event)
    
    if event == 'C':
      clear = ''
      window['expressao'].update(clear)
    

window.close()
