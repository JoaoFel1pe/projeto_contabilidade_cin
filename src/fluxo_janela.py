import os
import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from filtros import CONTAS, Filtros


class Reports:
    # Inicializa a classe, configurando a janela principal da interface.
    def __init__(self, master):
        self.filtros = Filtros()

        self.master = master
        self.master.title("Relatórios")
        self.master.geometry("1000x450")

        self.frame_menu = tk.Frame(self.master, bg="#082130")
        self.frame_uf = tk.Frame(self.master, bg="#082130")
        self.frame_conta_uf = tk.Frame(self.master, bg="#082130")
        self.frame_reports = tk.Frame(self.master, bg="#082130")

        self.style = ttk.Style()
        self.style.configure('Rotulo.TLabel', font=('Arial', 20, 'bold'), padding=(0, 100, 0, 20), background="#082130", foreground='white')
        self.style.configure('Botao.TButton', font=('Helvetica', 12, 'bold'), padding=(0, 10, 0, 10), background="#082130")
        self.style.configure('Entrada.TEntry', font=('Helvetica', 50), padding=20, background="#082130")
        self.style.configure('Opcao.TCombobox', font=('Helvetica', 50), padding=10, background="#082130")
        self.criar_menu()

    def botoes_enviar_voltar(self, frame, entrada):
        def enviar(l):
            botao_enviar = ttk.Button(
                frame,
                text="Enviar",
                command=l,
                style='Botao.TButton',
            )
            botao_enviar.pack()

        def voltar():
            botao_voltar = ttk.Button(frame, text="Voltar", command=self.voltar_menu,
                style='Botao.TButton')
            botao_voltar.pack()

        if frame == self.frame_uf:
            filtro = self.filtros.filtrar_uf
            l = lambda: filtro(self.tratar_uf(entrada.get()))
            enviar(l)
            voltar()

        else:
            voltar()

    # Cria um menu de opções para o usuário escolher o tipo de filtro que deseja aplicar aos dados.
    def criar_menu(self):
        for widget in self.frame_menu.winfo_children():
            widget.destroy()

        self.frame_menu.pack()
        rotulo = ttk.Label(self.frame_menu, text="Escolha o tipo de filtro:", style='Rotulo.TLabel')
        rotulo.pack()

        botao_uf = ttk.Button(
            self.frame_menu, text="Filtrar por UF", command=self.criar_janela_uf, style='Botao.TButton'
        )
        botao_uf.pack()

        botao_conta_uf = ttk.Button(
            self.frame_menu,
            text="Filtrar por Conta",
            command=self.criar_janela_conta_uf,
        style='Botao.TButton')
        botao_conta_uf.pack()

        botao_reports = ttk.Button(
            self.frame_menu,
            text="Checar relatórios existentes",
            command=self.criar_janela_reports,style='Botao.TButton'
        )
        botao_reports.pack()

    # Cria uma nova janela para que o usuário possa digitar a UF (Unidade Federativa) do uf que deseja filtrar. Quando o botão "Enviar" é clicado, a função filtrar_uf é chamada.
    def criar_janela_uf(self):
        self.frame_uf = tk.Frame(self.master, bg="#082130")
        self.frame_menu.pack_forget()
        self.frame_uf.pack()

        rotulo = ttk.Label(self.frame_uf, text="Digite a UF desejada:",style='Rotulo.TLabel')
        rotulo.pack()

        entrada = ttk.Entry(self.frame_uf, style="Entrada.TEntry")
        entrada.pack()

        self.botoes_enviar_voltar(self.frame_uf, entrada)

    # Cria uma nova janela para o usuário filtrar a CONTA que ele deseja com base numa UF
    def criar_janela_conta_uf(self):
        self.frame_conta_uf = tk.Frame(self.master, bg="#082130")
        self.frame_menu.pack_forget()
        self.frame_conta_uf.pack()

        rotulo = ttk.Label(
            self.frame_conta_uf,
            text="Digite a UF desejada e o tipo de conta a ser filtrado:",style='Rotulo.TLabel'
        )
        rotulo.pack()

        entrada = ttk.Entry(self.frame_conta_uf, style="Entrada.TEntry", background="#082130")
        entrada.pack()

        self.opcao_conta = tk.StringVar()
        combobox = ttk.Combobox(
            self.frame_conta_uf,
            textvariable=self.opcao_conta,
            values=["Selecione uma opção"] + CONTAS,
            state="readonly",
            style='Opcao.TCombobox'
        )
        combobox.pack()

        botao = ttk.Button(
            self.frame_conta_uf,
            text="Filtrar",
            command=lambda: self.filtros.filtrar_conta_uf(
                entrada.get(), self.opcao_conta.get()
            ),style="Botao.TButton"
        )
        botao.pack()

        self.botoes_enviar_voltar(self.frame_conta_uf, entrada=None)

    # Cria uma interface gráfica que permite ao usuário visualizar e abrir relatórios disponíveis
    def criar_janela_reports(self):
        self.frame_reports = tk.Frame(self.master, background="#082130")
        self.frame_menu.pack_forget()
        self.frame_reports.pack()

        rotulo = ttk.Label(self.frame_reports, text="Lista de relatórios disponíveis:",style='Rotulo.TLabel')
        rotulo.pack()

        # Obtem a lista de arquivos na pasta "reports"
        arquivos_ufs = os.listdir("reports/ufs")
        arquivos_contas = os.listdir("reports/contas")

        # Cria um widget ListBox para exibir os nomes dos arquivos
        lista_arquivos = tk.Listbox(self.frame_reports, width=50)
        lista_arquivos.pack()

        # Adiciona cada arquivo à lista
        for arquivo in arquivos_ufs:
            lista_arquivos.insert(tk.END, "UF -> " + arquivo.split("_")[1])

        for arquivo in arquivos_contas:
            lista_arquivos.insert(tk.END, "CONTA -> " + arquivo.split("_")[1])

        # Adiciona um evento de clique na lista de arquivos
        lista_arquivos.bind("<Double-Button-1>", self.abrir_arquivo_excel)

        self.botoes_enviar_voltar(frame=self.frame_reports, entrada=None)

    def abrir_arquivo_excel(self, event):
        widget = event.widget
        selection = widget.curselection()
        working_dir = os.getcwd()

        if selection:
            caminho = ""
            arquivo = widget.get(selection[0])
            if "UF" in arquivo:
                caminho = f"{working_dir}/reports/ufs/dados_{arquivo.split(' -> ')[1]}_filtrados.xlsx"
            else:
                caminho = f"{working_dir}/reports/contas/dados_{arquivo.split(' -> ')[1]}_filtrados.xlsx"
            os.startfile(caminho)

    # Retorna para o menu principal da interface, destruindo as janelas secundárias que estiverem abertas.
    def voltar_menu(self):
        self.frame_uf.pack_forget()
        self.frame_conta_uf.pack_forget()
        self.frame_reports.pack_forget()
        self.criar_menu()

    # Recebe uma string que representa a UF (Unidade Federativa) de um uf e a retorna em maiúsculo, sem espaços em branco no início ou no final.
    def tratar_uf(self, UF):
        return UF.upper().strip()


def rodar_janelas():
    root = tk.Tk()
    root.configure(background="#082130")
    app = Reports(root)
    app.criar_menu()
    root.mainloop()


if __name__ == "__main__":
    rodar_janelas()
