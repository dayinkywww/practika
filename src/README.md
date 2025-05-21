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
Блок-схема для текстового редактора [diagram.png](diagram.png)
1. Создание основного окна
   &nbsp;from tkinter import *
   
   &nbsp;root = Tk()
   &nbsp;root.title('Текстовый редактор')
   &nbsp;root.geometry('600x700')

2. Добавление текстового поля
   &nbsp;text_fild = Text(root, bg='black', fg='lime',padx=10, pady=10,wrap=WORD)
   
   &nbsp;text_fild.pack(expand=1, fill=BOTH)
   
4. Реализация меню
   &nbsp;main_menu = Menu(root)
   
   
   &nbsp;file_menu = Menu(main_menu, tearoff=0)
   
   &nbsp;file_menu.add_command(label='Открыть', command=open_file)
   
   &nbsp;file_menu.add_command(label='Сохранить', command=save_file)
   
   &nbsp;main_menu.add_cascade(label='Файл', menu=file_menu)
   

   &nbsp;root.config(menu=main_menu)
   
6. Функции для работы с файлами
   &nbsp;def open_file():
   
   &nbsp;file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (txt)','*.txt'),))
   
   &nbsp;if file_path:
   
   &nbsp;text_fild.delete('1.0',END)
   
   &nbsp;text_fild.insert('1.0', open(file_path, encoding='utf-8').read())
   
   &nbsp; def save_file():
   
   &nbsp;file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (txt)','*.txt'),))
   
   &nbsp;if file_path:
   
   &nbsp; with open(file_path,'w', encoding='utf-8') as f:
   
   &nbsp;&nbspf.write(text_fild.get('1.0', END))
   
8. Реализация тем оформления
   &nbsp;view_colors = {
   
   &nbsp;'dark': {'text_bg':'black', 'text_fg':'lime', 'cursor':'brown'},
   
   &nbsp;'light': {'text_bg':'white', 'text_fg':'black', 'cursor':'#A5A5A' }
   
   &nbsp;}
   
   &nbsp; def change_theme(theme):
   
   &nbsp;text_fild['bg'] = view_colors[theme]['text_bg']
   
   &nbsp;text_fild['fg'] = view_colors[theme]['text_fg']
   
10. Добавление прокрутки
   &nbsp;scroll = Scrollbar(text_fild, command=text_fild.yview)

   &nbsp;scroll.pack(side=RIGHT, fill=Y)
   
   &nbsp;text_fild.config(yscrollcommand=scroll.set)
   
## Модификация проекта
Текстовый редактор имеет базовый функционал, но его можно улучшить.
1. Можно создать удобное и просто окно для поиска текста(**Пример кода**):
   def find_text():

    search_window = Toplevel(root)
    
    Entry(search_window).pack()
    
    Button(search_window, text="Найти", command=lambda: search(...)).pack()

3. Также можно добавить сочетания клавиш для более удобной работы с редактором(**Пример кода**):
   root.bind('<Control-o>', lambda e: open_file())
   
   root.bind('<Control-s>', lambda e: save_file())
    

## Заключение
Данный текстовый редактор предоставляет базовый функционал для работы с текстовыми файлами. В репозитории находятся два файла [TextEditor.py](TextEditor.py)- базовый текстовый редактор и [TextEditorN.py](TextEditorN.py) - модифицированный текстовый редактор.
   

  
