[EN](README.md) | __RU__

---

# Исходный код SoCalled Robotics (MicroPython)

Эта директория содержит исходный код
модулей [SoCalled Robotics](../README_RU.md).
Каждый модуль представлен файлом&nbsp;__.py__
в&nbsp;директории [__socalled__](socalled)
и&nbsp;отвечает за&nbsp;определенную функциональность.

*	Файл [__\_\_init\_\_.py__](socalled/__init__.py) выполняет несколько ключевых функций:
	*   Определяет, какие имена будут доступны при импорте `socalled`.
	*   Задает метаданные пакета: `__version__`, `__author__`.
	*   Упрощает синтаксис импорта.

<a name="installation"></a>
## Установка

Вы&nbsp;можете несколькими способами установить фреймворк
на&nbsp;устройство с&nbsp;MicroPython.

<a name="installation-mip"></a>
### Использование пакетного менеджера mip

Это рекомендованный способ.
Он&nbsp;автоматически загружает все модули фреймворка
в&nbsp;правильные места на&nbsp;устройстве с&nbsp;помощью
[пакетного менеджера MicroPython](https://docs.micropython.org/en/latest/reference/packages.html).

Для установки последней версии из&nbsp;основной ветки
подключите устройство к&nbsp;ПК и&nbsp;выполните в&nbsp;консоли&nbsp;ПК:

```bash
mpremote mip install https://socalled.link/robotics-mpy/raw/main/package.json
```

Для установки из&nbsp;другой ветки замените `main` в&nbsp;ссылке.

Для локальной установки из&nbsp;склонированного репозитория
выполните в&nbsp;корне директории репозитория:

```bash
mpremote mip install package.json
```

<a name="installation-manual"></a>
### Ручное копирование файлов

Если Вам требуются не&nbsp;все модули фреймворка,
а&nbsp;доступная память на&nbsp;устройстве ограничена,
можете вручную скопировать файлы только нужных модулей.
Для того, чтобы они корректно определялись при&nbsp;импорте,
разместите директорию __socalled__ по&nbsp;одному из&nbsp;путей,
где&nbsp;MicroPython ищет модули:
в&nbsp;корневой директории файловой системы устройства
или в&nbsp;директории&nbsp;__/lib__.

<a name="installation-verifying"></a>
### Проверка установки

После установки проверьте работоспособность,
выполнив на&nbsp;устройстве:

```python
import socalled
print(socalled.__version__)
```

Если Вы&nbsp;видите вывод версии (например,&nbsp;`0.1.0`),
установка, скорее всего, прошла успешно.

<a name="installation-updating"></a>
### Обновление

При&nbsp;выходе новых версий достаточно повторить установку,
новые файлы заменят существующие.

<a name="using"></a>
## Использование модулей

После установки Вы&nbsp;можете импортировать нужные модули
одним из&nbsp;способов:

*	Импорт всего пакета и&nbsp;доступ к&nbsp;модулям через точку:

	```python
	import socalled
	from socalled.{имя_модуля} import {ИмяКласса}
	```

*	Прямой импорт конкретного модуля,
	если он&nbsp;экспортирован в&nbsp;[__\_\_init\_\_.py__](socalled/__init__.py):

	```python
	from socalled import {ИмяКласса}
	```

---

_Copyright&nbsp;©&nbsp;2026 [Участники проекта SoCalled Robotics (MicroPython)](../CONTRIBUTORS.md)._
_Этот документ предоставляется в&nbsp;соответствии с&nbsp;[Публичной лицензией Creative Commons с&nbsp;указанием авторства версии&nbsp;4.0 Международная](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
