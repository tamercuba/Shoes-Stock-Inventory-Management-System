# Shoe Stock Inventory Management System
[![Generic badge](https://img.shields.io/badge/Python-3.7.3-Blue.svg)](https://docs.python.org/3/index.html) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

> Uma aplicação de controle de estoque de calçados construida sob arquitetura REST.

## Descrição

Escrito em Python + Django e utilizando o Django Rest Framework para a implementação da arquitetura REST, o SSIMS visa fornecer uma CRUD para gerenciar um sistema de estoque de calçados.

![Frontend](https://i.imgur.com/QKiFHfe.png)

## Features

A aplicação retorna valores JSON a partir dos seguintes endpoints:

Método HTTP | URL | Comportamento
------------|-----|---------------
`GET`| `'index'` | Frontend simples que lista os calçados
`POST`| `resources/csv_import/` | Recebe um arquivo `csv` com informações sobre os calçados e realiza a inserção
`GET` | `resources/` | Retorna lista paginada de calçados permitindo busca
`POST`| `resources/` | Adiciona um novo calçado
`GET` | `resources/id` | Retorna um calçado existente
`PUT` | `resources/id` | Altera as informações de um calçado existente
`PATCH` | `resources/id/` | Altera parcialmente as informações de um calçado existente
`DELETE` | `resources/id/` | Remove um calçado existente

## Tutorial de Instalação

1. Primeiramente crie um diretório raiz para o SSIMS no seu computador executando `mkdir SSIMS_ROOT` no seu terminal e entre no diretório com `cd SSIMS_ROOT`.
2. Caso não tenha, instale o `VirtualEnv` utilizando `pip install virtualenv` (lembre-se que o projeto utiliza Python 3, se o seu Sistema Operacional utilizar o 2 como padrão talvez você tenha que usar `pip3`)
3. Localize o diretório raiz do Python 3.7 na sua máquina executando `which python3.7`
4. Agora execute `virtualenv --python=/path/to/your/python3.7 .venv` (lembre-se de substituir /path/to/your/python3.7 pelo caminho descoberto na etapa anterior, note que você pode substituir o nome `.venv` para o nome que desejar) e ative o ambiente virtual rodando `source .venv/bin/activate` (para desativá-lo basta substituir o `source` por `deactivate`).
5. Execute agora `git clone https://github.com/tamercuba/Shoes-Stock-Inventory-Management-System.git` para clonar o repositório que ficará num diretório chamado `SSIMS` dentro do diretório raiz. Entre no diretório utilizando o comando `cd SSIMS`.
6. Para baixar as depêndencias execute `pip install -r requirements.txt`.
7. Execute `touch .env`, edite esse arquivo com seu editor e texto preferido colocando as seguintes informações:
```
NAME_DB= "NOME DO BANCO"
USER_DB= "NOME DO USUÁRIO"
PW_DB= "SENHA"
HOST_DB= "ENDEREÇO"
PORT_DB= "PORTA"
```
> Substitua os valores entre aspas (sem as aspas) com as informações necessárias de um banco de dados PostgreSQL.

8. Execute `./manage.py makemigrations` em seguida execute `./manage.py migrate`.
9. Agora você ja está pronto para rodar a aplicação com o comando `./manage runserver`

#### Exemplos de utilização

Ao requisitar `GET` na endpoint `resources/` você deverá receber algo parecido com isso:
```
{
    "count": 13,
    "next": "http://localhost:8000/resources/?page=2",
    "previous": null,
    "results": [
        {
            "_id": 5,
            "descricao": "Adidas Classic",
            "fornecedor": "ADIDAS",
            "tipo": "CS",
            "preco_custo": "101.00",
            "preco_venda": "300.00",
            "quantidade_total": 100,
            "estoque": [
                {
                    "tamanho": 37,
                    "quantidade": 3701
                },
                {
                    "tamanho": 36,
                    "quantidade": 3601
                },
            ]
        },
        {
            "_id": 9,
            "descricao": "Air Max Branco",
            "fornecedor": "NIKE",
            "tipo": "CS",
            "preco_custo": "200.00",
            "preco_venda": "550.00",
            "quantidade_total": 5070,
            "estoque": [
                {
                    "tamanho": 41,
                    "quantidade": 5000
                },
                {
                    "tamanho": 36,
                    "quantidade": 70
                }
            ]
        }
}
```

Para requisitar `POST` nessa mesma endpoint você deve enviar um JSON no formato acima, omitindo apenas os capos `'_id'`, `"quantidade_total"`.


Ao requisitar `GET` na endpoint `resources/6/` você deve receber algo semelhante a isso:
```
{
    "_id": 6,
    "descricao": "Havaianas Branco e Azul",
    "fornecedor": "Havaianas",
    "tipo": "CH",
    "preco_custo": "10.00",
    "preco_venda": "50.00",
    "quantidade_total": 990,
    "estoque": [
        {
            "tamanho": 38,
            "quantidade": 900
        },
        {
            "tamanho": 43,
            "quantidade": 90
        }
}

```
Para utilizar o verbo `PUT` você deve retornar o mesmo JSON acima com as alterações desejadas.

Para requisitar `PATCH` você deve enviar um JSON no seguinte formato:
```
{
    "descricao": Havaianas Tradicional Branco e Azul
}
```
Se quiser adicionar um novo tamanho ou alterar a quantidade em estoque basta enviar um JSON no seguinte formato
(ainda no verbo PATCH):

> Para deletar uma instancia de estoque basta atualizar a quantidade daquela numeração para 0

```
{
    "estoque": [
        {
            "tamanho": 39,                  # <- ADICIONA NOVA INSTANCIA
            "quantidade": 1000,
        },
        {
            "tamanho": 38,                  # <- ALTERA QUANTIDADE
            "quantidade": 899
        }
    ]
}
```
#### Busca

Para realizar a busca pelo endpoint `resources/` você deve adicionar um parâmetro `?campo1=valor1&campo2=valor2...`, podendo buscar por um ou mais campos.

Os campos disponíveis para busca são:
* `?descricao`: busca pela descrição exata do calçado.
* `?fornecedor`: busca pela descrição exata do fornecedor.
> Os campos de busca tipo texto podem ser refinados usando o parâmetro `__ll` antes do `=`, esse parâmetro refina a busca para campos que contém o texto digitado.

* `?tipo`: Busca pela sigla do tipo de calçado.
* `?preco_custo`: busca pelo preço de custo digitado.
* `?preco_venda`: busca pelo preço de venda digitado.
> Os campos de busca tipo numéricos podem ser refinados usando os parametros `__lt`/`__gt` para 'menor/maior que' e também `__lte/__gte` para 'menor/maior ou igual a'.

Exemplo: `/resources/?quantidade__lte=500&preco_venda__gt=150` retorna todos calçados que tem quantidade em estoque menor ou igual a `500` e preço de venda maior que `R$150,00`.


#### CSV Import

No diretório `static/TEMP` você encontrará um aquivo chamado `data_example.csv`. Nele você encontrará um `csv` com as seguintes colunas: `descricao,fornecedor,tipo,preco_custo,preco_venda,total,35,36,37,38,39,40,41,42,43,44,45`. As colunas numeradas recebem um valor de `0` a `1` indicando a porcentagem daquela numeração em estoque. O arquivo deve, necessáriamente ser renomeado para `data.csv` antes do envio.

Para enviar o arquivo `.csv` basta executar `curl -F file=@data.csv localhost:8000/resources/csv_import/`.


## Depêndencias

Pacote | Versão
------ | -------
Django | 2.2.1  
djangorestframework | 3.9.4  
pip | 19.1.1
psycopg2 | 2.8.2  
python-decouple | 3.1    
pytz | 2019.1
setuptools | 41.0.1
sqlparse | 0.3.0  
wheel | 0.33.4

## Versões

* MASTER - ATUAL
* [v0.2](https://github.com/tamercuba/Shoes-Stock-Inventory-Management-System/tree/v0.2)
* [v0.1](https://github.com/tamercuba/Shoes-Stock-Inventory-Management-System/tree/v0.1)

## Contato

* [LinkedIn](https://linkedin.com/in/tamercuba)
* [Facebook](https://www.fb.com/tamercuba)
* E-mail: `tamercuba@gmail.com`
