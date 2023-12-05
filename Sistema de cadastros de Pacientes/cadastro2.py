from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


janela = Tk()
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
        self.frame_2.place(relx= 0.10, rely=0.24, relwidth= 0.80, relheight= 0.71)
        self.frame_3 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_3.place(relx= 0.12, rely=0.26, relwidth= 0.76, relheight= 0.15)
        self.frame_4 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_4.place(relx= 0.12, rely=0.42, relwidth= 0.76, relheight= 0.10)
        self.frame_5 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_5.place(relx= 0.12, rely=0.53, relwidth= 0.76, relheight= 0.10)
        self.frame_6 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_6.place(relx= 0.12, rely=0.64, relwidth= 0.76, relheight= 0.10)
        self.frame_7 = Frame(self.janela, bd=4, highlightbackground='#B0C4DE', highlightthickness=1)
        self.frame_7.place(relx= 0.12, rely=0.75, relwidth= 0.76, relheight= 0.10)

    def logo(self):
        logoimg = Image.open("img/logo-cin-1(2).png")
        self.lg = ImageTk.PhotoImage(logoimg)
        self.lbl = tk.Label(self.frame_1, image= self.lg)
        self.lbl.place(relx=0.40, rely=0.01, relwidth=0.2, relheight=0.12)
        self.lbl.image = self.lg
      

    def conteudo(self):


        self.titulo = Label(self.frame_1, text="CADASTRO DE PACIENTE",)
        self.titulo.place(relx=0.38, rely=0.14)

        self.nome = Label(self.frame_1, text="Nome do Paciente:")
        self.nome.place(relx=0.08, rely=0.18)
        self.n = Entry(self.frame_1)
        self.n.place(relx=0.27, rely=0.18, relwidth=0.65)
        
        self.rselecionado = StringVar()
        self.r = self.rselecionado.get()
        

        self.identificacao = Label(self.frame_3, text="Documento de Identificação:")
        self.identificacao.place(relx=0.05, rely=0.05)
        
        self.r1 = Radiobutton(self.frame_3, text='RG', value=1, variable= self.rselecionado)
        self.r1.place(relx=0.05, rely=0.32)
        self.r2 = Radiobutton(self.frame_3, text='CNH', value=2, variable= self.rselecionado)
        self.r2.place(relx=0.25, rely=0.32)
        
        
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
        self.bt_frente.place(relx=0.2, rely=0.92, relwidth=0.15, relheight=0.05)
        self.bt_verso = Button(self.frame_2, text="Limpar")
        self.bt_verso.place(relx=0.65, rely=0.92, relwidth=0.15, relheight=0.05)

        #botaoimg = Image.open("gifs-c(3).png")
        #self.lg1 = ImageTk.PhotoImage(botaoimg)
        #self.lbl2 = Button(self.frame_5, image= self.lg1)
        #self.lbl2.place(relx=0.70, rely=0.5)
        self.entry_data = DateEntry(self.frame_5, width=10)
        self.entry_data.place(relx=0.25,rely=0.52, relheight=0.38)

        #botaoimg = Image.open("gifs-c(3).png")
        #self.lg2 = ImageTk.PhotoImage(botaoimg)
        #self.lbl3 = Button(self.frame_6, image= self.lg1)
        #self.lbl3.place(relx=0.70, rely=0.4)
        self.entry_data2 = DateEntry(self.frame_6, width=10)
        self.entry_data2.place(relx=0.25,rely=0.5)
       

Aplicacao()


janela.mainloop()