function CICLO () {
    pins.digitalWritePin(PINES[index2], 1)
    TonoEntrada = pins.analogReadPin(AnalogReadWritePin.P3)
    TonoEntrada = pins.analogReadPin(AnalogReadWritePin.P3)
    VolumenEntrada = pins.analogReadPin(AnalogReadWritePin.P2)
    VolumenEntrada = pins.analogReadPin(AnalogReadWritePin.P2)
    Potenciómetro = pins.analogReadPin(AnalogReadWritePin.P1)
    Potenciómetro = pins.analogReadPin(AnalogReadWritePin.P1)
    pins.digitalWritePin(PINES[index2], 0)
    index2 += 1
    if (index2 > 7) {
        index2 = 0
    }
    pins.digitalWritePin(PINES[index2], 1)
    music.stopAllSounds()
    Tocar(Potenciómetro, TonoEntrada, VolumenEntrada)
}
input.onButtonPressed(Button.A, function () {
    music.changeTempoBy(-5)
})
pins.onPulsed(DigitalPin.P15, PulseValue.High, function () {
    CICLO()
})
function Tocar (Sonido: number, Tono: number, Volumen: number) {
    music.setVolume(Volumen / 4)
    if (Sonido > 350) {
        music.play(music.createSoundExpression(
        WaveShape.Noise,
        10000 + Tono * 3,
        5000 + Tono * 3,
        255,
        0,
        Sonido - 512,
        SoundExpressionEffect.None,
        InterpolationCurve.Curve
        ), music.PlaybackMode.InBackground)
    } else {
        music.play(music.createSoundExpression(
        WaveShape.Sine,
        175 + Tono / 3,
        20,
        255,
        0,
        1050 - Sonido * 3,
        SoundExpressionEffect.None,
        InterpolationCurve.Curve
        ), music.PlaybackMode.InBackground)
    }
}
input.onButtonPressed(Button.B, function () {
    music.changeTempoBy(7)
})
let Potenciómetro = 0
let VolumenEntrada = 0
let TonoEntrada = 0
let index2 = 0
let PINES: number[] = []
led.enable(false)
pins.setAudioPin(DigitalPin.P0)
music.setTempo(150)
PINES = [
DigitalPin.P4,
DigitalPin.P6,
DigitalPin.P7,
DigitalPin.P8,
DigitalPin.P9,
DigitalPin.P10,
DigitalPin.P12,
DigitalPin.P13
]
for (let value of PINES) {
    pins.digitalWritePin(value, 0)
}
pins.digitalWritePin(DigitalPin.P14, 0)
loops.everyInterval(music.beat(BeatFraction.Half), function () {
    pins.digitalWritePin(DigitalPin.P14, 0)
    CICLO()
    pins.digitalWritePin(DigitalPin.P14, 1)
})
