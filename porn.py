from PySimpleGUI import PySimpleGUI as sg
from pornhub_api import PornhubApi
import webbrowser

# Api Client PornHub
api = PornhubApi()

# Layout
sg.theme('Black')
menu_def = [['Help', ['GitHub', 'About']]]
layout = [
    [sg.Menu(menu_def, background_color='black')],
    [sg.Text('1 - Hentai\n2 - Anal\n3 - Gay\n4 - Brazilian')],
    [sg.Text('Enter category:'), sg.Input(
        key='category_', text_color='yellow')],
    #[sg.Text('Warn: Recommended for ages 18 and over.', text_color='red')],
    [sg.Button('Search')],
    [sg.Output(key='_log_', visible=False, size=(75, 25))]
]

# Janela
window = sg.Window('PornHub CLI | Videos Search', icon='./logo.ico').Layout(layout)
sg.ChangeLookAndFeel('black')
# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'GitHub':
        webbrowser.open('https://github.com/pauloodev')
    else:
        if eventos == 'About':
            sg.popup('About this program:', 'This program uses a third-party api. I just did a simple project with a simple GUI.', '- Version 1.2\n- Twitter: @pauloodeev', title='About', button_color='white', text_color='white', background_color='black', icon='./logo.ico')

    if eventos == 'Search':
        if valores['category_'] == '1':
            window.FindElement('_log_').Update('')
            result = api.search.search(
                ordering='recent', category='hentai')
            for vid in result.videos:
                window['_log_'].update(visible=True)
                window.Element('_log_')._TKOut.output.bind(
                    "<Key>", lambda e: "break")
                print('Title: ' + vid.title + '\nLink: ' + vid.url + '\n')

        if valores['category_'] == '2':
            window.FindElement('_log_').Update('')
            result = api.search.search(
                ordering='recent', category='anal')
            for vid in result.videos:
                window['_log_'].update(visible=True)
                window.Element('_log_')._TKOut.output.bind(
                    "<Key>", lambda e: "break")
                print('Title: ' + vid.title + '\nLink: ' + vid.url + '\n\n')

        if valores['category_'] == '3':
            window.FindElement('_log_').Update('')
            result = api.search.search(
                ordering='recent', category='gay')
            for vid in result.videos:
                window['_log_'].update(visible=True)
                window.Element('_log_')._TKOut.output.bind(
                    "<Key>", lambda e: "break")
                print('Title: ' + vid.title + '\nLink: ' + vid.url + '\n\n')

        if valores['category_'] == '4':
            window.FindElement('_log_').Update('')
            result = api.search.search(
                ordering='recent', category='brazilian')
            for vid in result.videos:
                window['_log_'].update(visible=True)
                window.Element('_log_')._TKOut.output.bind(
                    "<Key>", lambda e: "break")
                print('Title: ' + vid.title + '\nLink: ' + vid.url + '\n\n')
    # if valores['senha'] == '159753':
    #     print('[LOGIN] - Olá \n[LOGIN] - Logado com sucesso!')
    # else:
    #     print('[ERROR] Senha incorreta, tente novamente!')
