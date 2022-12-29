# EN
# Final project - financier bot
____
### Description
This project is the last control project during studying in ITstep

The main task was to create a Telegram bot whose task is to store financial records.
The bot is able to receive records from user and to save them in a text file, clear this file and generate a report on all income/expenses
The following information is recorded in the file:
- ID - used when filtering records and deleting them
- Amount - is an indicator of the amount of money (how much was spent or added)
- Category - field just for the convenience of the user - he can enter any kind of necessary data there
- Date - an automatically created field in which the year-month-day of adding a record to the file is specified
____
### Structure
File **main.py** - contains all the logic of the program, connection to the bot, etc.

Image **task_board.png** - a board on which the scheme of the bot's logic is displayed

The **data_file** file is a text file that is used as a database. It records the data that the bot receives from the user

----
# UA
# Фінальний проект - бот-фінансист
____
### Опис
Даний проект є останнім контрольним проектом під час навчання в ITstep

Головним завданням було створити Telegram-бота, завданням якого є зберігання фінансових записів.
Бот вміє приймати записи та зберігати їх в текстовому файлі, очищати цей файл та формувати звіт по всіх доходах/розходах
В файл записується наступна інформація:
- ID - використовується при фільтруванні записів та їх видаленні
- Сума - є показником суми грошей (скільки їх витратилось чи додалось)
- Кетегорія - поле виключно для зручності користувача - він може вписувати туди довільні дані
- Дата - автоматично створюване поле в якому вказаний рік-місяць-день додання запису в файл
____
### Структура
Файл **main.py** - містить всю логіку програми, підключення до бота і т. д..

Зображення **task_board.png** - дошка на якій відображена схема роботи бота

Файл **data_file** - текстовий файл який використовується як база даних. В нього ведеться запис даних які бот приймає у користувача