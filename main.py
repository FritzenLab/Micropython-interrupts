from machine import Pin, Timer, ADC
import time

led = machine.Pin(16, machine.Pin.OUT)
#onboard = machine.Pin(25, machine.Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)
tempsensor = machine.ADC(4)

led.off()
#onboard.off()
buttonTime = time.ticks_ms()
buttonTime = 0
ledFundamental = 0
blinkState = False
tempcounter = 0

def toggle_led(timer):
    global blinkState
    global tempcounter
    
    if blinkState == True:
        led.value(not led.value())  # Toggle the LED state (ON/OFF)
        tempcounter= tempcounter + 1
        
        if tempcounter == 4:
            tempcounter = 0
            ADC_voltage = tempsensor.read_u16() * (3.3 / (65536))
            temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
            print("Temperature: {}°C".format(temperature_celcius))
            
    else:
        led.value(0)

def callback(button):
    global buttonTime
    global blinkState
    # This IF is the debounce for the button reading. It also defines the blinking state
    # (on or off)
    if time.ticks_ms() - buttonTime > 400:
        buttonTime = time.ticks_ms()
        blinkState = not blinkState

button.irq(trigger=Pin.IRQ_FALLING, handler=callback)
blink_timer = Timer()
blink_timer.init(mode=Timer.PERIODIC, period=250, callback=toggle_led)  # Timer repeats every 0.25 seconds

 
# While True:  # This not necessary since we are handling everything
                # inside callbacks