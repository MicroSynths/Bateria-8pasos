def CICLO():
    global TonoEntrada, VolumenEntrada, Potenciómetro, index2
    pins.digital_write_pin(PINES[index2], 1)
    TonoEntrada = pins.analog_read_pin(AnalogReadWritePin.P3)
    VolumenEntrada = pins.analog_read_pin(AnalogReadWritePin.P2)
    Potenciómetro = pins.analog_read_pin(AnalogReadWritePin.P1)
    Potenciómetro = pins.analog_read_pin(AnalogReadWritePin.P1)
    pins.digital_write_pin(PINES[index2], 0)
    index2 += 1
    if index2 > 7:
        index2 = 0
    pins.digital_write_pin(PINES[index2], 1)
    basic.show_string("" + str((index2 + 1)))
    music.stop_all_sounds()
    Tocar(Potenciómetro, TonoEntrada, VolumenEntrada)
    pins.digital_write_pin(PINES[index2], 0)

def on_button_pressed_a():
    music.change_tempo_by(-5)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pulsed_p15_high():
    global Potenciómetro, TonoEntrada, VolumenEntrada
    Potenciómetro = pins.analog_read_pin(AnalogReadWritePin.P1)
    TonoEntrada = pins.analog_read_pin(AnalogReadWritePin.P2)
    VolumenEntrada = pins.analog_read_pin(AnalogReadWritePin.P3)
    Tocar(Potenciómetro, TonoEntrada, VolumenEntrada)
pins.on_pulsed(DigitalPin.P15, PulseValue.HIGH, on_pulsed_p15_high)

def Tocar(Sonido: number, Tono: number, Volumen: number):
    music.set_volume(Volumen / 4)
    if Sonido > 512:
        music.play(music.create_sound_expression(WaveShape.SINE,
                100 + Tono / 2,
                0,
                255,
                0,
                Sonido - 512,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        music.play(music.create_sound_expression(WaveShape.NOISE,
                10000 + Tono * 5,
                6000 + Tono * 5,
                255,
                0,
                512 - Sonido,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.IN_BACKGROUND)

def on_button_pressed_b():
    music.change_tempo_by(7)
input.on_button_pressed(Button.B, on_button_pressed_b)

Potenciómetro = 0
VolumenEntrada = 0
TonoEntrada = 0
index2 = 0
PINES: List[number] = []
pins.set_audio_pin(DigitalPin.P0)
music.set_tempo(146)
PINES = [DigitalPin.P4,
    DigitalPin.P6,
    DigitalPin.P7,
    DigitalPin.P8,
    DigitalPin.P9,
    DigitalPin.P10,
    DigitalPin.P12,
    DigitalPin.P13]
for value in PINES:
    pins.digital_write_pin(value, 0)

def on_every_interval():
    CICLO()
loops.every_interval(music.beat(BeatFraction.SIXTEENTH), on_every_interval)
