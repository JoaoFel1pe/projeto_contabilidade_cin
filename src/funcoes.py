import locale

import pandas as pd

# Constantes
CAMINHO_DADOS = "data/dataframe_tratado.xlsx"
COLUNAS = [
    "DESPESAS",
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
    "12 - EDUCAÇÃO",
]

CONTAS_SUB = [
    
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
DESPESAS = [
    "DESPESAS EMPENHADAS",
    "DESPESAS LIQUIDADAS",
    "DESPESAS PAGAS",
    "INSCRIÇÃO DE RESTOS A PAGAR NÃO PROCESSADOS",
    "INSCRIÇÃO DE RESTOS A PAGAR PROCESSADOS",
]

linhas = [
    ["DESPESAS EMPENHADAS", 0, 0, 0, 0, 0, 0],
    ["DESPESAS LIQUIDADAS", 0, 0, 0, 0, 0, 0],
    ["DESPESAS PAGAS", 0, 0, 0, 0, 0, 0],
    ["INSCRIÇÃO DE RESTOS A PAGAR NÃO PROCESSADOS", 0, 0, 0, 0, 0, 0],
    ["INSCRIÇÃO DE RESTOS A PAGAR PROCESSADOS", 0, 0, 0, 0, 0, 0]
]

# lista de nomes de colunas
colunas = [
    "DESPESAS",
    "SEGURANÇA PÚBLICA",
    "ASSISTÊNCIA SOCIAL",
    "PREVIDÊNCIA SOCIAL",
    "SAÚDE",
    "EDUCAÇÃO",
    "TOTAL"
]


# Define a localização para formatação de moeda
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def criar_dataframe_por_uf(uf):
    # Carrega os dados
    dados = pd.read_excel(CAMINHO_DADOS)

    # Filtra os dados por UF e funções
    dados_filtrados = dados[(dados["UF"] == uf) & (dados["CONTA"].isin(CONTAS_SUB))]

    # Converte a coluna de valores para numérico
    dados_filtrados["VALOR"] = pd.to_numeric(dados_filtrados["VALOR"], errors="coerce")

    # Agrupa os dados por instituição e função e soma os valores
    dados_agrupados = (
        dados_filtrados.groupby(["DESPESAS", "CONTA"])["VALOR"].sum().reset_index()
    )

    # Agrupa os dados por instituição e calcula o total
    total_por_instituicao = (
        dados_agrupados.groupby("DESPESAS")["VALOR"].sum().reset_index()
    )
    
    # Cria um dataframe vazio com as colunas desejadas
    df = pd.DataFrame(columns=COLUNAS)

    # definir a coluna "DESPESAS" como o índice
    df.set_index("DESPESAS", inplace=True)


    # Preenche o dataframe com os valores calculados
    for index, row in dados_agrupados.iterrows():
        despesas = row["DESPESAS"]
        funcao = row["CONTA"]
        valor = row["VALOR"]
        total = total_por_instituicao[
            total_por_instituicao["DESPESAS"] == despesas
        ]["VALOR"].values[0]
        df.loc[despesas, funcao] = valor
        df.loc[despesas, "TOTAL"] = total

    df = df.drop(
        columns=[
            "SEGURANÇA PÚBLICA",
            "ASSISTÊNCIA SOCIAL",
            "PREVIDÊNCIA SOCIAL",
            "SAÚDE",
            "EDUCAÇÃO",
        ]
    )
    df.fillna(0, inplace=True)
    df["TOTAL"] = df["TOTAL"] - df["10 - SAÚDE"]
    df = df.applymap(
        lambda x: locale.currency(x, grouping=True)
        if isinstance(x, (int, float))
        else x
    )
    # Remove as colunas desnecessárias
    return df


def criar_dataframe_por_municipio(municipio):
    # Carrega os dados
    dados = pd.read_excel(CAMINHO_DADOS)

    # Filtra os dados por UF e funções
    dados_filtrados = dados[(dados["INSTITUIÇÃO"] == municipio) & (dados["CONTA"].isin(CONTAS_SUB))]

    # Converte a coluna de valores para numérico
    dados_filtrados["VALOR"] = pd.to_numeric(dados_filtrados["VALOR"], errors="coerce")

    # Agrupa os dados por instituição e função e soma os valores
    dados_agrupados = (
        dados_filtrados.groupby(["DESPESAS", "CONTA"])["VALOR"].sum().reset_index()
    )

    # Agrupa os dados por instituição e calcula o total
    total_por_instituicao = (
        dados_agrupados.groupby("DESPESAS")["VALOR"].sum().reset_index()
    )
    
    # Cria um dataframe vazio com as colunas desejadas
    df = pd.DataFrame(columns=COLUNAS)

    # definir a coluna "DESPESAS" como o índice
    df.set_index("DESPESAS", inplace=True)


    # Preenche o dataframe com os valores calculados
    for index, row in dados_agrupados.iterrows():
        despesas = row["DESPESAS"]
        funcao = row["CONTA"]
        valor = row["VALOR"]
        total = total_por_instituicao[
            total_por_instituicao["DESPESAS"] == despesas
        ]["VALOR"].values[0]
        df.loc[despesas, funcao] = valor
        df.loc[despesas, "TOTAL"] = total

    df = df.drop(
        columns=[
            "SEGURANÇA PÚBLICA",
            "ASSISTÊNCIA SOCIAL",
            "PREVIDÊNCIA SOCIAL",
            "SAÚDE",
            "EDUCAÇÃO",
        ]
    )
    df.fillna(0, inplace=True)
    df["TOTAL"] = df["TOTAL"] - df["10 - SAÚDE"]
    df = df.applymap(
        lambda x: locale.currency(x, grouping=True)
        if isinstance(x, (int, float))
        else x
    )
    # Remove as colunas desnecessárias
    return df


if __name__ == "__main__":
    criar_dataframe_por_municipio("PREFEITURA MUNICIPAL DE ABADIA DE GOIÁS - GO")
