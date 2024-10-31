import customtkinter as ctk
def soma():
    s1=int(n1.get())
    s2=int(n2.get())
    soma1=s1+s2
    resultado.configure(text=f'{s1} + {s2} = {soma1:.0f}')

def sub():
    su1=int(n1.get())
    su2=int(n2.get())
    sub=su1-su2
    resultado.configure(text=f'{su1} - {su2} = {sub:.0f}')



def mult():
    m=int(n1.get())
    m1=int(n2.get())
    mul=m*m1
    resultado.configure(text=f'{m} x {m1} = {mul:.0f}')

    
def div():
    d=int(n1.get())
    d1=int(n2.get())
    div=d/d1
    resultado.configure(text=f'{d} / {d1} = {div:.0f}')



janela=ctk.CTk('black')
janela.geometry('500x500')
janela.title('calcular')

ctk.CTkLabel(janela,
             text='calculadora',
             font=('verdana',30,'bold'),
             text_color='yellow').pack()

n1=ctk.CTkEntry(janela,
                 width=400,
                 height=40,
                 placeholder_text='inorme o numero')
n1.pack()

n2=ctk.CTkEntry(janela,
                width=400,
                height=40,
                placeholder_text='informe o numero')
n2.pack(pady=10)

b1=ctk.CTkButton(janela,
                 text='+',
                 font=('verdana',15,'bold'),
                 fg_color='blue',
                 command=soma)
b1.pack(pady=10)

b2=ctk.CTkButton(janela,
                 text='-',
                 font=('verdana',15,'bold'),
                 fg_color='blue',
                 command=sub)
b2.pack(pady=10)

b3=ctk.CTkButton(janela,
                 text='*',
                 font=('verdana',15,'bold'),
                 fg_color='blue',
                 command=mult)
b3.pack(pady=10)

b4=ctk.CTkButton(janela,
                 text='/',
                 font=('verdana',15,'bold'),
                 fg_color='blue',
                 command=div)
b4.pack(pady=10)

resultado=ctk.CTkLabel(janela,
                       text='',
                       text_color='yellow')
                       
resultado.pack()




janela.mainloop()