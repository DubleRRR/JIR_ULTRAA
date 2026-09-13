#from tkinter import *
import customtkinter as ctk #Подключил библиотеки

#Окно
root = ctk.CTk()
root.title('Калькулятор эхолокации')
root.geometry('720x480')
root.resizable(width=False, height=False)

# Arial Black сделает надписи очень плотными, толстыми и современными
#FONT_MAIN = ctk.CTkFont(family="Arial Black", size=13)

# Trebuchet MS сделает маленькие надписи и результаты более округлыми и мягкими
#FONT_SMALL = ctk.CTkFont(family="Trebuchet MS", size=12, weight="bold")
#FONT_RESULT = ctk.CTkFont(family="Trebuchet MS", size=15, weight="bold")

block = ctk.CTkFrame(root, width=380, height=450, border_width=1, border_color='#CBD5E1', fg_color='#F0F4F8')
block.grid_propagate(False)
block.place(x=15, y=15)

block1 = ctk.CTkFrame(block, width=350, height=120, border_width=1, border_color='#CBD5E1', fg_color='#E2E8F0')
block1.grid_propagate(False)
block1.place(x=15, y=265)

block2 = ctk.CTkFrame(block, width=350, height=4, fg_color='#E2E8F0')
block2.grid_propagate(False)
block2.place(x=15, y=242)

label1 = ctk.CTkLabel(block, text='Среда', text_color='#475569', font=("Trebuchet MS" 'bold', 14))
label1.grid(row=0, column=0, pady=5, padx=15, sticky='w')

label2 = ctk.CTkLabel(block, text='Температура воздуха', text_color='#475569', font=("Comic Sans MC", 14))
label2.grid(row=3, column=0, pady=5, padx=45, sticky='w')

label3 = ctk.CTkLabel(block, text='Время распространения сигнала', text_color='#475569', font=("Comic Sans MC", 14))
label3.grid(row=5, column=0, pady=5, padx=45, sticky='w')

label4 = ctk.CTkLabel(block1, text='Параметры воды', text_color='#475569', font=("Comic Sans MC", 14))
label4.grid(row=0, column=0, pady=(10,0), padx=17, sticky='w')

label5 = ctk.CTkLabel(block1, text='Солёность', text_color='#475569', font=("Comic Sans MC", 12))
label5.grid(row=1, column=0, pady=(6,0), padx=17, sticky='w')

label6 = ctk.CTkLabel(block1, text='Давление', text_color='#475569', font=("Comic Sans MC", 12))
label6.grid(row=1, pady=(6,0), padx=183, sticky='w')

#ctk.set_appearance_mode("Light")
#root.configure(fg_color="#F0F4F8")

#root['bg'] = '#3A92FF' - Цвет фона

#Поля ввода, которые появляются ток с водой
solenost = ctk.CTkEntry(block1, placeholder_text='', width=150, height=30, border_width=1, border_color='#CBD5E1') #Переменная солёности
solenost.grid(row=2, column=0, pady=0, padx=17, sticky='w')

davlenie = ctk.CTkEntry(block1, placeholder_text='', width=150, height=30, border_width=1, border_color='#CBD5E1') #Переменная давления/глубины
davlenie.grid(row=2, pady=0, padx=183, sticky='w')

def environment_changed(choise): #Чойс - то же говно, что и энвироментс которое можно называть как угодно. Чанджед реагирует, когда переменая перед '_' изменяется
    if choise == 'Вода': #С водой проявляет поля
        solenost.configure(state="normal")
        davlenie.configure(state="normal")
        label4.configure(text_color='#475569')
        label5.configure(text_color='#475569')
        label6.configure(text_color='#475569')
    elif choise == 'Воздух': #С воздухом прячет
        solenost.delete(0, 50)
        davlenie.delete(0, 50)
        solenost.configure(state="disabled")
        davlenie.configure(state="disabled")
        label4.configure(text_color='gray')
        label5.configure(text_color='gray')
        label6.configure(text_color='gray')

environments = ['Воздух', 'Вода'] #Энвироментс - параша, название переменной, именую как хочу. Список - это квадратные скобки
environment = ctk.CTkComboBox(block, #Комбобокс - лист-выпадашка
                              values=environments, #Валуес - слова в выпадашке
                              command=environment_changed, height=36, width=350, border_width=1, border_color='#CBD5E1', button_color='#CBD5E1', button_hover_color="#0082FF", text_color='#475569') #wight=430, height=38) #corner_radius = 8  # Мягкое скругление углов
environment.set('Воздух') #Сет выбирает слово в кавычках как дефолтное
environment_changed(environment.get())
environment.grid(row=1, column=0, padx=15)

#environment.bind('<<ComboboxSelected>>',
#environment_changed()

#Поля ввода
e1 = ctk.CTkEntry(block, placeholder_text= '', width=320, height=36, border_width=1, border_color='#CBD5E1') #Время
e1.grid(row=4, column=0, sticky='e', padx=15)

e2 = ctk.CTkEntry(block, placeholder_text='', width=320, height=36, border_width=1, border_color='#CBD5E1') #Температура
e2.grid(row=6, column=0, sticky='e', padx=15)

#На лейбл выводится результат
label = ctk.CTkLabel(root,
              text="",
              font=("ComicSansMC", 12),
              text_color='black',
              )
label.place(x=420, y=100)

#environment.bind('<<ComboboxSelected>>',
#environment_changed)

#def dele(): #команда на очистку всех полей
    #e1.delete(0, END)
    #e2.delete(0, END)
    #solenost.delete(0, END)
    #davlenie.delete(0, END)
    #label.configure(text="")

#btn1 = ctk.CTkButton(root,
             #text = 'Удалить',
             #command = dele,
             #font = ("ComicSansMS", 20),
             #width=430, height=38, #Размеры кнопки
             #hover_color = 'blue',
             #fg_color = '#3A92FF',
             #text_color = 'white'
             #)
#btn1.pack()

#Считает ВСЁ
def distanse():
    try:
        num1 = float(e1.get()) #Время. Переменная = принять за число(знаки из поля ввода. Вытащить())
        num2 = float(e2.get()) #Температура
        if environment.get()=='Воздух': #Смотрит на значение параши-переменной и смотрит, воздух ли там
            v=331 + 0.6 * num2
        elif environment.get()=='Вода':
            if solenost.get() in ('') or davlenie.get() in (''): #Если оставил поле пустым, то скорость берётся базовая
                v = 1480
            else:
                s = float(solenost.get())  # Солёность в промилле
                d = float(davlenie.get())  # Давление/Глубина в метрах
                v=1448.96 + (4.591 * num2) - (0.05304 * (num2**2)) + (0.0002374 * (num2**3)) + (1.34 * (s - 35)) + (0.0163 * d) #Формула Маккензи
        result = num1 * v / 2
        label.configure(text=f"Скорость звука: {v:.1f} м/с\nРезультат: {result:.2f} м.", #:.2f округляет до 2 знаков после запятой, n - энтер
                     text_color='green')
    except ValueError: #Вместо ошибки прога ругает тебя
        label.configure(text='Числа пиши осёл.', #Конфигур меняет. В данном случае меняет текст с пустого на инструкцию и имя получателя
                     text_color='red')

btn2 = ctk.CTkButton(block,
             text = 'Рассчитать',
             command = distanse,
             font = ("ComicSansMS", 15),
             #width=10, height=2, - Размеры кнопки
             hover_color = 'blue', #activebackground = hover_color
             fg_color = '#0082FF', #bg, background = fg_color 3a92ff
             text_color = 'white', #fg = text_color
             width=350, height=35
             )
btn2.place(x=15, y=400)

#e.insert(0, 'Введи') - Надпись в строке по дефолту

root.mainloop()