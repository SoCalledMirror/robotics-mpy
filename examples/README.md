__EN__ | [RU](README_RU.md)

---

# SoCalled Robotics (MicroPython) Examples

This&nbsp;directory contains practical examples
demonstrating the&nbsp;capabilities
of&nbsp;the&nbsp;[SoCalled Robotics framework](../README_RU.md).

Each example is&nbsp;provided as&nbsp;a&nbsp;separate __.py__&nbsp;file.
The&nbsp;examples use&nbsp;the&nbsp;installed `socalled` package
and&nbsp;can be&nbsp;run on&nbsp;target devices.

<a name="installation"></a>
## Installation

Before running the&nbsp;examples, [install the&nbsp;framework](../src/README_RU.md#installation).
There&nbsp;is no&nbsp;need to&nbsp;copy the&nbsp;__examples__ directory to&nbsp;the&nbsp;device.

*	To&nbsp;install an&nbsp;example file from the&nbsp;network, use
	the&nbsp;[package manager](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote):

	``` bash
	mpremote mip install --target / https://socalled.link/robotics-mpy/raw/main/examples/{example_name}.py
	```

	The&nbsp;`--target` flag allows you to&nbsp;specify
	the&nbsp;target directory on&nbsp;the&nbsp;device
	(by&nbsp;default, modules are&nbsp;installed in&nbsp;__/lib__).
*	For&nbsp;local installation from&nbsp;a&nbsp;cloned repository
	copy the&nbsp;example file to&nbsp;the&nbsp;device manually:

	```bash
	mpremote fs cp examples/{example_name}.py :
	```

	To&nbsp;make the&nbsp;example run automatically when the&nbsp;device starts,
	save it&nbsp;as&nbsp;the&nbsp;__main.py__ file:

	```bash
	mpremote fs cp examples/{example_name}.py :main.py
	```

<a name="available-examples"></a>
## Available Examples

Additional instructions for&nbsp;running and&nbsp;code explanations
are&nbsp;provided in&nbsp;the&nbsp;comments within example files.

### Blinking LED

[__blinking_led.py__](blinking_led.py)

This example demonstrates the&nbsp;core principle of&nbsp;hardware abstraction
by&nbsp;using the&nbsp;framework's wrappers
for&nbsp;&nbsp;`machine.Pin&nbsp;class and&nbsp;`time.sleep`&nbsp;method.
&nbsp;also includes basic error handling for hardware initialisation.

__Expected Behavior:__
The&nbsp;built-in LED blinks continuously with a&nbsp;1-second interval.

ESP8266 built-in LED logic:

*	Pin 2 is the on-board LED.
*	LED is ACTIVE LOW:
	*	`led.value(0)` or `led.off()` → LED __ON__;
	*	`led.value(1)` or `led.on()` → LED __OFF__.

---

_Copyright&nbsp;©&nbsp;2026 [SoCalled Robotics (MicroPython) Contributors](CONTRIBUTORS.md)._
_This document is&nbsp;licensed under the&nbsp;[Creative Commons Attribution&nbsp;4.0 International Public License](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
