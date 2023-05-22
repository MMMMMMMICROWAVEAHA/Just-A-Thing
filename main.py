def on_button_pressed_a():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            1,
            1850,
            255,
            0,
            309,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
    for index in range(4):
        basic.show_leds("""
            # . # . #
                        . # # # .
                        # # # # #
                        . # # # .
                        # . # . #
        """)
        basic.pause(100)
        basic.show_leds("""
            # . # . #
                        . . # . .
                        # # # # #
                        . . # . .
                        # . # . #
        """)
    basic.show_string("KA-BOOM!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Microwave")
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play_melody("B E G C5 D B F A ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)
