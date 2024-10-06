# goit-algo-hw-03
## Тема 3. Рекурсивні функції, алгоритми та приклади їх застосування

Перед початком роботи:
1. Версія **Python: >=3.10**
2. Cтворюємо віртуальне середовище (Python: >=3.10) `.env`: `python -m venv .env`
3. Активуємо (відповідно до своєї ОС): `source .env/bin/activate`
4. Інсталюємо залежності: `pip install -r requirements.txt`
5. По завершенню роботи деактивовуємо: `deactivate`

## Завдання 1
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії 
та сортує в піддиректорії, назви яких базуються на розширенні файлів.

Також візьміть до уваги наступні умови:
1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: 
    - шлях до вихідної директорії;
    - шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
2. Рекурсивне читання директорій:
    - Має бути написана функція, яка приймає шлях до директорії як аргумент.
    - Функція має перебирати всі елементи у директорії.
    - Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
    - Якщо елемент є файлом, він має бути доступним для копіювання.
3. Копіювання файлів:
    - Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
    - Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.


### Критерії оцінювання:
1. Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою `dist`).
2. Рекурсивне читання директорій:
    - Написана функція, яка приймає шлях до директорії як аргумент.
    - Функція перебирає всі елементи у директорії.
    - Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
    - Якщо елемент є файлом, він є обробленим для копіювання.
3. Копіювання файлів:
    - Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
    - Файл з відповідним типом копіюється у відповідну піддиректорію.
4. Обробка винятків: код обробляє винятки, наприклад, помилки доступу до файлів або директорій.
5. Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову директорію та розсортовано в піддиректорії за їх розширенням.

### Ресурси
- [task1.py](./task1.py)
- [file_generator.py](./file_generator.py)
- [Module helpers](./helpers)

## Завдання 2
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
що користувач повинен мати можливість вказати рівень рекурсії.

### Критерії оцінювання:
1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».
2. Користувач має можливість вказати рівень рекурсії.

### Ресурси
- [task2.py](./task2.py)
- [Module helpers](./helpers)

## Завдання 3
Напишіть програму, яка виконує переміщення дисків з стрижня `А` на стрижень `С`, використовуючи стрижень `В` як допоміжний. 
Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.

Правила:
1. За один крок можна перемістити тільки один диск.
2. Диск можна класти тільки на більший диск або на порожній стрижень.

Вхідними даними програми має бути число `n` — кількість дисків на початковому стрижні. Вихідними даними — логування послідовності кроків для переміщення дисків зі стрижня `А` на стрижень `С`.

Наведемо приклад виконання коду для кількості дисків `n = 3`. На початковому стрижні вони розміщені так: `[3, 2, 1]`, де `3` — найбільший диск, а `1` — найменший.

```
Початковий стан: {'A': [3, 2, 1], 'B': [], 'C': []}
Перемістити диск з A на C: 1
Проміжний стан: {'A': [3, 2], 'B': [], 'C': [1]}
Перемістити диск з A на B: 2
Проміжний стан: {'A': [3], 'B': [2], 'C': [1]}
Перемістити диск з C на B: 1
Проміжний стан: {'A': [3], 'B': [2, 1], 'C': []}
Перемістити диск з A на C: 3
Проміжний стан: {'A': [], 'B': [2, 1], 'C': [3]}
Перемістити диск з B на A: 1
Проміжний стан: {'A': [1], 'B': [2], 'C': [3]}
Перемістити диск з B на C: 2
Проміжний стан: {'A': [1], 'B': [], 'C': [3, 2]}
Перемістити диск з A на C: 1
Проміжний стан: {'A': [], 'B': [], 'C': [3, 2, 1]}
Кінцевий стан: {'A': [], 'B': [], 'C': [3, 2, 1]}
```

### Ресурси
- [task3.py](./task3.py)
- [task3-gui.py](./task3-gui.py)
- [Module helpers](./helpers)


## Додатково
- [Домашнє завдання до теми “Рекурсивні функції, алгоритми та приклади їх застосування”](https://www.edu.goit.global/uk/learn/24858703/19646173/19646405/homework)
- [https://github.com/nickolas-z/goit-algo-hw-03](https://github.com/nickolas-z/goit-algo-hw-03)
- [goit-algo-hw-03-main.zip](https://s3.eu-north-1.amazonaws.com/lms.goit.files/e6bf9518-6bc3-43d3-8946-24ea44a0bd6b%D0%94%D0%973_%D0%97%D1%83%D0%B1%D1%87%D0%B8%D0%BA%D0%9C%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%9C%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9%D0%BE%D0%B2%D0%B8%D1%87.zip)
- [Basic-Algorithms-and-Data-Structures-Neoversity](https://github.com/nickolas-z/Basic-Algorithms-and-Data-Structures-Neoversity)