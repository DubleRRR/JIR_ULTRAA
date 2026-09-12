#from tkinter import *
import customtkinter as ctk #Подключил библиотеки

#Окно
root = ctk.CTk()
root.title('Калькулятор эхолокации')
root.geometry('720x480')
root.resizable(width=False, height=False)

#ctk.set_appearance_mode("Light")
#root.configure(fg_color="#F0F4F8")

#root['bg'] = '#3A92FF' - Цвет фона

#Поля ввода, которые появляются ток с водой
solenost = ctk.CTkEntry(root, placeholder_text='Солёность воды,‰', width=430, height=38) #Переменная солёности

davlenie = ctk.CTkEntry(root, placeholder_text='Глубина,м', width=430, height=38) #Переменная давления/глубины

def environment_changed(choiсe): #Чойс - то же говно, что и энвироментс которое можно называть как угодно. Чанджед реагирует, когда переменая перед '_' изменяется
    if choiсe == 'Вода': #С водой проявляет поля
        solenost.pack(pady=5)
        davlenie.pack(pady=5)
    elif choiсe == 'Воздух': #С воздухом прячет
        solenost.pack_forget()
        davlenie.pack_forget()

environments = ['Воздух', 'Вода'] #Энвироментс - параша, название переменной, именую как хочу. Список - это квадратные скобки
environment = ctk.CTkComboBox(root, #Комбобокс - лист-выпадашка
                              values=environments, #Валуес - слова в выпадашке
                              command=environment_changed, height=38, width=430, border_width=1) #wight=430, height=38) #corner_radius = 8  # Мягкое скругление углов
environment.set('Воздух') #Сет выбирает слово в кавычках как дефолтное
environment.pack()

#Поля ввода
e1 = ctk.CTkEntry(root, placeholder_text='Время,с', width=430, height=38)
e1.pack(pady=10)

e2 = ctk.CTkEntry(root, placeholder_text='Температура,°C', width=430, height=38)
e2.pack(pady=10)

#На лейбл выводится результат
label = ctk.CTkLabel(root,
              text="",
              font=("ComicSamsMC", 12),
              text_color='black',
              )
label.pack(pady=5)

#environment.bind('<<ComboboxSelected>>',
#environment_changed)

#def dele(): #команда на очистку всех полей
    #e1.delete(0, END)
    #e2.delete(0, END)
    #solenost.delete(0, END)
    #davlenie.delete(0, END)
    #label.config(text='')

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
        num1 = float(e1.get()) #Время. Переменная = принять за число(знаки из поля ввода.вытащить())
        num2 = float(e2.get()) #Температура
        if environment.get()=='Воздух': #Смотрит на значение параши-переменной и смотрит, воздух ли там
            v=331 + 0.6 * num2
        elif environment.get()=='Вода':
            if solenost.get() in ('', 'Солёность') or davlenie.get() in ('', 'Давление'): #Если оставил поле пустым, то скорость берётся базовая
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

btn2 = ctk.CTkButton(root,
             text = 'Высчитать',
             command = distanse,
             font = ("ComicSansMS", 20),
             #width=10, height=2, - Размеры кнопки
             hover_color = 'blue', #activebackground = hover_color
             fg_color = '#3A92FF', #bg, background = fg_color
             text_color = 'white', #fg = text_color
             width=430, height=38
             )
btn2.pack(pady=10)

#e.insert(0, 'Введи') - Надпись в строке по дефолту

root.mainloop()