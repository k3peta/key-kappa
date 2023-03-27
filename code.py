print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap]


# 列ピンの定義
keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
# 行ピンの定義
keyboard.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

CTL_Q = KC.MT(KC.Q, KC.LCTL)
ALT_P = KC.MT(KC.P, KC.LALT)
GUI_ENT = KC.MT(KC.ENT, KC.LGUI)
SFT_Z = KC.MT(KC.Z, KC.LSFT)
LT1_SLSH = KC.LT(1, KC.SLSH)
LT2_X = KC.LT(2, KC.X)


keyboard.keymap = [
    [
        CTL_Q,    KC.W,    KC.E,    KC.R,   KC.T,     KC.Y,    KC.U,    KC.I,    KC.O,    ALT_P,
        KC.A,    KC.S,    KC.D,    KC.F,   KC.G,     KC.H,    KC.J,    KC.K,    KC.L,    GUI_ENT,
        SFT_Z,    LT2_X,    KC.C,    KC.V,   KC.B,     KC.SPC,    KC.N,    KC.M,    LT1_SLSH,    KC.RSFT
    ],
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.CIRC,   KC.AMPR,   KC.ASTR,   KC.LPRN,   KC.RPRN,
        KC.LBRC,    KC.RBRC,    KC.COMM,    KC.DOT,   KC.MINS,     KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.BSLS,
        KC.GRAVE,    KC.LGUI,    KC.SCOLON,    KC.QUOT,   KC.EQL,     KC.F10,    KC.F11,    KC.F12,    KC.TRNS,    KC.RSFT
    ],
    [
        KC.EXLM,   KC.AT,   KC.HASH,   KC.DLR,   KC.PERC,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.ALT,   KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.LEFT,    KC.DOWN,    KC.UP,    KC.RGHT,    KC.RGUI(KC.ENT),
        KC.LCTL,    KC.TRNS,    KC.ESC,    KC.DEL,   KC.BSPC,     KC.TAB,    KC.HOME,    KC.END,    KC.RGUI,    KC.BSPC
    ],
]

if __name__ == '__main__':
    keyboard.go()
