import os
import tkinter as tk
from tkinter import messagebox

import pandas as pd


class Reports:
    # Inicializa a classe, configurando a janela principal da interface.
    def __init__(self, master):
        self.master = master
        self.master.title("Relatórios")
        self.master.geometry("400x300")

        self.frame_menu = tk.Frame(self.master)
        self.frame_estado = tk.Frame(self.master)
        self.frame_municipio = tk.Frame(self.master)
        self.frame_reports = tk.Frame(self.master)

        self.criar_menu()

    # Cria um menu de opções para o usuário escolher o tipo de filtro que deseja aplicar aos dados.
    def criar_menu(self):
        for widget in self.frame_menu.winfo_children():
            widget.destroy()

        self.frame_menu.pack()
        rotulo = tk.Label(self.frame_menu, text="Escolha o tipo de filtro:")
        rotulo.pack()

        botao_estado = tk.Button(
            self.frame_menu, text="Filtrar por Estado", command=self.criar_janela_estado
        )
        botao_estado.pack()

        botao_municipio = tk.Button(
            self.frame_menu,
            text="Filtrar por Município",
            command=self.criar_janela_municipio,
        )
        botao_municipio.pack()

        botao_reports = tk.Button(
            self.frame_menu,
            text="Checar relatórios existentes",
            command=self.criar_janela_reports,
        )
        botao_reports.pack()

    # Cria uma nova janela para que o usuário possa digitar a UF (Unidade Federativa) do estado que deseja filtrar. Quando o botão "Enviar" é clicado, a função filtrar_estado é chamada.
    def criar_janela_estado(self):
        self.frame_estado = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_estado.pack()

        rotulo = tk.Label(self.frame_estado, text="Digite o UF desejado:")
        rotulo.pack()

        entrada = tk.Entry(self.frame_estado)
        entrada.pack()

        botao_enviar = tk.Button(
            self.frame_estado,
            text="Enviar",
            command=lambda: self.filtrar_estado(entrada.get()),
        )
        botao_enviar.pack()

        botao_voltar = tk.Button(
            self.frame_estado, text="Voltar", command=self.voltar_menu
        )
        botao_voltar.pack()

    # Cria uma nova janela para que o usuário possa digitar o nome do município e a UF (Unidade Federativa) do município que deseja filtrar. Quando o botão "Enviar" é clicado, a função filtrar_municipio é chamada.
    def criar_janela_municipio(self):
        self.frame_municipio = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_municipio.pack()

        rotulo = tk.Label(
            self.frame_municipio,
            text="Digite o Município desejado no seguinte formato:",
        )
        rotulo.pack()

        rotulo2 = tk.Label(
            self.frame_municipio, text="nome do município - UF do município"
        )
        rotulo2.pack()

        rotulo3 = tk.Label(
            self.frame_municipio,
            text="Exemplo: Recife - PE      ou      Belo Horizonte - MG",
        )
        rotulo3.pack()

        entrada = tk.Entry(self.frame_municipio)
        entrada.pack()

        botao_enviar = tk.Button(
            self.frame_municipio,
            text="Enviar",
            command=lambda: self.filtrar_municipio(entrada.get()),
        )
        botao_enviar.pack()

        botao_voltar = tk.Button(
            self.frame_municipio, text="Voltar", command=self.voltar_menu
        )
        botao_voltar.pack()

    def criar_janela_reports(self):
        self.frame_reports = tk.Frame(self.master)
        self.frame_menu.pack_forget()
        self.frame_reports.pack()

        rotulo = tk.Label(self.frame_reports, text="Lista de relatórios disponíveis:")
        rotulo.pack()

        # Obtem a lista de arquivos na pasta "reports"
        arquivos_ufs = os.listdir("reports/ufs")
        arquivos_municipios = os.listdir("reports/municipios")

        # Cria um widget ListBox para exibir os nomes dos arquivos
        lista_arquivos = tk.Listbox(self.frame_reports, width=50)
        lista_arquivos.pack()

        # Adiciona cada arquivo à lista
        for arquivo in arquivos_ufs:
            lista_arquivos.insert(tk.END, "UF - " + arquivo.split("_")[1])

        for arquivo in arquivos_municipios:
            lista_arquivos.insert(tk.END, "MUNICÍPIO - " + arquivo.split("_")[1])

        # Adiciona um evento de clique na lista de arquivos
        lista_arquivos.bind("<Double-Button-1>", self.abrir_arquivo_excel)

        botao_voltar = tk.Button(
            self.frame_reports, text="Voltar", command=self.voltar_menu
        )
        botao_voltar.pack()

    def abrir_arquivo_excel(self, event):
        widget = event.widget
        selection = widget.curselection()
        working_dir = os.getcwd()

        if selection:
            arquivo = widget.get(selection[0])
            if "UF" in arquivo:
                caminho = f"{working_dir}/reports/ufs/dados_{arquivo.split(' - ')[1]}_filtrados.xlsx"
            else:
                caminho = f"{working_dir}/reports/municipios/dados_{arquivo.split(' - ')[1]}_filtrados.xlsx"
            os.startfile(caminho)

    # Retorna para o menu principal da interface, destruindo as janelas secundárias que estiverem abertas.
    def voltar_menu(self):
        self.frame_estado.pack_forget()
        self.frame_municipio.pack_forget()
        self.frame_reports.pack_forget()
        self.criar_menu()

    # Recebe uma string que representa a UF (Unidade Federativa) de um estado e a retorna em maiúsculo, sem espaços em branco no início ou no final.
    def tratar_uf(self, UF):
        return UF.upper().strip()

    # Recebe uma string que representa o nome e a UF (Unidade Federativa) de um município e a retorna com o nome em título e a UF em maiúsculo.
    def tratar_municipio(self, municipio):
        return municipio.strip().upper()

    # Recebe uma string que representa a UF (Unidade Federativa) de um estado e filtra os dados do arquivo Excel para incluir apenas as linhas que correspondem a esse estado. Se não houver dados para esse estado, uma mensagem de erro é exibida.
    def filtrar_estado(self, UF):
        UF = self.tratar_uf(UF)
        df = pd.read_excel("data\dataframe_tratado.xlsx")
        df_filtrado = df.loc[df["UF"] == UF]
        if df_filtrado.empty:
            messagebox.showinfo(
                "Erro",
                "Ocorreu um erro na sua requisição. Ou o você não passou o UF de forma adequada, ou esse UF não existe",
            )
        else:
            df_filtrado.to_excel(rf"reports\ufs\dados_{UF}_filtrados.xlsx", index=False)
            messagebox.showinfo(
                "SUCESSO",
                "Sua requisição foi realizada com sucesso. Cheque o diretório destinado aos relatórios",
            )

    # Recebe uma string que representa o nome e a UF (Unidade Federativa) de um município e filtra os dados do arquivo Excel para incluir apenas as linhas que correspondem a esse município. Se não houver dados para esse município, uma mensagem de erro é exibida. Caso contrário, uma nova janela é aberta para exibir os dados filtrados.
    def filtrar_municipio(self, municipio):
        municipio = self.tratar_municipio(municipio)
        df = pd.read_excel("data\dataframe_tratado.xlsx")
        df_filtrado = df.loc[
            df["INSTITUIÇÃO"] == "PREFEITURA MUNICIPAL DE " + municipio
        ]
        if df_filtrado.empty:
            messagebox.showinfo(
                "Erro",
                "Ocorreu um erro na sua requisição. Ou o você não passou o município de forma adequada, ou esse município não existe",
            )
        else:
            df_filtrado.to_excel(
                f"reports\municipios\dados_{municipio}_filtrados.xlsx", index=False
            )
            messagebox.showinfo(
                "SUCESSO",
                "Sua requisição foi realizada com sucesso. Cheque o diretório destinado aos relatórios",
            )


def rodar_janelas():
    root = tk.Tk()
    app = Reports(root)
    app.criar_menu()
    root.mainloop()
