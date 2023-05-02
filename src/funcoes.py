import locale

import pandas as pd

# Constantes
CAMINHO_DADOS = "data/dataframe_tratado.xlsx"
COLUNAS = [
    "INSTITUIÇÃO",
    "SEGURANÇA PÚBLICA",
    "ASSISTÊNCIA SOCIAL",
    "PREVIDÊNCIA SOCIAL",
    "SAÚDE",
    "EDUCAÇÃO",
    "TOTAL",
]
CONTAS = [
    "06 - SEGURANÇA PÚBLICA",
    "08 - ASSISTÊNCIA SOCIAL",
    "09 - PREVIDÊNCIA SOCIAL",
    "10 - SAÚDE",
    "10.301 - ATENÇÃO BÁSICA",
    "10.302 - ASSISTÊNCIA HOSPITALAR E AMBULATORIAL",
    "10.303 - SUPORTE PROFIILÁTICO E TERAPÊUTICO",
    "10.304 - VIGILÂNCIA SANITÁRIA",
    "10.305 - VIGILÂNCIA EPIDEMIOLÓGICA",
    "10.306 - ALIMENTAÇÃO E NUTRIÇÃO",
    "12 - EDUCAÇÃO",
]

# Define a localização para formatação de moeda
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def criar_dataframe_por_uf(uf):
    # Carrega os dados
    dados = pd.read_excel(CAMINHO_DADOS)

    # Filtra os dados por UF e funções
    dados_filtrados = dados[(dados["UF"] == uf) & (dados["CONTA"].isin(CONTAS))]

    # Converte a coluna de valores para numérico
    dados_filtrados["VALOR"] = pd.to_numeric(dados_filtrados["VALOR"], errors="coerce")

    # Agrupa os dados por instituição e função e soma os valores
    dados_agrupados = (
        dados_filtrados.groupby(["INSTITUIÇÃO", "CONTA"])["VALOR"].sum().reset_index()
    )

    # Agrupa os dados por instituição e calcula o total
    total_por_instituicao = (
        dados_agrupados.groupby("INSTITUIÇÃO")["VALOR"].sum().reset_index()
    )

    # Cria um dataframe vazio com as colunas desejadas
    df = pd.DataFrame(columns=COLUNAS)

    # Define a coluna de instituição como índice
    df = df.set_index("INSTITUIÇÃO")

    sub = 0
    # Preenche o dataframe com os valores calculados
    for index, row in dados_agrupados.iterrows():
        instituicao = row["INSTITUIÇÃO"]
        funcao = row["CONTA"]
        valor = row["VALOR"]
        if funcao == "10 - SAÚDE":
            sub = valor
        total = total_por_instituicao[
            total_por_instituicao["INSTITUIÇÃO"] == instituicao
        ]["VALOR"].values[0]
        df.loc[instituicao, funcao] = valor
        df.loc[instituicao, "TOTAL"] = total - sub

    # Formata as células do dataframe como moeda
    df = df.applymap(
        lambda x: locale.currency(x, grouping=True)
        if isinstance(x, (int, float))
        else x
    )
    # Remove as colunas desnecessárias
    df = df.drop(
        columns=[
            "SEGURANÇA PÚBLICA",
            "ASSISTÊNCIA SOCIAL",
            "PREVIDÊNCIA SOCIAL",
            "SAÚDE",
            "EDUCAÇÃO",
        ]
    )
    return df
