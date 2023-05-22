input.onButtonPressed(Button.A, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1, 1850, 255, 0, 309, SoundExpressionEffect.Vibrato, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . . # . .
            # # # # #
            . . # . .
            # . # . #
            `)
    }
    basic.showString("KA-BOOM!")
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Microwave")
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("B E G C5 D B F A ", 120)
})
