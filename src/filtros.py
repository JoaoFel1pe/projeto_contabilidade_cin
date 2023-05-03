from tkinter import messagebox

import pandas as pd

from funcoes import *


class Filtros:
    def __init__(self) -> None:
        pass

    # Recebe uma string que representa a UF (Unidade Federativa) de um uf e filtra os dados do arquivo Excel para incluir apenas as linhas que correspondem a esse uf. Se não houver dados para esse uf, uma mensagem de erro é exibida.
    def filtrar_uf(self, UF):
        df = criar_dataframe_por_uf(UF)

        if df.empty:
            messagebox.showinfo(
                "Erro",
                "Ocorreu um erro na sua requisição. Ou o você não passou o UF de forma adequada, ou esse UF não existe",
            )
        else:
            df.to_excel(rf"reports\ufs\dados_{UF}_filtrados.xlsx", index=True)
            messagebox.showinfo(
                "SUCESSO",
                "Sua requisição foi realizada com sucesso. Cheque o diretório destinado aos relatórios",
            )

    # Recebe uma string que representa o nome e a UF (Unidade Federativa) de uma conta e filtra os tipos de despesas daquela conta por cada municipio do estado
    def filtrar_conta_uf(self, UF, conta):
        df = criar_dataframe_por_conta(UF, conta)

        if df.empty:
            messagebox.showinfo(
                "Erro",
                "Ocorreu um erro na sua requisição. Ou o você não passou o UF de forma adequada, ou esse UF não existe",
            )
        else:
            df.to_excel(
                rf"reports\contas\dados_{conta.split(' - ')[1]}-{UF}_filtrados.xlsx",
                index=True,
            )
            messagebox.showinfo(
                "SUCESSO",
                "Sua requisição foi realizada com sucesso. Cheque o diretório destinado aos relatórios",
            )
