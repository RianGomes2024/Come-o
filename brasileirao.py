import customtkinter as ctk

def cam():
    ca=int(campeao.get())
    cam=int(time.get())
    r=ca-cam
    resultado.configure(text=f'seu time esta a {r} pontos atras do lider')
def libertadores():
    li=int(liberta.get())
    lib=int(time.get())
    r1=li-lib
    if lib>li:
        resultado.configure(text=f'seu time esta a {r1} pontos a fente ultima vaga de libertadores ')    
    else:
          resultado.configure(text=f'seu time esta a {r1} pontos atras da ultima vaga da liberta ')
def sulamerica():
    s=int(sula.get())
    s1=int(time.get())
    sulam=s1-s
    if s1>s:
     resultado.configure(text=f'seu time esta a {sulam} pontos a frente do primeiro time fora da sula')
    else:
       resultado.configure(text=f'seu time esta a {sulam} pontos atras da ultima vaga da sula')  

def rebaixamento():
    re=int(reb.get())
    reba=int(time.get())
    rebaixado=reba-re
    resultado.configure(text=f'seu time esta a {rebaixado} pontos do primeiro dentro da zona')    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

janela=ctk.CTk('black')
janela.geometry('700x700')
janela.title('Brasileirao')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ctk.CTkLabel(janela,
             text='Brasileirao',
             text_color='white',
             font=('verdana',30,'bold')).pack()

time=ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='informe a pontuacao do seu time')
time.pack(pady=10)
campeao=ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='informe a pontuacao do lider')
campeao.pack(pady=10)
liberta=ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='informe a pontuacao do 6 colocado')
liberta.pack(pady=10)
sula=ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='informe a pontuacao do 14')
sula.pack(pady=10)
reb=ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='informe a pontuacao do 17')
reb.pack(pady=10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
resultado2=ctk.CTkLabel(janela,
                       text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
                       text_color='white',
                       font=('arial',20,'bold')
                       )
resultado2.pack()
c=ctk.CTkButton(janela,
                text='dist.campeao',
                text_color='black',
                fg_color='yellow',
                command=cam)
c.pack(pady=10)

l=ctk.CTkButton(janela,
                text='dist.liberta',
                text_color='black',
                fg_color='green',
                command=libertadores)
l.pack(pady=10)
s=ctk.CTkButton(janela,
                text='dist.sula',
                text_color='black',
                fg_color='orange',
                command=sulamerica)
s.pack(pady=10)
r=ctk.CTkButton(janela,
                text='dist.rebaixamento',
                text_color='black',
                fg_color='red',
                command=rebaixamento)
r.pack(pady=10)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
resultado=ctk.CTkLabel(janela,
                       text='',
                       text_color='black',
                       font=('arial',20,'bold')
                       )
resultado.pack()

resultado1=ctk.CTkLabel(janela,
                       text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
                       text_color='white',
                       font=('arial',20,'bold')
                       )
resultado1.pack()
janela.mainloop()