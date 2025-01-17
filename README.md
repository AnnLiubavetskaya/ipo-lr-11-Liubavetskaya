# ipo-lr-11-Liubavetskaya
# Требования к практической части

---

<aside>
🚨

Какие же как в 11ой лабе

</aside>

# Общие задания

---

<aside>
🚨

Работа выполняется в репозитории 11 работы

</aside>

<aside>
🚨

Можно использовать любую библиотеку для GUI, я советую `DearPyGUI` 

</aside>

## Задание 1

Cоздать в репозитории новую ветку `gui` для выполнения заданий.

## Задание 2

Разработать графический пользовательский интерфейс место консольного в для [лр11](https://www.notion.so/11-Python-14b9f5faa7fd80d8a8e2fbcf7e7e3848?pvs=21) в файле `main_gui.py`   

---

## Требование к интерфейсу

### **1. Основные окна и их структура**

1. **Главное окно приложения**
    - **Части интерфейса:**
        - **Меню:**
            - "Экспорт результата” (смотреть задание 3) + проверка на наличие данных
            - "О программе" — Открывает модальное окна с номером лр, вариантом, и фио разработчика
        - **Рабочая область:**
            - Панель управления объектами (содержит кнопочки).
            - Таблицы данных (клиенты и транспортные средства).
        - **Статусная строка:**
            - Отображает текущие действия и сообщения об ошибках.
    - **Кнопки управления:**
        - "Добавить клиента", "Добавить транспорт", "Распределить грузы".
2. **Окно добавления/редактирования клиента**
    - **Части интерфейса:**
        - Поля для ввода данных клиента.
        - Кнопки: "Сохранить", "Отмена".
3. **Окно добавления/редактирования транспортного средства**
    - **Части интерфейса:**
        - Поля для ввода данных транспорта.
        - Кнопки: "Сохранить", "Отмена".

---

### **2. Поля для ввода данных и их валидация**

1. **Для клиента:**
    - Поле "Имя клиента" – обязательное, текстовое (валидация: только буквы, минимум 2 символа).
    - Поле "Вес груза" – обязательное, числовое (валидация: положительное число, не более 10000 кг).
    - Поле "VIP статус" – чекбокс (по умолчанию отключен).
2. **Для транспортного средства:**
    - Поле "Тип транспорта" – выпадающий список (варианты: "Грузовик", "Поезд").
    - и т.д. и т.п.
3. **Общее для всех форм:**
    - Валидация: при некорректном вводе появляется окно с предупреждением и очищается поле

---

### **3. Действия в интерфейсе**

1. **Добавление объекта:**
    - Клиента: открывается окно для заполнения данных и сохранения.
    - Транспортного средства: аналогично, с выбором типа транспорта.
2. **Редактирование объекта:**
    - По двойному щелчку на записи открывается окно редактирования.
3. **Удаление объекта:**
    - Выбор из таблицы и нажатие кнопки "Удалить".
4. **Оптимизация распределения грузов:**
    - Кнопка "Распределить грузы".
    - После выполнения отображается таблица с результатами.
5. **Сохранение и загрузка данных:**
    - Сохранение текущего состояния в файл.

---

### **4. Дополнительные рекомендации**

1. **Удобство работы:**
    - Использовать всплывающие подсказки (tooltip) для всех кнопок и полей.
    - Поддерживать возможность управления клавишами (например, Enter для подтверждения, Esc для отмены).
2. **Сообщения:**
    - Уведомления об успешных действиях (например, "Клиент добавлен").
    - Ошибки в модальном окне (например, "Грузоподъемность не может быть меньше 0").
3. **Отображение данных:**
    - Таблица клиентов: имя, вес груза, статус VIP.
    - Таблица транспортных средств: ID, тип, грузоподъемность, текущая загрузка.
    - Возможность сортировки и фильтрации по столбцам.
4. **Логика оптимизации:**
    - Отображение результата распределения грузов в отдельном модальном окне или в основной таблице.

---

## Задание 3

Добавить возможность сохранения результатов распределения грузов в файл (*формат на ваш выбор*).

Добавить кнопку в интерфейс для выполнения операции.

## Задание 4

Совершить слияние веток `main` и `gui`
