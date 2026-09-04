from kmk.keys import KC

# This file ONLY stores your actual keys
KEYMAP = [
    [
        # ROW 1: Clipboard and Utility
        KC.LCTRL(KC.C),            KC.LCTRL(KC.V),            KC.CALCULATOR,
        
        # ROW 2: Media Actions
        KC.MPLY,                   KC.MPRV,                   KC.MUTE,
        
        # ROW 3: System Tools & Lock Screen
        KC.LCTRL(KC.LSFT(KC.ESC)), KC.LWIN(KC.LSFT(KC.S)),    KC.LWIN(KC.L)
    ]
]