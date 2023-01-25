from tkinter import *
import os



janela = Tk()
img = PhotoImage(file = "C:\Projeto Cadastro\Sistema de cadastros de Pacientes\img\logo-cin.png")
class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.logo()
        self.conteudo()
        janela.mainloop()
    def tela(self):
        self.janela.title("Cadastro de Pacientes - CIN")
        self.janela.configure(background='#B0C4DE')
        self.janela.geometry("600x650")
        self.janela.resizable(False, False)
    def frames(self):
        self.frame_1 = Frame(self.janela)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.96)
        self.frame_2 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=2)
        self.frame_2.place(relx= 0.10, rely=0.20, relwidth= 0.80, relheight= 0.75)
        self.frame_3 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_3.place(relx= 0.12, rely=0.22, relwidth= 0.76, relheight= 0.15)
        self.frame_4 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_4.place(relx= 0.12, rely=0.38, relwidth= 0.76, relheight= 0.10)
        self.frame_5 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_5.place(relx= 0.12, rely=0.49, relwidth= 0.76, relheight= 0.10)
        self.frame_6 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_6.place(relx= 0.12, rely=0.60, relwidth= 0.76, relheight= 0.10)
        self.frame_7 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_7.place(relx= 0.12, rely=0.71, relwidth= 0.76, relheight= 0.10)

    def logo(self):
        img = PhotoImage(file = "C:\Projeto Cadastro\Sistema de cadastros de Pacientes\img\logo-cin.png")
        self.lg = Label(self.frame_1, image=img)
        self.lg.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.5)

    def conteudo(self):

        img = PhotoImage(file = "img/logo-cin.png")
        self.lg = Label(self.frame_1, image=img)
        self.lg.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.5)

        self.nome = Label(self.frame_1, text="Nome do Paciente:")
        self.nome.place(relx=0.08, rely=0.14)
        self.n = Entry(self.frame_1)
        self.n.place(relx=0.27, rely=0.14, relwidth=0.65)
        
        self.identificacao = Label(self.frame_3, text="Documento de Identificação:")
        self.identificacao.place(relx=0.05, rely=0.05)
        self.bt_frente = Button(self.frame_3, text="Frente")
        self.bt_frente.place(relx=0.05, rely=0.70, relwidth=0.15, relheight=0.25)
        self.bt_verso = Button(self.frame_3, text="Verso")
        self.bt_verso.place(relx=0.25, rely=0.70, relwidth=0.15, relheight=0.25)

        self.carteirinha = Label(self.frame_4, text="Carteirinha do Plano de Saúde:")
        self.carteirinha.place(relx=0.05, rely=0.05)
        self.bt_inserircarteirinha = Button(self.frame_4, text="Inserir")
        self.bt_inserircarteirinha.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.4)

        self.pedidom = Label(self.frame_5, text="Pedido Médico:")
        self.pedidom.place(relx=0.05, rely=0.05)
        self.bt_inserirpedidom = Button(self.frame_5, text="Inserir")
        self.bt_inserirpedidom.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.4)

        self.relatoriom = Label(self.frame_6, text="Relatório Médico:")
        self.relatoriom.place(relx=0.05, rely=0.05)
        self.bt_inserirrelatoriom = Button(self.frame_6, text="Inserir")
        self.bt_inserirrelatoriom.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.4)

        self.exames = Label(self.frame_7, text="Exames:")
        self.exames.place(relx=0.05, rely=0.05)
        self.bt_inserirexames = Button(self.frame_7, text="Inserir")
        self.bt_inserirexames.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.4)

        self.bt_frente = Button(self.frame_2, text="Gravar")
        self.bt_frente.place(relx=0.2, rely=0.90, relwidth=0.15, relheight=0.05)
        self.bt_verso = Button(self.frame_2, text="Limpar")
        self.bt_verso.place(relx=0.65, rely=0.90, relwidth=0.15, relheight=0.05)


Aplicacao()


janela.mainloop()