hummingbird.startHummingbird()
// initialize our first boolean flag variable
let light_value = true
basic.forever(function on_forever() {
    
    // turn on LED
    if (light_value) {
        hummingbird.setLED(ThreePort.One, 100)
    } else {
        // turn off LED
        hummingbird.setLED(ThreePort.One, 0)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    // turn on light
    
    light_value = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    // turn off light
    
    light_value = false
})
