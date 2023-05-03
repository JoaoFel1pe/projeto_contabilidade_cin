# Desenvolvimento de Algoritmo para Extração de Dados Financeiros

Este projeto é uma atividade acadêmica desenvolvida por uma equipe de alunos da disciplina de Contabilidade de Custos e Gerencial, do curso de Sistemas de Informação da UFPE. O objetivo é desenvolver um algoritmo capaz de extrair dados financeiros de municípios e estados da federação do arquivo "FINBRA_Municípios_Despesas por Função_2019.xlsx", gerando relatórios específicos para cada função orçamentária.

## Funcionalidades
Funções Orçamentárias:
  - 06 SEGURANÇA PÚBLICA
  - 08 ASSISTÊNCIA SOCIAL 
  - 09 PREVIDÊNCIA SOCIAL
  - 10 SAÚDE
    - 10.301 - Atenção Básica 
    - 10.302 - Assistência Hospitalar e Ambulatorial
    - 10.303 - Suporte Profilático e Terapêutico
    - 10.304 - Vigilância Sanitária
    - 10.305 - Vigilância Epidemiológica
    - 10.306 - Alimentação e Nutrição.
  - 12 EDUCAÇÃO
  
O algoritmo desenvolvido neste projeto será capaz de extrair as seguintes informações para cada função orçamentária:

- Despesas Empenhadas
- Despesas Liquidadas
- Despesas Pagas
- Restos a Pagar Não Processados
- Restos a Pagar Processados

As informações serão apresentadas por estado da federação somente ou por estado e função orçamentária, permitindo uma análise detalhada dos gastos públicos em cada região.

## Tecnologias Utilizadas

O projeto será desenvolvido em Python. Para rodá-lo, instale o python e as seguintes bibliotecas:

- pandas: para a leitura e manipulação do arquivo "FINBRA_Municípios_Despesas por Função_2019.xlsx"

## Instalação e Uso

Primeiramente, instale o Git e o Python 3.9 no seu computador

- git: https://git-scm.com/download/
- Python: https://www.python.org/downloads/release/python-390/

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/JoaoFel1pe/projeto_contabilidade_cin.git
```

2. Instale as dependências do projeto utilizando o gerenciador de pacotes pip:

```bash
pip install -r requirements.txt
```

3. Execute o arquivo principal do projeto:

```bash
python src/main.py
```

4. Serão utilizadas 3 pastas para esse projeto:
- src: onde o código principal e os demais estarão alocados
- data: onde ficará o arquivo excel a ser lido, permitindo a reutilização desse algoritmo com outras planilhas
- reports: onde serão armazenados os relatórios gerados

## Contribuição

Para fazer alterações nesse projeto, faça o commit falando quais foram as alterações feitas e então dê o push direto na branch main

```bash
git push origin main
```

## Autores

- João Felipe (jfbs@cin.ufpe.br)
- Angel Lima (awrl@cin.ufpe.br)
- Diego França (drgf@cin.ufpe.br)
- Gabriel Sousa (gmcs@cin.ufpe.br)
- José Gervásio (jgbcn@cin.ufpe.br)

## Licença

Este projeto é licenciado sob a licença MIT - consulte o arquivo LICENSE.md para obter mais detalhes.
