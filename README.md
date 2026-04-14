# Painel-eleitoral-2022
Painel Eleitoral Brasil 2022

Visão Geral do Projeto

O Painel Eleitoral Brasil 2022 é uma aplicação web interativa desenvolvida para visualizar e analisar os dados das eleições brasileiras de 2022. Este projeto foi criado com o objetivo de transformar grandes volumes de dados brutos do Tribunal Superior Eleitoral (TSE) em informações acessíveis e compreensíveis, permitindo a exploração dos resultados de votação por candidato, município e zona eleitoral.

Funcionalidades

•
Visualização Interativa: Apresenta os resultados eleitorais de forma dinâmica e intuitiva.

•
Filtros de Dados: Permite filtrar os dados por turno, estado e cargo, facilitando a análise específica.

•
Análise de Votos: Exibe a quantidade de votos nominais para cada candidato em diferentes níveis geográficos.

Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

•
Python: Linguagem de programação principal, conhecida por sua versatilidade e ecossistema robusto para análise de dados e desenvolvimento web.

•
Flask: Um microframework web para Python, utilizado para construir o backend da aplicação, gerenciar as rotas e servir as páginas HTML.

•
Pandas: Biblioteca fundamental para manipulação e análise de dados. Essencial para a leitura do arquivo CSV do TSE, filtragem, agregação e preparação dos dados para visualização.

•
Plotly: Biblioteca de visualização de dados que permite a criação de gráficos interativos e dinâmicos, incorporados diretamente nas páginas web.

•
Jinja2: Motor de templates para Python, utilizado para renderizar as páginas HTML dinamicamente, integrando os dados processados pelo Flask e Pandas.

•
HTML/CSS: Para a estruturação e estilização do frontend da aplicação, garantindo uma interface de usuário responsiva e agradável.

Estrutura do Projeto

Plain Text


Painel-Eleitoral-Brasil-2022/
├── app.py                  # Lógica principal da aplicação Flask, rotas e inicialização
├── models/
│   ├── __init__.py
│   ├── analyzer.py         # Lógica de análise e agregação dos dados eleitorais
│   ├── chart_builder.py    # Funções para construção dos gráficos Plotly
│   └── data_loader.py      # Responsável pelo carregamento e pré-processamento dos dados do TSE
├── static/                 # Arquivos estáticos (CSS, JavaScript, imagens)
│   ├── css/
│   └── js/
├── templates/              # Arquivos HTML para o frontend da aplicação
│   └── index.html
└── requirements.txt        # Lista de dependências Python do projeto



Dados Eleitorais do TSE

Os dados utilizados neste projeto são provenientes do Tribunal Superior Eleitoral (TSE) e correspondem à votação nominal por candidato, município e zona das eleições de 2022.

Arquivo de Dados

O arquivo principal de dados é votacao_candidato_munzona_2022.zip, que contém um CSV com as informações detalhadas dos votos. Devido ao seu grande volume, este arquivo não está incluído no repositório GitHub.

Download e Preparação

Para executar o projeto, você precisará baixar o arquivo de dados e colocá-lo em uma pasta data/ na raiz do projeto. Siga os passos:

1.
Crie a pasta data/: Na raiz do seu clone do repositório, crie uma pasta chamada data.

2.
Baixe os dados: Faça o download do arquivo votacao_candidato_munzona_2022.zip diretamente do site do TSE:
https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2022.zip

3.
Extraia e coloque o CSV: Descompacte o arquivo ZIP e coloque o arquivo CSV resultante (provavelmente votacao_candidato_munzona_2022_BR.csv ou similar) dentro da pasta data/.

Colunas Utilizadas (Exemplos)

O data_loader.py seleciona colunas específicas para otimizar o carregamento e a análise. Algumas das colunas-chave incluem:

•
NR_TURNO: Número do turno (1º ou 2º).

•
SG_UF: Sigla da Unidade da Federação (Estado).

•
NM_MUNICIPIO: Nome do Município.

•
DS_CARGO: Descrição do Cargo (e.g., Presidente, Governador).

•
NM_CANDIDATO: Nome do Candidato.

•
QT_VOTOS_NOMINAIS: Quantidade de votos nominais recebidos.

Como Executar o Projeto

1.
Clone o repositório:

Bash


git clone https://github.com/albernazz/Painel-Eleitoral-Brasil-2022.git
cd Painel-Eleitoral-Brasil-2022





2.
Crie e ative um ambiente virtual (recomendado ):

Bash


python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate





3.
Instale as dependências:

Bash


pip install -r requirements.txt





4.
Prepare os dados: Siga as instruções na seção "Dados Eleitorais do TSE" para baixar e posicionar o arquivo CSV.

5.
Execute a aplicação Flask:

Bash


python app.py





6.
Acesse o painel: Abra seu navegador e acesse http://127.0.0.1:5000/.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e novas funcionalidades.

Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


