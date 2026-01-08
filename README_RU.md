[EN](README.md) | __RU__

---

# SoCalled Robotics (MicroPython)

__Лёгкий, событийно-ориентированный фреймворк
для&nbsp;робототехники и&nbsp;IoT на&nbsp;MicroPython.__

[Начать](#quick-start) •
[Участвовать](CONTRIBUTING_RU.md) •
[Чат](https://t.me/SoCalledGroup) •
[Блог](https://t.me/SoCalledBlog) •
[Задачи](https://socalled.link/robotics-mpy/issues)

__SoCalled Robotics__&nbsp;— это открытый фреймворк
для&nbsp;создания робототехнических и&nbsp;IoT-приложений для&nbsp;микроконтроллеров.
Он&nbsp;предоставляет готовые, оптимизированные компоненты
для&nbsp;работы с&nbsp;оборудованием, таймерами, событиями и&nbsp;периферией,
позволяя вам сосредоточиться на&nbsp;логике приложения, а&nbsp;не&nbsp;на&nbsp;низкоуровневых деталях.

Проект развивается открыто
в&nbsp;[сообществе SoCalled](https://socalled.link/community)&nbsp;— сообществе единомышленников,
разделяющих общие [ценности](https://socalled.link/community/README_RU.md#values)
и&nbsp;[принципы](https://socalled.link/community/README_RU.md#principles).

📚&nbsp;[Подробнее о&nbsp;процессах в&nbsp;Руководстве по&nbsp;участию](CONTRIBUTING_RU.md)

<a name="vision"></a>
## Наше видение

Проект создаёт экосистему для&nbsp;лёгкой интеграции различных устройств.
Мы&nbsp;постепенно исследуем и&nbsp;реализуем возможности микроконтроллеров,
MicroPython и&nbsp;подключаемой периферии, строя библиотеку компонентов,
которые работают вместе «из&nbsp;коробки».
Долгосрочная цель&nbsp;— создание согласованной экосистемы,
где компоненты на&nbsp;MicroPython будут совместимы
с&nbsp;реализацией на&nbsp;C++ для&nbsp;AVR и&nbsp;других платформ.

<a name="design-principles"></a>
## Принципы проектирования

Фреймворк построен вокруг основных принципов, определяющих его архитектуру:

*	__Абстракция оборудования.__  
	Единообразный API для&nbsp;различных платформ микроконтроллеров,
	упрощающий портирование и&nbsp;разработку.
*	__Эффективность памяти.__  
	Оптимизирован для&nbsp;устройств с&nbsp;ограниченной RAM/ROM
	за&nbsp;счёт использования синглтонов и&nbsp;эффективных структур данных.
*	__Энергоэффективность.__  
	Интеллектуальный сон между событиями
	и&nbsp;задачи с&nbsp;низким энергопотреблением
	для&nbsp;увеличения времени автономной работы.
*	__Потокобезопасность.__  
	Атомарные операции и&nbsp;защита от&nbsp;реентерабельности
	для&nbsp;надёжной работы в&nbsp;асинхронных сценариях.
*	__Расширяемость.__  
	Простота добавления новых компонентов
	при&nbsp;сохранении архитектурной согласованности.
*	__Совместимость API.__  
	Максимально возможная совместимость по&nbsp;API с&nbsp;реализацией фреймворка
	для&nbsp;других языков программирования.
*   __Связность компонентов.__  
	Компоненты спроектированы для&nbsp;лёгкой интеграции в&nbsp;распределённые системы, 
	где устройства на&nbsp;разных языках и&nbsp;платформах могут работать согласованно.

<a name="target-platforms"></a>
## Целевые платформы

Первая версия фреймворка предназначена для&nbsp;__ESP8266__.
Поддержка других платформ, совместимых с&nbsp;MicroPython, (ESP32, RP2040)
запланирована в&nbsp;следующих этапах развития.

<a name="repository-structure"></a>
## Структура репозитория

Репозиторий организован в&nbsp;соответствии
с&nbsp;[рекомендациями для&nbsp;Python-пакетов](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

*	Директория [__examples__](examples/README_RU.md)
	содержит примеры использования модулей фреймворка.
*	Директория [__src__](src/README_RU.md)
	содержит исходный код модулей фреймворка.
*	Файл [__CONTRIBUTORS.md__](CONTRIBUTORS.md)
	содержит список участников проекта.
*	Файл [__README_RU.md__](README_RU.md)
	Вы&nbsp;читаете сейчас
	(является переводом файла [__README.md__](README.md)).

<a name="quick-start"></a>
## Начало работы

1.	Загрузите последнюю прошивку MicroPython для&nbsp;ESP8266
	с&nbsp;[официального сайта](https://micropython.org/download/ESP8266_GENERIC/).
2.	Установите прошивку на&nbsp;устройство, следуя
	[руководству по установке](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware).
3.	Установите фреймворк SoCalled Robotics на&nbsp;устройство.
	См.&nbsp;[описание исходного кода модулей](src/README_RU.md#installation).
4.	Используйте [готовые примеры](examples/README_RU.md#available-examples)
	как отправную точку для&nbsp;проектов.

<a name="licenses"></a>
## Лицензии

Сообщество SoCalled использует открытые лицензии
для&nbsp;разных типов материалов:

*	__Исходный код__ распространяется под&nbsp;лицензией
	[__Mozilla Public License&nbsp;2.0 (MPL-2.0)__](https://socalled.link/community/LICENSE_MPL-2.0.md).
	Эта лицензия требует,
	чтобы модификации исходного кода оставались открытыми,
	при&nbsp;этом позволяя интегрировать код
	с&nbsp;проприетарным программным обеспечением.
*	__Документация и&nbsp;другие творческие материалы__ (включая этот файл)
	распространяются под&nbsp;лицензией
	[__Creative Commons Attribution&nbsp;4.0 International (CC-BY-4.0)__](https://socalled.link/community/LICENSE_CC-BY-4.0.md).
	Эта лицензия позволяет свободно использовать,
	распространять и&nbsp;адаптировать материалы
	при&nbsp;условии указания авторства.

<a name="communication"></a>
## Коммуникация

*	[__Чат сообщества__](https://t.me/SoCalledGroup)&nbsp;—
	для&nbsp;неформального общения и&nbsp;помощи.
*	[__Блог__](https://t.me/SoCalledBlog)&nbsp;—
	анонсы и&nbsp;новости.
*	[__Трекер задач__](https://socalled.link/robotics-mpy/issues)&nbsp;—
	для&nbsp;технических обсуждений (предпочтительно).
*	[__Почта__](mailto:community@socalled.link)&nbsp;—
	для&nbsp;конфиденциальных вопросов.

📚&nbsp;[Подробнее о&nbsp;принципах коммуникаций в&nbsp;Кодексе поведения](https://socalled.link/community/CODE_OF_CONDUCT_RU.md)

---

_Copyright&nbsp;©&nbsp;2026 [Участники проекта SoCalled Robotics (MicroPython)](CONTRIBUTORS.md)._
_Этот документ предоставляется в&nbsp;соответствии с&nbsp;[Публичной лицензией Creative Commons с&nbsp;указанием авторства версии&nbsp;4.0 Международная](https://socalled.link/community/LICENSE_CC-BY-4.0.md)._
