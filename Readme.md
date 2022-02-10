# Playbook: Python_SQLServer e Docker_Airflow_Postgres

Desenvolve duas aplicações distintas com uso da API do Twitter. A primeira realiza ETL no SQL Server através do driver ODBC. A outra trata os dados coletados na aplicação anterior, deposita-os no Postgres e cria uma view. O processo neste caso é orquestrado pelo Airflow em ambiente Docker. 

## Índice
- [Descrição](#Descrição)
- [Configuração](#Configuração)
- [Uso](#Uso)
    - [Para o ETL no SQLServer](#Para o ETL no SQLServer)
    - [Para utilizar a aplicação orquestrada pelo Airflow](#Para utilizar a aplicação orquestrada pelo Airflow)

# Descrição
#### Componentes utilizados:
* **Sistema operacional: windows 11 com Ubuntu 20.04 rodando em WSL2**
* **Python**
* **Docker**
* **Airflow**
* **Postgres**


# Configuração
A pasta docker-airflow-igti_desafio_final contém os requisitos de ambiente para rodar o projeto.
Necessário importar pacotes que serão utilizados no arquivo get_tweets.py e dags_twitter_postgres2.py.
Quaisquer aplicações não presentes necessárias a execução deverão ser baixadas. 

# Uso
#### Para o ETL no SQLServer:

* Necessário criar uma conta de desenvolvedor no Twitter para ter acesso as chaves "consumer" e "access" e inserí-las no "cadastro das chaves de acesso" do arquivo get_tweets.py.

* Ainda no arquivo get_tweets.py na função Main, o usuário poderá inserir o critério de busca, no exemplo deste projeto o filtro foi "Bolsonaro".

* Para geração do txt com os tweets coletados execute, no arquivo extrect_analyze.ipynb:
    python get_tweets.py.

* Os demais comandos irão: estruturar e criar um arquivo json, transformar os tweets em uma estrutura relacional analisável, fazer o tratamento do tweet e convertê-lo para um DataFrame e, por fim, irá fazer a ingestão de dados do twitter no SQLServer. 

* Abra o SGBD de sua preferência para consumo dos dados.

#### Para utilizar a aplicação orquestrada pelo Airflow:

Inicie o docker:
    
    sudo service docker start

Navegue até a pasta onde se encontra o ambiente e execute:
    
    docker-compose -f docker-compose-CeleryExecutor.yml up -d --scale worker=2

O ambiente é escalável, nesta aplicação foram utilizados 2 "workers".

A configuração define o Airflow no http://localhost:8080/ .

* No ambiente, crie uma pasta com nome "data" e Execute a DAG

<p align="center">
<img src="https://github.com/LeandroRFausto/ETL_postgres_sqlserver_docker-Twitter/blob/main/tweet_postgres_airflow%20-%20docker/GraphView_dag.png" alt="Image" height="300" width="600"/>
</p>

* O Graph View deverá demonstrar todos os trabalhos em verde. Quando o status for "success", abra o SGBD de sua preferência, lá estarão uma tabela e um View.  

* O Airflow terá: separado todos os tweets em arquivos json e salvado na pasta data. Neste projeto, foram salvos 1940 arquivos json; executado um sensor de arquivo que certifica a existência de um dado; lido cada um dos json e exportado para csv já processado(pandas); listado o que está no ambiente; juntado todos os csv's; escrito a tabela no Postgres e criado uma View. Conforme arquivos table.sql e view.sql salvos no projeto.  
