# Desenvolvimento de Algoritmo para Extração de Dados Financeiros

Este projeto é uma atividade acadêmica desenvolvida por uma equipe de alunos da disciplina de Contabilidade de Custos e Gerencial, do curso de Sistemas de Informação da UFPE. O objetivo é desenvolver um algoritmo capaz de extrair dados financeiros de municípios e estados da federação do arquivo "FINBRA_Municípios_Despesas por Função_2019.xlsx", gerando relatórios específicos para cada função orçamentária.

## Funcionalidades

O algoritmo desenvolvido neste projeto será capaz de extrair as seguintes informações para cada função orçamentária:

- Despesas Empenhadas
- Despesas Liquidadas
- Despesas Pagas
- Restos a Pagar Não Processados
- Restos a Pagar Processados

As informações serão apresentadas por município e estado da federação, permitindo uma análise detalhada dos gastos públicos em cada região.

## Tecnologias Utilizadas

O projeto será desenvolvido em Python, utilizando as seguintes bibliotecas:

- pandas: para a leitura e manipulação do arquivo "FINBRA_Municípios_Despesas por Função_2019.xlsx"
- reportlab: para a geração de relatórios em PDF

## Instalação e Uso

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seunome/seuprojeto.git
```

2. Instale as dependências do projeto utilizando o gerenciador de pacotes pip:

```bash
pip install pandas reportlab
```

3. Execute o arquivo principal do projeto:

```bash
python main.py
```

4. Siga as instruções exibidas no terminal para escolher a função orçamentária desejada e gerar o relatório correspondente.

## Contribuição

Contribuições para o desenvolvimento deste projeto são sempre bem-vindas! Para contribuir, siga as instruções abaixo:

1. Faça um fork deste repositório
2. Crie uma nova branch com suas alterações:

```bash
git checkout -b minha-feature
```

3. Faça o commit das suas alterações:

```bash
git commit -m 'Adicionando uma nova feature'
```

4. Faça o push para a sua branch:

```bash
git push origin minha-feature
```

5. Abra um pull request para este repositório

## Autores

- João Silva (joaosilva@email.com)
- Maria Santos (mariasantos@email.com)
- José Oliveira (joseoliveira@email.com)

## Licença

Este projeto é licenciado sob a licença MIT - consulte o arquivo LICENSE.md para obter mais detalhes.
