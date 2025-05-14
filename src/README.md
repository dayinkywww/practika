# Техническое руководство по созданию текстового редактора на языке программирования Python c библиотекой tkinter

## Исследование предметной части
### Цели исследования
1. Анализ существующих текстовых редакторов
2. Определение базового функционала
3. Изучение библиотеки Tkinter для реализации GUI

### Результаты исследования
Были выявлены ключевые компоненты текстового редактора:
* Работа с файлами (открытие/сохранение)
* Настройки внешнего вида (темы, шрифты)
* Базовое текстовое поле с прокруткой

## Техническое руководство
### Требования
1. Python 3.6+
2. Библиотека Tkinter (обычно входит в стандартную поставку Python)

### Установка
1. Убедитесь, что Python установлен:
   * Windows: написать в командной строке *python --version*
   * macOS: написать в терминале *python -version*
   * Linux: написать в терминале *python -version*
2. Дополнительные установки не требуются, так как Tkinter входит в стандартную библиотеку.

### Пошаговая реализаций

1. Создание основного окна
   >from tkinter import *
   
   >root = Tk()
   >root.title('Текстовый редактор')
   >root.geometry('600x700')

2. Добавление текстового поля
   >text_fild = Text(root, bg='black', fg='lime',padx=10, pady=10,wrap=WORD)
   >text_fild.pack(expand=1, fill=BOTH)
3. Реализация меню
   >main_menu = Menu(root)
   
   >file_menu = Menu(main_menu, tearoff=0)
   >file_menu.add_command(label='Открыть', command=open_file)
   >file_menu.add_command(label='Сохранить', command=save_file)
   >main_menu.add_cascade(label='Файл', menu=file_menu)

   >root.config(menu=main_menu)
4. Функции для работы с файлами
   >def open_file():
    >file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (txt)','*.txt'),))
    >if file_path:
        >text_fild.delete('1.0',END)
        >text_fild.insert('1.0', open(file_path, encoding='utf-8').read())
   >def save_file():
    >file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (txt)','*.txt'),))
    >if file_path:
        >with open(file_path,'w', encoding='utf-8') as f:
            >f.write(text_fild.get('1.0', END))
 5. Реализация тем оформления
    >view_colors = {
        >'dark': {'text_bg':'black', 'text_fg':'lime', 'cursor':'brown'},
        >'light': {'text_bg':'white', 'text_fg':'black', 'cursor':'#A5A5A' }
    >}
    >def change_theme(theme):
        >text_fild['bg'] = view_colors[theme]['text_bg']
        >text_fild['fg'] = view_colors[theme]['text_fg']
6. Добавление прокрутки
   >scroll = Scrollbar(text_fild, command=text_fild.yview)
   >scroll.pack(side=RIGHT, fill=Y)
   >text_fild.config(yscrollcommand=scroll.set)
## Модификация проекта


## Заключение
Данный текстовый редактор предоставляет базовый функционал для работы с текстовыми файлами и может быть легко расширен. Код доступен /TextEditor.py
   

  
