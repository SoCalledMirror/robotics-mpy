# SPDX-FileCopyrightText: 2026 SoCalled Robotics Contributors <community@socalled.link>
# SPDX-License-Identifier: MPL-2.0

"""
Basic LED Blinking Example for SoCalled Robotics.

This example demonstrates the core principle of hardware abstraction
by using the framework's wrapper for the `machine.Pin` class.
It also includes basic error handling for hardware initialisation.

Expected Behavior:
    The built-in LED blinks continuously with a 1-second interval.

ESP8266 built-in LED logic:
- Pin 2 is the on-board LED.
- LED is ACTIVE LOW:
  led.value(0) or led.off() → LED **ON**;
  led.value(1) or led.on()  → LED **OFF**.
"""

import socalled

# Pin 2 is the built-in LED on most ESP8266 boards
LED_PIN_NUMBER = 2

try:
    # Create LED object through framework abstraction
    led_pin = socalled.Pin(LED_PIN_NUMBER, socalled.Pin.OUT)
    # Turn LED **ON** (active-low logic)
    led_pin.off()
    print('LED on pin', LED_PIN_NUMBER, 'initialized successfully')

except Exception as error:
    # Catch any hardware-init failure
    print('Hardware error', error)
    # Re-raise to stop execution
    raise

print('Starting blink loop (press Ctrl+C to stop)')

try:
    while True:
        # Invert state: 0→1 or 1→0 (active-low LED toggles on/off)
        led_pin.value(not led_pin.value())
        socalled.sleep(0.5)

except KeyboardInterrupt:
    # Graceful shutdown on Ctrl+C
    print('\nBlinking stopped by user')
    # Turn LED **ON** (active-low logic)
    led_pin.off()
    print('LED turned on')
