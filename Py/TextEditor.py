# Разработка текстового редактора.
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def chenge_theme(theme):
    text_fild['bg']=view_colors[theme]['text_bg']
    text_fild['fg']=view_colors[theme]['text_fg']
    text_fild['insertbackground']=view_colors[theme]['cursor']
    text_fild['selectbackground']=view_colors[theme]['select_bg']
def chenge_fonts(fontss):
    text_fild['font']=fonts[fontss]['font']
def notepad_exit():
    answer=messagebox.askokcancel('Quit','Are you sure?')
    if answer:
        root.destroy()
def open_file():
    file_path=filedialog.askopenfilename(title='choice file', filetypes=(('Text docs (*.txt)','*.txt'),('All files', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())
def save_file():
    file_path=filedialog.asksaveasfilename(filetypes=(('Text docs (*.txt)','*.txt'),('All files', '*.*')))
    f=open(file_path, 'w', encoding='utf-8')
    text=text_fild.get('1.0', END)
    f.write(text)
    f.close()
root=Tk()
root.title('Text editor')
root.geometry('600x700')
#root.iconbitmap('notepad.ico')
main_menu=Menu(root)
#File
file_menu=Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Close', command=notepad_exit)
#View
view_menu=Menu(main_menu, tearoff=0)
view_menu_sub=Menu(view_menu, tearoff=0)
font_menu_sub=Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Dark', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Light', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Theme', menu=view_menu_sub)
font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Rowan', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='font',menu=font_menu_sub)
root.config(menu=view_menu)
#Add lists menu
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
root.config(menu=main_menu)
f_text=Frame(root)
f_text.pack(fill=BOTH, expand=1)
text_fild=Text(f_text,
        bg='black',
        fg='lime',
        padx=10,
        pady=10,
        wrap=WORD,
        insertbackground='blue',
        selectbackground='white',
        spacing3=10,
        width=30,
        font='Arial 14 bold'
        )
view_colors={'dark':{'text_bg':'black',
            'text_fg':'lime',
            'cursor':'blue',
            'select_bg':'white'},
        'light':{
            'text_bg':'white',
            'text_fg':'black',
            'cursor':'blue',
            'select_bg':'black'}}
fonts={
        'Arial':{
                'font':'Arial 14 bold'
        },
        'CSMS':{
                'font':('Comic Sans MS', 14, 'bold')
        },
        'TNR':{
                'font':('Times New Roman', 14, 'bold')
        }
}
text_fild.pack(expand=1, fill=BOTH, side=LEFT)
scroll=Scrollbar(f_text,command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)
root.mainloop()
# https://www.youtube.com/playlist?list=PL9aGGxgLOVw44btcB1CM6j_jhrl7L95aH