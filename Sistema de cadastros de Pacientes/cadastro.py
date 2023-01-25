
from cProfile import label
from pydoc import text
from tkinter import *

from pygame import font

janela = Tk()
janela.title("Cadastro de Pacientes - CIN")
img = PhotoImage(file = "img/logo-cin.png")
logo = Label(janela, image=img)
logo.grid(column=2, row=0, padx=10, pady=10)

caixa = Label(janela, text="                    ")
caixa.grid(column=0, row=1)

caixa2 = Label(janela, text="                              ")
caixa2.grid(column=4, row=3)

caixa3 = Label(janela, text="                              ")
caixa3.grid(column=5, row=6)

caixa4 = Label(janela, text="                              ")
caixa4.grid(column=5, row=1)

caixa5 = Label(janela, text="                              ")
caixa5.grid(column=5, row=4)

caixa5 = Label(janela, text="                              ")
caixa5.grid(column=5, row=18)

caixa5 = Label(janela, text="                              ")
caixa5.grid(column=5, row=9)

caixa5 = Label(janela, text="                              ")
caixa5.grid(column=5, row=12)

caixa5 = Label(janela, text="                              ")
caixa5.grid(column=5, row=15)

texto_nome = Label(janela, text="Nome do Paciente:")
texto_nome.grid(column=1, row=2)
caixa_nome = Entry(janela, background="white", width=40, font="Arial 12")
caixa_nome.grid(column=2, row=2)

texto_identificacao = Label(janela, text="Documento de Identificação:")
texto_identificacao.grid(column=1, row=4)
botaof = Button(janela, text='Frente', command='*')
botaof.grid(column=1, row=5)
botaov = Button(janela, text='Verso', command='*')
botaov.grid(column=2, row=5)

texto_carteirinha = Label(janela, text="Carteirinha do Plano de Saúde:")
texto_carteirinha.grid(column=1, row=7)
inserir = Button(janela, text='Inserir', command='*')
inserir.grid(column=1, row=8)

texto_pedido = Label(janela, text="Pedido Médico:")
texto_pedido.grid(column=1, row=10)
inserirp = Button(janela, text='Inserir', command='*')
inserirp.grid(column=1, row=11)

texto_relatorio = Label(janela, text="Relatório Médico:")
texto_relatorio.grid(column=1, row=13)
inserir = Button(janela, text='Inserir', command='*')
inserir.grid(column=1, row=14)

texto_exames = Label(janela, text="Exames:")
texto_exames.grid(column=1, row=16)
inserir = Button(janela, text='Inserir', command='*')
inserir.grid(column=1, row=17)

janela.mainloop()

