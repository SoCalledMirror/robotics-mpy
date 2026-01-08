[EN](CONTRIBUTING.md) | __RU__

---

# Руководство по&nbsp;участию в&nbsp;проекте SoCalled Robotics (MicroPython)

Благодарим за&nbsp;интерес к&nbsp;развитию проекта
[SoCalled Robotics (MicroPython)](README_RU.md)!

⚠️ Сначала ознакомьтесь
с&nbsp;[общим руководством по участию в&nbsp;сообществе SoCalled](https://socalled.link/community/CONTRIBUTING_RU.md).
В&nbsp;нём описаны ключевые процессы, работа с&nbsp;задачами и&nbsp;Git,
требования к&nbsp;коммитам и&nbsp;DCO, а&nbsp;также другие способы участия.

Этот документ устанавливает специфичные для&nbsp;фреймворка
правила стиля, архитектуры, документирования и&nbsp;оформления.

## Содержание

*	[Как начать работу](#quick-start)
*	[Архитектурные принципы](#architecture)
	*	[Абстракция оборудования](#hardware-abstraction)
	*	[Ленивая инициализация](#lazy-init)
	*	[Потокобезопасность](#thread-safety)
	*	[Эффективность](#efficiency)
	*	[Устойчивость](#stability)
	*	[Проверка на&nbsp;примерах](#examples)
*	[Стиль кода](#code-style)
	*	[Соглашения по&nbsp;именованию](#code-naming)
	*	[Форматирование](#code-formatting)
	*	[Импорты](#code-imports)
	*	[Константы и&nbsp;«магические числа»](#code-constants)
*	[Документирование кода](#code-documentation)
	*	[Строки документации](#docstrings)
	*	[Архитектурные комментарии](#arch-comments)
*	[Метки задач](#labels)
*	[Процесс разработки](#development-process)
*	[Лицензии и&nbsp;авторские права](#licensing)

<a name="quick-start"></a>
## Как начать работу

Чтобы приступить к&nbsp;разработке:

1.	Изучите [трекер задач](https://socalled.link/robotics-mpy/issues).
2.	Найдите любую открытую задачу (например, с&nbsp;меткой __Good First Issue__).
3.	Оставьте комментарий о&nbsp;готовности над ней поработать.
4.	После согласования с&nbsp;мейнтейнерами приступайте к&nbsp;работе,
	следуя [общим](https://socalled.link/community/CONTRIBUTING_RU.md)
	и&nbsp;правилам из&nbsp;этого документа.

<a name="architecture"></a>
## Архитектурные принципы

Код должен соответствовать [принципам проектирования](README_RU.md#design-principles).
Для этого используются следующие подходы:

<a name="hardware-abstraction"></a>
### Абстракция оборудования

Используйте стандартные классы `machine` (`Pin`, `PWM`).
Где это уместно, переиспользуйте и&nbsp;расширяйте существующие классы фреймворка.

<a name="lazy-init"></a>
### Ленивая инициализация

Ресурсы (память, таймеры, пины) выделяйте при&nbsp;первом использовании
и&nbsp;освобождайте, как только они перестают быть нужными.

<a name="thread-safety"></a>
### Потокобезопасность

Обеспечивайте консистентность данных и&nbsp;последовательность операций,
когда код может выполняться в&nbsp;контексте прерываний.
Для&nbsp;работы с&nbsp;разделяемыми данными используйте:
	
```python
machine.disable_irq()
# безопасный код здесь
machine.enable_irq()
```

<a name="efficiency"></a>
### Эффективность

В&nbsp;критичных по&nbsp;производительности или&nbsp;памяти участках кода
(обработчики прерываний, частые колбэки)
избегайте конструкций, создающих излишнюю нагрузку,
например, f-строк (`f"..."`).
Отдавайте предпочтение конкатенации строк или&nbsp;заранее подготовленным шаблонам.

<a name="stability"></a>
### Устойчивость

Код должен быть рассчитан на&nbsp;возможные сбои.

*	При&nbsp;работе с&nbsp;оборудованием всегда оборачивайте операции
в&nbsp;`try`/`except` для&nbsp;обработки возможных сбоев.
*	Используйте встроенные исключения Python
	(`ValueError`, `TypeError`, `OSError` и&nbsp;др.) для&nbsp;стандартных случаев.
*	Избегайте «голых» `except`, указывайте конкретные типы исключений.

<a name="examples"></a>
### Проверка на&nbsp;примерах

Вся добавленная логика должна быть проверена.
Создавайте или&nbsp;обновляйте примеры для&nbsp;демонстрации работы новых функций.
Перед отправкой запроса на&nbsp;слияние __обязательно__ убедитесь,
что примеры выполняются на&nbsp;целевых устройствах.

<a name="code-style"></a>
## Стиль кода

Соблюдение единого стиля кода повышает читаемость,
упрощает совместную работу и&nbsp;поддержку проекта.

<a name="code-naming"></a>
### Соглашения по&nbsp;именованию

Используйте следующие стили для&nbsp;разных элементов кода:

| Элемент кода       | Стиль              | Примеры
|:--                 |:--                 |:--
| Файлы модулей      | __snake_case__     | __socalled/timer.py__, __socalled/event_loop.py__
| Классы             | `CamelCase`        | `EventLoop`, `ServoController`
| Функции и методы   | `snake_case`       | `async_sleep_ms()`, `read()`
| Константы          | `UPPER_SNAKE_CASE` | `MAX_DISTANCE_CM`
| Приватные атрибуты | `_snake_case`      | `_events`, `_sleep_time_ms`

Для переменных и&nbsp;аргументов, представляющих физические величины,
добавляйте суффикс с&nbsp;единицами измерений, например, `timeout_ms`, `distance_cm`.
Это улучшает ясность кода и&nbsp;помогает избежать ошибок.

<a name="code-formatting"></a>
### Форматирование

*	__Отступы.__  
	4 пробела на&nbsp;уровень.
*	__Длина строки.__  
	Cтарайтесь укладываться в&nbsp;79&nbsp;символов.
	Допускается до&nbsp;120&nbsp;символов, если это позволит улучшить читаемость.
*	__Пробелы__.  
	Операторы окружаются пробелами (`a = b + 1`).
	После запятых при&nbsp;перечислении элементов ставится пробел.

<a name="code-imports"></a>
### Импорты

*	Последовательность:
	1.	Стандартные библиотеки Python.
	2.	Библиотеки MicroPython.
	3.	Модули проекта (`socalled`).
*	Внутри каждой группы&nbsp;— в&nbsp;алфавитном порядке.
*	Используйте абсолютные импорты.
*	Всегда импортируйте модули и&nbsp;классы явно.
	Запрещено использовать импорт через звёздочку (`*`):
	
	```python
	from socalled import Timer
	```

<a name="code-constants"></a>
### Константы и&nbsp;«магические числа»

Выносите в&nbsp;именованные константы (`UPPER_SNAKE_CASE`)
в&nbsp;начале модуля или в&nbsp;классах
все числовые или&nbsp;строковые литералы с&nbsp;неочевидным значением,
например, тайминги, коды ошибок, размеры буферов и&nbsp;калибровочные коэффициенты.

<a name="code-documentation"></a>
## Документирование кода

Понятные комментарии и&nbsp;документация существенно упрощают понимание кода,
его использование и&nbsp;развитие.

<a name="docstrings"></a>
### Строки документации

Используйте __Google-style docstrings__ на&nbsp;английском языке
для&nbsp;всех публичных модулей, классов, функций и&nbsp;методов.

Обязательные элементы документирования метода или функции:

*	Краткое описание назначения.
*	__Args__&nbsp;— список аргументов с&nbsp;указанием типа и&nbsp;назначения.
*	__Returns__&nbsp;— описание возвращаемого значения, включая тип.
*	__Raises__&nbsp;— перечень исключений, которые могут быть вызваны, с&nbsp;условиями.

Пример:

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
### Архитектурные комментарии

Значимые архитектурные решения, особенно те, что касаются
оптимизации памяти, энергопотребления или&nbsp;потокобезопасности,
должны быть прокомментированы в&nbsp;коде. 

*	Используйте комментарии для&nbsp;объяснения неочевидных решений или&nbsp;сложной логики.
*	Объясняйте _почему_ выбрана именно такая реализация, если это неочевидно.
*	Избегайте комментариев, которые просто дублируют код.
*	Располагайте комментарий над объясняемым блоком, начиная с&nbsp;заглавной буквы.

Пример:

```python
# Using list instead of dict to save memory per event (~16 bytes)
# Format: [handler, timestamp_ms, period_ms]
self._events = []
```

<a name="labels"></a>
## Метки задач

Для&nbsp;категоризации задач используются
[общие метки сообщества](https://socalled.link/community/CONTRIBUTING_RU.md#labels),
а&nbsp;также собственные метки проекта для&nbsp;компонентов.
Их&nbsp;рекомендуется указывать в&nbsp;заголовках коммитов
в&nbsp;квадратных скобках для&nbsp;обозначения области изменений
(например, `[sensors] Add calibration methods...`).

| Метка             | Назначение              | Примеры компонентов
|:--                |:--                      |:--
| __Actuators__     | Управление приводами    | __socalled/servo.py__, __socalled/servo_controller.py__
| __Core__          | Изменения в&nbsp;ядре   | __socalled/timer.py__, __socalled/event_loop.py__
| __Documentation__ | Документация            | __README_RU.md__, __doc/*__
| __Examples__      | Примеры использования   | __examples/brightness_controller.py__
| __Input__         | Обработка ввода         | __socalled/button.py__
| __Sensors__       | Работа с&nbsp;датчиками | __socalled/digital_sensor__, __socalled/hcsr04_sensor__

<a name="licensing"></a>
## Лицензии и&nbsp;авторские права

__Исходный код__ распространяется под&nbsp;лицензией
__[Mozilla Public License&nbsp;2.0 (MPL-2.0)](https://socalled.link/community/LICENSE_MPL-2.0.md)__.
В&nbsp;начало каждого файла с&nbsp;исходниками добавьте комментарий с&nbsp;SPDX-заголовком
(при&nbsp;необходимости скорректировав формат комментариев и&nbsp;год на&nbsp;актуальный):

```python
# SPDX-FileCopyrightText: 2026 SoCalled Robotics Contributors <community@socalled.link>
# SPDX-License-Identifier: MPL-2.0
```

__Документация и&nbsp;другие творческие материалы__ (включая этот файл)
распространяются под&nbsp;лицензией
__[Creative Commons Attribution&nbsp;4.0 International (CC-BY-4.0)](https://socalled.link/community/LICENSE_CC-BY-4.0.md)__.
В&nbsp;конце каждого файла документации добавляйте следующий комментарий
(при&nbsp;необходимости скорректировав формат и&nbsp;год на&nbsp;актуальный):

```markdown
---

_Copyright&nbsp;©&nbsp;2026 [Участники проекта SoCalled Robotics (MicroPython)](CONTRIBUTORS.md)._
_Этот документ предоставляется в&nbsp;соответствии с&nbsp;[Публичной лицензией Creative Commons с&nbsp;указанием авторства версии&nbsp;4.0 Международная](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
```

---

_Copyright&nbsp;©&nbsp;2026 [Участники проекта SoCalled Robotics (MicroPython)](CONTRIBUTORS.md)._
_Этот документ предоставляется в&nbsp;соответствии с&nbsp;[Публичной лицензией Creative Commons с&nbsp;указанием авторства версии&nbsp;4.0 Международная](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
