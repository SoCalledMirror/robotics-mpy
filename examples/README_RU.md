[EN](README.md) | __RU__

---

# Примеры SoCalled Robotics (MicroPython)

В&nbsp;этой директории собраны практические примеры,
демонстрирующие возможности [фреймворка SoCalled Robotics](../README_RU.md).

Каждый пример представлен отдельным файлом&nbsp;__.py__.
Примеры используют установленный пакет `socalled`
и&nbsp;могут быть запущены на&nbsp;целевых устройствах.

<a name="installation"></a>
## Установка

Перед&nbsp;запуском примеров [установите фреймворк](../src/README_RU.md#installation).
Директорию __examples__ на&nbsp;устройство переносить не&nbsp;требуется.

*	Для установки файла примера из&nbsp;сети используйте
	[пакетный менеджер](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote):

	```bash
	mpremote mip install --target / https://socalled.link/robotics-mpy/raw/main/examples/{имя_примера}.py
	```

	Флаг `--target` позволяет указать
	целевую директорию на&nbsp;устройстве
	(по&nbsp;умолчанию модули устанавливаются в&nbsp;__/lib__).
*	Для локальной установки из&nbsp;склонированного репозитория
	вручную скопируйте файл на&nbsp;устройство:

	```bash
	mpremote fs cp examples/{имя_примера}.py :
	```

	Чтобы пример исполнялся автоматически при&nbsp;запуске устройства,
	сохраните его в&nbsp;файл __main.py__:

	```bash
	mpremote fs cp examples/{имя_примера}.py :main.py
	```

<a name="available-examples"></a>
## Доступные примеры

Дополнительные инструкции по&nbsp;запуску и&nbsp;пояснения к&nbsp;коду
находятся в&nbsp;комментариях в&nbsp;файлах примеров.

### Blinking LED

[__blinking_led.py__](blinking_led.py)

Этот пример доментстрирует базовые принципы абстракции оборудования
за&nbsp;счёт использования обёрток фреймворка
для&nbsp;класса&nbsp;`machine.Pin` и&nbsp;метода&nbsp;`time.sleep`.
Он&nbsp;также содержит базовую обработку ошибок при&nbsp;инициализации оборудования.

__Ожидаемое поведение:__
Встроенный светодиод непрерывно мигает с&nbsp;1-секундным интервалом.

Логика встроенного светодиода ESP8266:

*	Пин&nbsp;2 соответствует светодиоду на&nbsp;плате.
*	Светодиод активен при&nbsp;низком сигнале:
	*	`led.value(0)` или&nbsp;`led.off()`&nbsp;→ светодиод __включён__;
	*	`led.value(1)` или&nbsp;`led.on()`&nbsp;→ светодиод __выключен__.

---

_Copyright&nbsp;©&nbsp;2026 [Участники проекта SoCalled Robotics (MicroPython)](../CONTRIBUTORS.md)._
_Этот документ предоставляется в&nbsp;соответствии с&nbsp;[Публичной лицензией Creative Commons с&nbsp;указанием авторства версии&nbsp;4.0 Международная](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
