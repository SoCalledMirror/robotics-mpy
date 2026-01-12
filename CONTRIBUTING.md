__EN__ | [RU](CONTRIBUTING_RU.md)

---

# SoCalled Robotics (MicroPython) Contribution Guide

Thank you for&nbsp;your interest in&nbsp;contributing
to&nbsp;the&nbsp;[SoCalled Robotics (MicroPython)](README.md) project!

⚠️ First, read
the&nbsp;[general contribution guide for&nbsp;the&nbsp;SoCalled community](https://socalled.link/community/CONTRIBUTING.md).
It&nbsp;describes key processes, working with tasks and&nbsp;Git,
commit and&nbsp;DCO requirements, and&nbsp;other ways to&nbsp;contribute.

This document establishes framework‑specific rules
for&nbsp;style, architecture, documentation, and&nbsp;formatting.

## Contents

*	[Quick Start](#quick-start)
*	[Architectural Principles](#architecture)
	*	[Hardware Abstraction](#hardware-abstraction)
	*	[Lazy Initialization](#lazy-init)
	*	[Thread Safety](#thread-safety)
	*	[Efficiency](#efficiency)
	*	[Stability](#stability)
	*	[Installation via&nbsp;mip](#mip-install)
	*	[Testing with Examples](#examples)
*	[Code Style](#code-style)
	*	[Naming Conventions](#code-naming)
	*	[Formatting](#code-formatting)
	*	[Imports](#code-imports)
	*	[Constants and “Magic Numbers”](#code-constants)
*	[Code Documentation](#code-documentation)
	*	[Docstrings](#docstrings)
	*	[Architectural Comments](#arch-comments)
*	[Task Labels](#labels)
*	[Licensing and Copyright](#licensing)

<a name="quick-start"></a>
## Quick Start

To start developing:

1.	Explore the&nbsp;[issue tracker](https://socalled.link/robotics-mpy/issues).
2.	Find any open task (e.g.,&nbsp;labeled __Good First Issue__).
3.	Leave a&nbsp;comment stating your willingness to&nbsp;work on&nbsp;it.
4.	After approval from the&nbsp;maintainers,
	begin work following the&nbsp;[general](https://socalled.link/community/CONTRIBUTING.md)
	and project‑specific rules.

<a name="architecture"></a>
## Architectural Principles

Code must comply with the&nbsp;[design principles](README.md#design-principles).
The following approaches are used:

<a name="hardware-abstraction"></a>
### Hardware Abstraction

Use standard `machine` classes (`Pin`, `PWM`).
Where appropriate, reuse and&nbsp;extend existing framework classes.

Functionality you add must be&nbsp;compatible
with all target devices unless otherwise specified
(e.g., adapting the&nbsp;framework for&nbsp;a&nbsp;new device).

<a name="lazy-init"></a>
### Lazy Initialization

Allocate resources (memory, timers, pins) on&nbsp;the&nbsp;first use
and&nbsp;release them as&nbsp;soon as&nbsp;they are no&nbsp;longer needed.

<a name="thread-safety"></a>
### Thread Safety

Ensure data consistency and&nbsp;operation sequence
when code may run in&nbsp;an&nbsp;interrupt context.
For shared data, use:

```python
machine.disable_irq()
# safe code here
machine.enable_irq()
```

<a name="efficiency"></a>
### Efficiency

In&nbsp;performance‑critical or&nbsp;memory‑critical code sections
(interrupt handlers, frequent callbacks),
avoid constructs that create unnecessary overhead, such as&nbsp;f‑strings (`f"..."`).
Prefer string concatenation or&nbsp;pre‑prepared templates.

<a name="stability"></a>
### Stability

Code must be&nbsp;resilient to&nbsp;possible failures.

*	When working with hardware, always wrap operations in&nbsp;`try`/`except`
	to&nbsp;handle potential failures.
*	Use built‑in Python exceptions (`ValueError`, `TypeError`, `OSError`, etc.)
	for standard cases.
*	Avoid “bare” `except` statements;
	specify concrete exception types.

<a name="mip-install"></a>
### Installation via&nbsp;mip

The framework libraries must be&nbsp;available
for&nbsp;[installation via the package manager](src/README.md#installation-mip).
For each new module, specify&nbsp;it in&nbsp;the&nbsp;files:

*	[__package.json__](package.json), the&nbsp;`urls` list
	(in&nbsp;lexicographic order relative to&nbsp;other modules);
*	[__socalled/\_\_init\_\_.py__](socalled/__init__.py), the&nbsp;`__attr_modules__` map
	(in&nbsp;lexicographic order relative to&nbsp;other attributes).

When adding or modifying modules,
update the&nbsp;framework version in&nbsp;these files
according to&nbsp;[Semantic Versioning](https://semver.org/)
__MAJOR.MINOR.PATCH__:

*	__PATCH__ for&nbsp;bug fixes;
*	__MINOR__ for&nbsp;new modules or&nbsp;functionality.

Before submitting a&nbsp;pull request, __make sure__
that the&nbsp;modules install correctly:

```bash
mpremote mip install package.json
```

and import correctly:

```python
import socalled
from socalled import {ClassName}
print(socalled.__version__)
```

If you encounter a&nbsp;`MemoryError` or `ImportError`,
fix the&nbsp;issue before creating a&nbsp;pull request.

<a name="examples"></a>
### Testing with Examples

All added logic must be&nbsp;validated.
Create or&nbsp;update [examples](examples/README.md#available-examples)
to&nbsp;demonstrate new functionality.
Before submitting a&nbsp;pull request,
__make sure__ that all existing examples run on&nbsp;the&nbsp;target devices.

<a name="code-style"></a>
## Code Style

Consistent code style improves readability
and&nbsp;eases collaboration and&nbsp;maintenance.

<a name="code-naming"></a>
### Naming Conventions

Use the&nbsp;following styles for&nbsp;different code elements:

| Code Element        | Style              | Examples
|:--                  |:--                 |:--
| Module files        | __snake_case__     | __socalled/timer.py__, __socalled/event_loop.py__
| Classes             | `CamelCase`        | `EventLoop`, `ServoController`
| Functions & methods | `snake_case`       | `async_sleep_ms()`, `read()`
| Constants           | `UPPER_SNAKE_CASE` | `MAX_DISTANCE_CM`
| Private attributes  | `_snake_case`      | `_events`, `_sleep_time_ms`

For variables and&nbsp;arguments representing physical quantities,
add a&nbsp;suffix with measurement units, e.g., `timeout_ms`, `distance_cm`.
This improves clarity and&nbsp;helps avoid errors.

<a name="code-formatting"></a>
### Formatting

*	__Indentation.__  
	4 spaces per level.
*	__Line length.__  
	Aim for&nbsp;79&nbsp;characters.
	Up&nbsp;to&nbsp;120&nbsp;characters is&nbsp;allowed
	if&nbsp;it&nbsp;improves readability.
*	__Spacing.__  
	Surround operators with spaces (`a = b + 1`).
	Place a&nbsp;space after commas in&nbsp;lists.

<a name="code-imports"></a>
### Imports

*	Order:
	1.	Standard Python libraries.
	2.	MicroPython libraries.
	3.	Project modules (`socalled`).
*	Within each group — alphabetical order.
*	Use absolute imports.
*	Always import modules and classes explicitly.
	Wildcard imports (`*`) are prohibited:

```python
from socalled import {ClassName}
```

<a name="code-constants"></a>
### Constants and “Magic Numbers”

Place all numeric or&nbsp;string literals with non‑obvious meaning
(e.g., timings, error codes, buffer sizes, sensor calibration coefficients)
into named constants (`UPPER_SNAKE_CASE`)
at&nbsp;the&nbsp;top of&nbsp;the&nbsp;module or&nbsp;inside classes.

<a name="code-documentation"></a>
## Code Documentation

Clear comments and&nbsp;documentation significantly ease understanding, usage,
and&nbsp;evolution of&nbsp;the&nbsp;code.

<a name="docstrings"></a>
### Docstrings

Use [__Google‑style docstrings__](https://google.github.io/styleguide/pyguide.html#docstrings)
in&nbsp;English for&nbsp;all public modules, classes, functions, and methods.

Required elements for&nbsp;a&nbsp;method or&nbsp;a&nbsp;function:

*	Brief description of&nbsp;purpose.
*	__Args__ is&nbsp;a&nbsp;list of&nbsp;arguments
	with type and&nbsp;purpose.
*	__Returns__ is&nbsp;a&nbsp;description
	of&nbsp;the&nbsp;return value, including type.
*	__Raises__ is&nbsp;list of&nbsp;exceptions
	that may&nbsp;be&nbsp;raised, with conditions.

Example:

```python
def calculate_distance(duration_us):
    """
    Calculate distance from pulse duration.

    Args:
        duration_us (int): Pulse duration in microseconds.

    Returns:
        float: Distance in centimeters, -1.0 on timeout.

    Raises:
        ValueError: If duration is negative.
    """
```

<a name="arch-comments"></a>
### Architectural Comments

Significant architectural decisions,
especially those concerning memory optimization, power consumption, or&nbsp;thread safety,
must&nbsp;be&nbsp;commented in&nbsp;the&nbsp;code.

*	Use comments to&nbsp;explain non‑obvious decisions or&nbsp;complex logic.
*	Explain _why_ a&nbsp;particular implementation was chosen,
	if&nbsp;it&nbsp;is&nbsp;not&nbsp;obvious.
*	Avoid comments that merely duplicate the&nbsp;code.
*	Place the&nbsp;comment above the&nbsp;explained block,
	starting with a&nbsp;capital letter.

Example:

```python
# Using list instead of dict to save memory per event (~16 bytes)
# Format: [handler, timestamp_ms, period_ms]
self._events = []
```

<a name="labels"></a>
## Task Labels

[Community‑wide labels](https://socalled.link/community/CONTRIBUTING.md#labels)
as&nbsp;well as&nbsp;project‑specific component labels
are&nbsp;used for&nbsp;task categorization.
It&nbsp;is&nbsp;recommended to&nbsp;include them in&nbsp;commit titles
in&nbsp;square brackets to&nbsp;indicate the&nbsp;scope of&nbsp;changes
(e.g., `[sensors] Add calibration methods...`).

| Label              | Purpose                | Component examples
|:--                 |:--                     |:--
| __Actuators__      | Actuator control       | `Servo`, `ServoController`
| __Core__           | Core changes           | `Timer`, `EventLoop`
| __Documentation__  | Documentation          | __README.md__, __CONTRIBUTING.md__
| __Examples__       | Usage examples         | __examples/blinking_led.py__
| __Infrastructure__ | Project infrastructure | __\_\_init\_\_.py__, __package.json__
| __Input__          | Input handling         | `Button`
| __Sensors__        | Working with sensors   | `DigitalSensor`, `Hcsr04Sensor`

<a name="licensing"></a>
## Licensing and Copyright

__Source code__ is&nbsp;distributed under
the&nbsp;__[Mozilla Public License&nbsp;2.0 (MPL‑2.0)](https://socalled.link/community/LICENSE_MPL-2.0.md)__ license.
Add the&nbsp;SPDX header comment
(adjusting the&nbsp;comment format and&nbsp;year as&nbsp;necessary)
at&nbsp;the top of&nbsp;each source file:

```python
# SPDX-FileCopyrightText: 2026 SoCalled Robotics Contributors <community@socalled.link>
# SPDX-License-Identifier: MPL-2.0
```

__Documentation and other creative materials__ (including this file) are&nbsp;distributed under
the&nbsp;__[Creative Commons Attribution&nbsp;4.0 International (CC‑BY‑4.0)](https://socalled.link/community/LICENSE_CC-BY-4.0.md)__ license.
Add the&nbsp;following notice
(adjusting the&nbsp;format and&nbsp;year as&nbsp;necessary)
at&nbsp;the&nbsp;end of&nbsp;each documentation file:

```markdown
---

_Copyright&nbsp;©&nbsp;2026 [SoCalled Robotics (MicroPython) Contributors](CONTRIBUTORS.md)._
_This document is&nbsp;licensed under the&nbsp;[Creative Commons Attribution&nbsp;4.0 International Public License](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
```

---

_Copyright&nbsp;©&nbsp;2026 [SoCalled Robotics (MicroPython) Contributors](CONTRIBUTORS.md)._
_This document is&nbsp;licensed under the&nbsp;[Creative Commons Attribution&nbsp;4.0 International Public License](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
