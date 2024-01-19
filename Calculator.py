import tkinter as tk

def buton(n):
    current=enter.get()
    enter.delete(0,tk.END)
    enter.insert(0,str(current+str(n)))

def add():
    global n
    global d
    n=enter.get()
    enter.delete(0, tk.END)
    d=0

def min():
    global n
    global d
    n = enter.get()
    enter.delete(0, tk.END)
    d=1

def pro():
    global n
    global d
    n = enter.get()
    enter.delete(0, tk.END)
    d=2

def div():
    global n
    global d
    n = enter.get()
    enter.delete(0, tk.END)
    d=3

def equal():
    m=enter.get()
    enter.delete(0, tk.END)
    if d == 0:
        enter.insert(0,str(float(n)+float(m)))
    elif d==1:
        enter.insert(0, str(float(n) - float(m)))
    elif d==2:
        enter.insert(0, str(float(n) * float(m)))
    elif d==3:
        enter.insert(0, str(float(n) / float(m)))

def clear():
    global n
    enter.delete(0,tk.END)
    n=0

form = tk.Tk()
form.title("Hesap Makinesi")
enter=tk.Entry(form,width=35)
enter.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
buton1=tk.Button(form,text="1",padx=40,pady=20,command=lambda: buton(1))
buton1.grid(row=1,column=0)
buton2=tk.Button(form,text="2",padx=40,pady=20,command=lambda: buton(2))
buton2.grid(row=1,column=1)
buton3=tk.Button(form,text="3",padx=40,pady=20,command=lambda: buton(3))
buton3.grid(row=1,column=2)
buton4=tk.Button(form,text="4",padx=40,pady=20,command=lambda: buton(4))
buton4.grid(row=2,column=0)
buton5=tk.Button(form,text="5",padx=40,pady=20,command=lambda: buton(5))
buton5.grid(row=2,column=1)
buton6=tk.Button(form,text="6",padx=40,pady=20,command=lambda: buton(6))
buton6.grid(row=2,column=2)
buton7=tk.Button(form,text="7",padx=40,pady=20,command=lambda: buton(7))
buton7.grid(row=3,column=0)
buton8=tk.Button(form,text="8",padx=40,pady=20,command=lambda: buton(8))
buton8.grid(row=3,column=1)
buton9=tk.Button(form,text="9",padx=40,pady=20,command=lambda: buton(9))
buton9.grid(row=3,column=2)
buton10=tk.Button(form,text="0",padx=40,pady=20,command=lambda: buton(9))
buton10.grid(row=4,column=1)
buton11=tk.Button(form,text="+",padx=38,pady=20,command=add)
buton11.grid(row=1,column=3)
buton12=tk.Button(form,text="-",padx=40,pady=20,command=min)
buton12.grid(row=2,column=3)
buton13=tk.Button(form,text="*",padx=40,pady=20,command=pro)
buton13.grid(row=3,column=3)
buton14=tk.Button(form,text="/",padx=40,pady=20,command=div)
buton14.grid(row=4,column=3)
buton15=tk.Button(form,text="=",padx=40,pady=20,command=equal)
buton15.grid(row=4,column=2)
buton16=tk.Button(form,text="C",padx=40,pady=20,command=clear)
buton16.grid(row=4,column=0)

form.mainloop()