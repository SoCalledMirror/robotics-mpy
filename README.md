# SoCalled Robotics (MicroPython)

__A&nbsp;lightweight, event‑driven framework
for&nbsp;robotics and&nbsp;IoT&nbsp;on&nbsp;MicroPython.__

[Get Started](#quick-start) •
[Chat](https://t.me/SoCalledGroup) •
[Blog](https://t.me/SoCalledBlog) •
[Issues](https://socalled.link/robotics-mpy/issues)

__SoCalled Robotics__ is&nbsp;an&nbsp;open‑source framework
for&nbsp;building robotics and&nbsp;IoT applications for&nbsp;microcontrollers.
It&nbsp;provides ready‑to‑use, optimized components
for&nbsp;working with hardware, timers, events, and&nbsp;peripherals,
letting you focus on&nbsp;application logic instead of&nbsp;low‑level details.

The&nbsp;project is&nbsp;developed openly
within the&nbsp;[SoCalled Community](https://socalled.link/community),
a&nbsp;community of&nbsp;like‑minded people
sharing common [values](https://socalled.link/community/README.md#values)
and&nbsp;[principles](https://socalled.link/community/README.md#principles).

📚&nbsp;[Learn more about processes in&nbsp;Contribution Guide](https://socalled.link/community/CONTRIBUTING.md)

<a name="vision"></a>
## Our Vision

The&nbsp;project creates an&nbsp;ecosystem for&nbsp;easy integration of&nbsp;various devices.
We&nbsp;gradually explore and&nbsp;implement the&nbsp;capabilities
of&nbsp;microcontrollers, MicroPython, and&nbsp;attachable peripherals,
building a&nbsp;library of&nbsp;components that work together “out&nbsp;of&nbsp;the&nbsp;box”.
The&nbsp;long‑term goal is&nbsp;to&nbsp;create a&nbsp;coherent ecosystem
where MicroPython components will be&nbsp;compatible with a&nbsp;C++ implementation
for&nbsp;AVR and&nbsp;other platforms.

<a name="design-principles"></a>
## Design Principles

The&nbsp;framework is&nbsp;built around core principles that define its&nbsp;architecture:

*	__Hardware Abstraction.__  
	A&nbsp;uniform API for&nbsp;different microcontroller platforms,
	simplifying porting and&nbsp;development.
*	__Memory Efficiency.__  
	Optimized for&nbsp;devices with limited RAM/ROM
	using singletons and&nbsp;efficient data structures.
*	__Energy Efficiency.__  
	Intelligent sleep between events and&nbsp;low‑power tasks to&nbsp;extend battery life.
*	__Thread Safety.__  
	Atomic operations and&nbsp;reentrancy protection
	for&nbsp;reliable operation in&nbsp;asynchronous scenarios.
*	__Extensibility.__  
	Ease of&nbsp;adding new components while maintaining architectural consistency.
*	__API Compatibility.__  
	Maximum possible API compatibility with implementations of&nbsp;the&nbsp;framework
	for&nbsp;other programming languages.
*	__Component Connectivity.__  
	Components are&nbsp;designed for&nbsp;easy integration into distributed systems
	where devices running different languages and&nbsp;platforms can work together.

<a name="target-platforms"></a>
## Target Platforms

The&nbsp;first version of&nbsp;the&nbsp;framework targets __ESP8266__.
Support for&nbsp;other MicroPython‑compatible platforms (ESP32, RP2040)
is&nbsp;planned for&nbsp;subsequent development stages.

<a name="repository-structure"></a>
## Repository Structure

The repository is&nbsp;organized in&nbsp;accordance with
the&nbsp;[recommendations for&nbsp;Python packages](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

*   The&nbsp;[__examples__](examples/README.md) directory
	contains examples of&nbsp;using the&nbsp;framework modules.
*   The&nbsp;[__src__](src/README.md) directory
	contains the&nbsp;source code of&nbsp;the&nbsp;framework modules.
*   The&nbsp;[__CONTRIBUTORS.md__](CONTRIBUTORS.md) file
	lists the&nbsp;project contributors.
*   The&nbsp;[__README.md__](README.md) file
	you are&nbsp;reading now.

<a name="quick-start"></a>
## Getting Started

1.	Download the&nbsp;latest MicroPython firmware for&nbsp;ESP8266
	from the&nbsp;[official site](https://micropython.org/download/ESP8266_GENERIC/).
2.	Install the&nbsp;firmware on&nbsp;your device by&nbsp;following
	the&nbsp;[installation guide](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware).
3.	Install the&nbsp;SoCalled Robotics framework on&nbsp;your device.
	See the&nbsp;[modules source code description](src/README.md#installation).
4.	Use the&nbsp;[ready-made examples](examples/README.md#available-examples)
	as&nbsp;a&nbsp;starting point for&nbsp;your projects.

<a name="licenses"></a>
## Licenses

SoCalled Community uses open licenses for different types of&nbsp;materials:

*	__Source Code__ is&nbsp;distributed under
	the&nbsp;[__Mozilla Public License&nbsp;2.0 (MPL-2.0)__](https://socalled.link/community/LICENSE_MPL-2.0.md).
	This license requires that modifications to&nbsp;source code remain open,
	while allowing integration with proprietary software.
*	__Documentation and&nbsp;other creative materials__ (including this&nbsp;file)
	are&nbsp;distributed under
	the&nbsp;[__Creative Commons Attribution&nbsp;4.0 International (CC-BY-4.0)__](https://socalled.link/community/LICENSE_CC-BY-4.0.md).
	This license allows free use, distribution, and&nbsp;adaptation of&nbsp;materials
	with attribution requirement.

<a name="communication"></a>
## Communication

*	[__Community Chat__](https://t.me/SoCalledGroup)&nbsp;—
	for&nbsp;informal communication and assistance.
*	[__Blog__](https://t.me/SoCalledBlog)&nbsp;—
	announcements and&nbsp;news.
*	[__Task Tracker__](https://socalled.link/robotics-mpy/issues)&nbsp;—
	for&nbsp;technical discussions (preferred).
*	[__Email__](mailto:community@socalled.link)&nbsp;—
	for&nbsp;confidential questions.

📚&nbsp;[Learn more about communication principles in&nbsp;Code of&nbsp;Conduct](https://socalled.link/community/CODE_OF_CONDUCT.md)

---

_Copyright&nbsp;©&nbsp;2026 [SoCalled Robotics (MicroPython) Contributors](CONTRIBUTORS.md)._
_This document is&nbsp;licensed under the&nbsp;[Creative Commons Attribution&nbsp;4.0 International Public License](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
