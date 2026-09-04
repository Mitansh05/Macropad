import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins = [
        board.D0, board.D1, board.D2,
        board.D3, board.D4, board.D5,
        board.D6, board.D7, board.D8
    ],
    value_when_pressed = False
)

keyboard.keymap = [
    [
        KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.CALCULATOR,
        KC.MPLY, KC.MPRV, KC.MUTE,
        KC.LCTRL(KC.LSFT(KC.ESC)), KC.LWIN(KC.LSFT(KC.S)), KC.LWIN(KC.L)
    ]
]

if __name__ == "__main__":
    keyboard.go()

    