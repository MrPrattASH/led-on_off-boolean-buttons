hummingbird.start_hummingbird()
#initialize our first boolean flag variable
light_value = True

def on_forever():
    global light_value
    #turn on LED
    if light_value:
        hummingbird.set_led(ThreePort.ONE, 100)
    #turn off LED
    else:
        hummingbird.set_led(ThreePort.ONE, 0)
basic.forever(on_forever)

def on_button_pressed_a():
    #turn on light
    global light_value
    light_value = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    #turn off light
    global light_value
    light_value = False
input.on_button_pressed(Button.B, on_button_pressed_b)