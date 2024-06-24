# Desafio AAWZ 

Projeto para a entrega do desafio técnico em backend de automação

## Descrição

O projeto utiliza uma planilha CSV para calcular a comissão de vendedores, e fazer uma verificação no valor que foi pago aos funcionários. Além disso, também
gera um uma planilha com a quantidade de cotas de cada sócio

## Primeiros passos

### Instalação

* Clone o projeto com o comando git clone ```git@github.com:grodrigues04/Desafio-AWZ.git```
* Entre dentro da pasta "desafio-AWZ"

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

* Para alterar as variáveis de ambiente, copie o .env.example, crie um .env e remova os comentários do que deseja alterar.

* Coloque os arquivos de entrada na pasta "data/spreadsheets"
    * Nomeie o arquivo da planilha como "Vendas.xlsx", como no exemplo do projeto
    * Nomeie o arquivo de partnership como "Partnership.txt"
    * Certifique de que a planilha vendas possui uma aba chamada "Vendas" e "Pagamentos"

* Execute o arquivo main.py para gerar os resultados.
* Os arquivos de saídas vão ser salvos na pasta "data/output-spreadsheets".

## Possiveis melhorias:

 * Testes: Devido ao limite de tempo, não foi possivel adicionar testes ao programa. Entretanto, testes são uma ótima prática, pois garantem um código robusto e eficiente, facilitando o tratamento de erros e aumentando a confiabilidade do código.

 * Interface Gráfica: Levando em consideração que o código seria utilizado por um departamento onde o foco não é a tecnologia, a interface gráfica é uma excelente maneira de garantir que qualquer pessoa da empresa seja capaz de utilizar, sem conhecimentos prévios em programação.

 * Tratamento de exceções: Apesar de ter sido implementado, o tratamento de exceções poderia ter sido feito com exceções mais específicas, facilitando a manutenção e correção de eventuais bugs. Isso contribuiria para uma identificação mais precisa das falhas no código e permitiria uma resposta mais direcionada a cada tipo de erro, aumentando a eficiência do sistema como um todo. Além disso, oferece uma mensagem de erro mais amigável ao usuário que deseja utilizar o sistema.
## Autor

* Gustavo Bernardo Rodrigues | [linkedin](https://www.linkedin.com/in/gustavorodriguesb04/)
