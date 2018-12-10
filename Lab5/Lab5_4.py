import datetime
from tkinter import *


def show_dif():
    birth = tuple([int(i) for i in date.get().split('.')])
    death = datetime.datetime(birth[2]+71, birth[1], birth[0])
    birthday = datetime.datetime(birth[2], birth[1], birth[0])
    delta = now - birthday
    deltad = death - now
    if r_var.get() == 0:
        result['text'] = delta.days
        resulte['text'] = deltad.days
    elif r_var.get() == 1:
        result['text'] = int(delta.total_seconds() // 3600)
        resulte['text'] = int(deltad.total_seconds() // 3600)
    elif r_var.get() == 2:
        result['text'] = int(delta.total_seconds() // 60)
        resulte['text'] = int(deltad.total_seconds() // 60)
    elif r_var.get() == 3:
        result['text'] = delta.days // 365
        resulte['text'] = deltad.days // 365


root = Tk()
root.title('Узнай всю правду')
greet = Label(text='Введите день вашего рождения в формате дд.мм.гггг')
frame1 = Frame()
frame2 = Frame()
frame3 = Frame()
dur = Label(frame2, text='сколько вы прожили |')
end = Label(frame2, text="сколько вам осталось")
result = Label(frame3)
resulte = Label(frame3)
probel = Label(frame3, text='      ')
date = Entry()
now = datetime.datetime.now()
but = Button(text="рассчитать", command=show_dif)

r_var = IntVar()
r_var.set(3)
day = Radiobutton(frame1, text='дни', variable=r_var, value=0)
month = Radiobutton(frame1, text='часы', variable=r_var, value=1)
sec = Radiobutton(frame1, text='минуты', variable=r_var, value=2)
year = Radiobutton(frame1, text='года', variable=r_var, value=3)

greet.pack()
date.pack()
frame1.pack()
year.pack(side='left')
day.pack(side='left')
month.pack(side='left')
sec.pack(side='left')
but.pack()
frame2.pack()
frame3.pack()
dur.pack(side='left')
end.pack(side='left')
result.pack(side='left')
probel.pack(side='left')
resulte.pack(side='left')


root.mainloop()