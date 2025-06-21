from machine import Pin, Timer, ADC
import time

led = machine.Pin(8, machine.Pin.OUT)
#onboard = machine.Pin(25, machine.Pin.OUT)
#button = Pin(15, Pin.IN, Pin.PULL_UP)
tempsensor = machine.ADC(4)
ledDelay= time.ticks_ms()

While True:
    if time.ticks_ms() - ledDelay > 1000:
        ledDelay= time.ticks_ms()
        led.value(not led.value())
        ADC_voltage = tempsensor.read_u16() * (3.3 / (65536))
        temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
        print("Temperature: {}°C".format(temperature_celcius))
    