// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
	[0] = LAYOUT (
        MT(MOD_LCTL, KC_Q),    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    MT(MOD_RALT,KC_P),
        KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    KC_H,    KC_J,    KC_K,    KC_L,    MT(MOD_LGUI, KC_ENT),
        KC_Z,    LT(2, KC_X),    KC_C,    KC_V,    MT(MOD_LGUI,KC_B),    KC_SPC,    KC_N,    KC_M, LT(1, KC_SLSH),  KC_RSFT
    ),
	[1] = LAYOUT (
		KC_1, KC_2, KC_3, KC_4, KC_5, LSFT(KC_6), LSFT(KC_7), LSFT(KC_8), LSFT(KC_9), LSFT(KC_0),
		KC_LBRC, KC_RBRC, KC_COMM, KC_DOT, KC_MINS, KC_F6, KC_F7, KC_F8, KC_F9, KC_BSLS,
		KC_GRV, KC_LGUI, KC_SCLN, KC_QUOT, KC_EQL, KC_F10, KC_F11, KC_F12, KC_TRNS, KC_RSFT
	),
	[2] = LAYOUT (
		LSFT(KC_1), LSFT(KC_2), LSFT(KC_3), LSFT(KC_4), LSFT(KC_5), KC_6, KC_7, KC_8, KC_9, KC_0,
		KC_LALT, KC_F2, KC_F3, KC_F4, KC_F5, KC_LEFT, KC_DOWN, KC_UP, KC_RGHT, RGUI(KC_ENT),
		KC_LCTL, KC_TRNS, KC_ESC, KC_DEL, KC_BSPC, KC_TAB, KC_HOME, KC_END, KC_RGUI, KC_BSPC
	),
	[3] = LAYOUT (
		KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
		KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
		KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
	),
};
