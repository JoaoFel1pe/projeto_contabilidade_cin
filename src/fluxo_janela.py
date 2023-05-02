import os
import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from filtros import COLUNAS, Filtros


class Reports:
    # Inicializa a classe, configurando a janela principal da interface.
    def __init__(self, master):
        self.filtros = Filtros()

        self.master = master
        self.master.title("Relatórios")
        self.master.geometry("300x300")

        self.frame_menu = tk.Frame(self.master)
        self.frame_uf = tk.Frame(self.master)
        self.frame_conta_uf = tk.Frame(self.master)
        self.frame_reports = tk.Frame(self.master)

        self.criar_menu()

    def botoes_enviar_voltar(self, frame, entrada):
        def enviar(l):
            botao_enviar = tk.Button(
                frame,
                text="Enviar",
                command=l,
            )
            botao_enviar.pack()

        def voltar():
            botao_voltar = tk.Button(frame, text="Voltar", command=self.voltar_menu)
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
        rotulo = tk.Label(self.frame_menu, text="Escolha o tipo de filtro:")
        rotulo.pack()

        botao_uf = tk.Button(
            self.frame_menu, text="Filtrar por UF", command=self.criar_janela_uf
        )
        botao_uf.pack()

        botao_conta_uf = tk.Button(
            self.frame_menu, text="Filtrar por Conta", command=self.criar_janela_conta_uf
        )
        botao_conta_uf.pack()

        botao_reports = tk.Button(
            self.frame_menu,
            text="Checar relatórios existentes",
            command=self.criar_janela_reports,
        )
        botao_reports.pack()

    # Cria uma nova janela para que o usuário possa digitar a UF (Unidade Federativa) do uf que deseja filtrar. Quando o botão "Enviar" é clicado, a função filtrar_uf é chamada.
    def criar_janela_uf(self):
        self.frame_uf = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_uf.pack()

        rotulo = tk.Label(self.frame_uf, text="Digite a UF desejada:")
        rotulo.pack()

        entrada = tk.Entry(self.frame_uf)
        entrada.pack()

        self.botoes_enviar_voltar(self.frame_uf, entrada)

    # Cria uma nova janela para o usuário filtrar a CONTA que ele deseja com base numa UF
    def criar_janela_conta_uf(self):
        self.frame_conta_uf = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_conta_uf.pack()

        rotulo = tk.Label(self.frame_conta_uf, text="Digite a UF desejada e o tipo de conta a ser filtrado:")
        rotulo.pack()

        entrada = tk.Entry(self.frame_conta_uf)
        entrada.pack()

        self.opcao_conta = tk.StringVar()
        combobox = ttk.Combobox(self.frame_conta_uf, textvariable=self.opcao_conta, values=["Selecione uma opção"] + COLUNAS[1:-1], state="readonly")
        combobox.pack()

        botao = tk.Button(self.frame_conta_uf, text="Filtrar", command=lambda: print(entrada.get(), self.opcao_conta.get()))
        botao.pack()
        

    # Cria uma interface gráfica que permite ao usuário visualizar e abrir relatórios disponíveis
    def criar_janela_reports(self):
        self.frame_reports = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_reports.pack()

        rotulo = tk.Label(self.frame_reports, text="Lista de relatórios disponíveis:")
        rotulo.pack()

        # Obtem a lista de arquivos na pasta "reports"
        arquivos_ufs = os.listdir("reports/ufs")

        # Cria um widget ListBox para exibir os nomes dos arquivos
        lista_arquivos = tk.Listbox(self.frame_reports, width=50)
        lista_arquivos.pack()

        # Adiciona cada arquivo à lista
        for arquivo in arquivos_ufs:
            lista_arquivos.insert(tk.END, "UF -> " + arquivo.split("_")[1])

        # Adiciona um evento de clique na lista de arquivos
        lista_arquivos.bind("<Double-Button-1>", self.abrir_arquivo_excel)

        self.botoes_enviar_voltar(frame=self.frame_reports, entrada=None)

    def abrir_arquivo_excel(self, event):
        widget = event.widget
        selection = widget.curselection()
        working_dir = os.getcwd()

        if selection:
            arquivo = widget.get(selection[0])
            if "UF" in arquivo:
                caminho = f"{working_dir}/reports/ufs/dados_{arquivo.split(' -> ')[1]}_filtrados.xlsx"
            os.startfile(caminho)

    # Retorna para o menu principal da interface, destruindo as janelas secundárias que estiverem abertas.
    def voltar_menu(self):
        self.frame_uf.pack_forget()
        self.frame_reports.pack_forget()
        self.criar_menu()

    # Recebe uma string que representa a UF (Unidade Federativa) de um uf e a retorna em maiúsculo, sem espaços em branco no início ou no final.
    def tratar_uf(self, UF):
        return UF.upper().strip()


def rodar_janelas():
    root = tk.Tk()
    app = Reports(root)
    app.criar_menu()
    root.mainloop()


if __name__ == "__main__":
    rodar_janelas()
