# SPDX-FileCopyrightText: 2026 SoCalled Robotics Contributors <community@socalled.link>
# SPDX-License-Identifier: MPL-2.0

"""
Lazy-loading core package for SoCalled Robotics framework.
Optimizes memory usage by importing modules only when accessed.
"""

__version__ = '0.1.0'
__author__ = '2026 SoCalled Robotics Contributors <community@socalled.link>'

# Registry mapping public attribute names to their source modules.
# Format: {'attr_name': 'module_name'}
# - Keys: names users will type (e.g. 'Timer' or 'Pin')
# - Values: module to import (relative '.timer' or absolute 'machine')
# Used by __getattr__ for lazy-loading — keeps memory footprint low.
__attr_modules__ = {
    'Pin': 'machine',
    'sleep': 'time',
    'sleep_ms': 'time',
    'sleep_ns': 'time',
}

# Public API definition for static analysis tools.
# Automatically includes all registered lazy attributes.
__all__ = list(__attr_modules__.keys())

def __getattr__(attr_name):
    """
    Dynamically import and return an attribute on first access.

    Implements lazy loading to reduce initial memory footprint.
    Supports both absolute and relative module paths.

    Caching behaviour:
    - First call: imports the module, stores the attribute in globals().
    - Subsequent calls: returns the cached attribute instantly.
    - This eliminates repeated __import__ overhead for frequently used objects.
    """

    # CACHE CHECK: Return cached attribute if already imported.
    # This optimization prevents repeated imports, improving performance
    # for frequently accessed attributes.
    if attr_name in globals():
        # SAFETY: Prevent outside code from injecting attributes into globals()
        # Only attributes from __attr_modules__ are allowed
        if attr_name not in __attr_modules__:
            raise RuntimeError("Attribute '" + attr_name + "' was added outside __getattr__.")
        return globals()[attr_name]

    # Validate that the requested attribute is declared in the registry.
    if attr_name not in __attr_modules__:
        raise AttributeError("Module '" + __name__ + "' has no attribute '" + attr_name + "'.")

    module_name = __attr_modules__[attr_name]

    # Prevent relative imports beyond package level (e.g. '..module')
    if module_name.startswith('..'):
        raise ValueError("Relative import level too high: '" + module_name + "'.")

    # Handle relative imports (starting with '.') for intra-package modules.
    module_path = __name__ + module_name if module_name.startswith('.') else module_name

    try:
        # MicroPython does not include importlib; we use __import__ instead.
        module = __import__(module_path, globals(), locals(), [attr_name])

    except ImportError as import_error:
        raise ImportError("Cannot import '" + attr_name + "' from module '" + module_path + "'. ") from import_error

    try:
        # Extract the requested attribute from the imported module.
        attr = getattr(module, attr_name)

    except AttributeError as attribute_error:
        raise ImportError("Cannot import '" + attr_name + "' from module '" + module_path + "'. ") from attribute_error

    # CACHE STORE: Store attribute in globals for future access.
    # This eliminates the overhead of repeated __import__ calls and getattr lookups,
    # optimizing memory and CPU usage.
    globals()[attr_name] = attr
    return attr
