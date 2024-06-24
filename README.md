# Desafio AAWZ 

Projeto para a entrega do desafio técnico em backend de automação

## Descrição

O projeto utiliza uma planilha CSV para calcular a comissão de vendedores, e fazer uma verificação no valor que foi pago aos funcionários. Além disso, também
gera um uma planilha com a quantidade de cotas de cada sócio

## Primeiros passos

### Instalação

* Clone o projeto com o comando git clone ```git@github.com:grodrigues04/Desafio-AWZ.git```

### Dependências

* Instale os pacotes de dependências usando:
```shell
$ pip install -r requirements/requirements.txt
```
* Caso você esteja no windons e se deparar com um problema de caminho, utilize o comando:

```shell
$ pip install -r requirements\requirements.txt
```

### Execução do programa

* Para alterar as variaveis de ambiente, copie o .env.example, crie um .env e remova os comentários do que deseja alterar 
* Coloque os arquivos de entrada na pasta "data/spreadsheets"
    * Nomeie o arquivo da planilha como "Vendas.xlsx", como no exemplo do projeto
    * Certifique de que a planilha vendas possui uma aba chamada "Vendas" e "Pagamentos"
    * Nomeie o arquivo de partnership como "Partnership.txt"
* Os arquivos de saídas vão ser salvos na pasta "data/output-spreadsheets"

## Autor

* Gustavo Bernardo Rodrigues | [linkedin](https://www.linkedin.com/in/gustavorodriguesb04/)
