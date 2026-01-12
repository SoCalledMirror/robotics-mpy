__EN__ | [RU](README_RU.md)

---

# SoCalled Robotics (MicroPython) Source Code

This directory contains the&nbsp;source code
of&nbsp;the&nbsp;[SoCalled Robotics](../README.md) modules.
Each module is&nbsp;represented by&nbsp;a&nbsp;__.py__&nbsp;file
in&nbsp;the&nbsp;[__socalled__](socalled) directory
and&nbsp;is&nbsp;responsible for&nbsp;a&nbsp;specific functionality.

*	The [__\_\_init\_\_.py__](socalled/__init__.py) file performs several key functions:
	*	Defines which names will be&nbsp;available when importing `socalled`.
	*	Sets package metadata: `__version__`, `__author__`.
	*	Simplifies import syntax.

<a name="installation"></a>
## Installation

You can install the&nbsp;framework
on&nbsp;a&nbsp;MicroPython device in&nbsp;several ways.

<a name="installation-mip"></a>
### Using the&nbsp;mip package manager

This&nbsp;is the&nbsp;recommended method.
It&nbsp;automatically downloads all the&nbsp;framework modules
to&nbsp;the&nbsp;correct locations on&nbsp;the&nbsp;device using
the&nbsp;[MicroPython package manager](https://docs.micropython.org/en/latest/reference/packages.html).

To&nbsp;install the&nbsp;latest version from&nbsp;the&nbsp;main branch,
connect the&nbsp;device to&nbsp;your&nbsp;PC and&nbsp;run in&nbsp;your&nbsp;PC console:

```bash
mpremote mip install https://socalled.link/robotics-mpy/raw/main/package.json
```

To&nbsp;install from another branch, replace `main` in&nbsp;the&nbsp;link.

For&nbsp;local installation from&nbsp;a&nbsp;cloned repository,
run in&nbsp;the&nbsp;root directory of&nbsp;the&nbsp;repository:

```bash
mpremote mip install package.json
```

<a name="installation-manual"></a>
### Manual file copying

If&nbsp;you don't need all framework modules
and the&nbsp;available memory on&nbsp;the&nbsp;device is&nbsp;limited,
you can manually copy only the&nbsp;necessary module files.
To&nbsp;ensure they&nbsp;are&nbsp;correctly detected on&nbsp;importing,
place the&nbsp;__socalled__ directory in&nbsp;one of&nbsp;the&nbsp;paths
where MicroPython looks for&nbsp;modules:
in&nbsp;the&nbsp;root directory of&nbsp;the&nbsp;device's file system
or&nbsp;in&nbsp;the __/lib__ directory.

<a name="installation-verifying"></a>
### Verifying installation

After installation, verify it&nbsp;works
by&nbsp;running on&nbsp;the&nbsp;device:

```python
import socalled
print(socalled.__version__)
```

If&nbsp;you see the&nbsp;version output (e.g.,&nbsp;`0.1.0`),
the&nbsp;installation was&nbsp;likely successful.

<a name="installation-updating"></a>
### Updating

When new versions are&nbsp;released, simply repeat the&nbsp;installation process.
The&nbsp;new files will replace the&nbsp;existing ones.

<a name="using"></a>
## Using the&nbsp;modules

After installation, you can import the&nbsp;required modules
in&nbsp;one of&nbsp;the&nbsp;following ways:

*	Import the&nbsp;entire package and access modules via&nbsp;dot notation:

	```python
	import socalled
	from socalled.{module_name} import {ClassName}
	```

*	Direct import of a specific module,
 	if it is exported in [__\_\_init\_\_.py__](socalled/__init__.py):

	```python
	from socalled import {ClassName}
	```

---

_Copyright&nbsp;©&nbsp;2026 [SoCalled Robotics (MicroPython) Contributors](CONTRIBUTORS.md)._
_This document is&nbsp;licensed under the&nbsp;[Creative Commons Attribution&nbsp;4.0 International Public License](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
