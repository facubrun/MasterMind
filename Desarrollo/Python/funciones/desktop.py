import PySimpleGUI as sg

button_size = (7, 4)
PLAYER_ONE = "X"
PLAYER_TWO = "O"

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
winner_plays = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
    [0, 4, 8], [2, 4, 6]              # Diagonales
]

layout = [
    [sg.Text('Turno de: X', key='-TURN-', size=(15, 1), justification='center')],
    [
        sg.Button("", key="-0-", size=button_size),
        sg.Button("", key="-1-", size=button_size),
        sg.Button("", key="-2-", size=button_size)
    ],
    [
        sg.Button("", key="-3-", size=button_size),
        sg.Button("", key="-4-", size=button_size),
        sg.Button("", key="-5-", size=button_size)
    ],
    [
        sg.Button("", key="-6-", size=button_size),
        sg.Button("", key="-7-", size=button_size),
        sg.Button("", key="-8-", size=button_size)
    ],
    [
        sg.Button("Terminar", key="-OK-"),
        sg.Button("Revancha", key="-RESTART-")
    ]
]

def restart_game(window):
    global deck
    deck = [0] * 9
    for i in range(9):
        window[f"-{i}-"].Update(text="")
    window["-TURN-"].Update("Turno de: X")

def move_and_check(window, event, current_player):
    if window.Element(event).ButtonText == "":
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                sg.popup(f"El jugador {current_player} ha ganado")
                return True

        if 0 not in deck:
            sg.popup("Juego terminado! Nadie gana")
            return True
    return False

def next_player(current_player):
    if current_player == PLAYER_ONE:
        return PLAYER_TWO
    else:
        return PLAYER_ONE

def tres_en_raya(window):
    current_player = PLAYER_ONE
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-OK-":
            break

        if event == "-RESTART-":
            restart_game(window)
            current_player = PLAYER_ONE
            continue

        finished = move_and_check(window, event, current_player)
        if not finished:
            current_player = next_player(current_player)
            window["-TURN-"].Update(f"Turno de: {current_player}")

def main():
    window = sg.Window("Tres en Raya", layout, margins=(100, 100))
    tres_en_raya(window)
    window.close()

if __name__ == "__main__":
    main()
