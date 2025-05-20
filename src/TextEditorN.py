from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']

def change_fonts(fontss):
    text_field['font'] = fonts[fontss]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()
        
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', 
                                         filetypes=(('Текстовые документы (txt)', '*.txt'),
                                                   ('Все файлы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        with open(file_path, encoding='utf-8') as f:
            text_field.insert('1.0', f.read())
        update_status_bar()

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (txt)', '*.txt'),
                                            ('Все файлы', '*.*')))
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            text = text_field.get('1.0', END)
            f.write(text)
        update_status_bar()

def find_text():
    search_window = Toplevel(root)
    search_window.title("Поиск текста")
    search_window.geometry("300x100")
    
    Label(search_window, text="Введите текст для поиска:").pack(pady=5)
    
    search_entry = Entry(search_window, width=30)
    search_entry.pack(pady=5)
    search_entry.focus_set()
    
    def search():
        
        text_field.tag_remove('found', '1.0', END)
        
        
        search_term = search_entry.get()
        
        if search_term:
            start_pos = '1.0'
            while True:
                
                start_pos = text_field.search(search_term, start_pos, stopindex=END)
                
                if not start_pos:
                    break
                    
               
                end_pos = f"{start_pos}+{len(search_term)}c"
                
                
                text_field.tag_add('found', start_pos, end_pos)
                
                
                start_pos = end_pos
            
            
            text_field.tag_config('found', background='yellow', foreground='black')
    
    Button(search_window, text="Найти", command=search).pack(pady=5)
    
    
    search_window.bind('<Return>', lambda event: search())

def update_status_bar(event=None):
    
    cursor_pos = text_field.index(INSERT)
    line, column = cursor_pos.split('.')
    
    
    total_lines = text_field.index('end-1c').split('.')[0]
    
    
    status_bar.config(text=f"Строка: {line}, Колонка: {column} | Всего строк: {total_lines}")


root = Tk()  
root.title('Текстовый редактор')
root.geometry('800x600')


main_menu = Menu(root)


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label='Сохранить', command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
main_menu.add_cascade(label='Файл', menu=file_menu)


edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Поиск', command=find_text, accelerator="Ctrl+F")
main_menu.add_cascade(label='Правка', menu=edit_menu)


view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)

view_menu_sub.add_command(label='Темная', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Calibri', command=lambda: change_fonts('Calibri'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)
main_menu.add_cascade(label='Вид', menu=view_menu)

root.config(menu=main_menu)


text_frame = Frame(root)
text_frame.pack(fill=BOTH, expand=1)


scroll_y = Scrollbar(text_frame)
scroll_y.pack(side=RIGHT, fill=Y)


scroll_x = Scrollbar(text_frame, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)


text_field = Text(text_frame,
                 yscrollcommand=scroll_y.set,
                 xscrollcommand=scroll_x.set,
                 wrap=NONE,
                 padx=10,
                 pady=10,
                 spacing3=10,
                 width=30,
                 font='Arial 14')
text_field.pack(expand=1, fill=BOTH)


scroll_y.config(command=text_field.yview)
scroll_x.config(command=text_field.xview)


status_bar = Label(root, text="Готово", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)


view_colors = {
    'dark': {
        'text_bg': 'black',
        'text_fg': 'lime',
        'cursor': 'brown',
        'select_bg': '#8d917a'
    },
    'light': {
        'text_bg': 'white',
        'text_fg': 'black',
        'cursor': '#A5A5A5',
        'select_bg': '#FAEEDD'
    }
}


fonts = {
    'Arial': {
        'font': 'Arial 14'
    },
    'Calibri': {
        'font': 'Calibri 14'
    },
    'TNR': {
        'font': ('Times New Roman', 14)
    }
}


change_theme('dark')


root.bind('<Control-o>', lambda e: open_file())
root.bind('<Control-s>', lambda e: save_file())
root.bind('<Control-f>', lambda e: find_text())


text_field.bind('<KeyRelease>', update_status_bar)
text_field.bind('<ButtonRelease>', update_status_bar)


update_status_bar()

root.mainloop()
