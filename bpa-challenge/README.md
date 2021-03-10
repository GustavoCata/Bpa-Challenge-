
## Execução do projeto
#### Download 

```
$ git clone https://github.com/Gustavo-Cata/bpa-challenge.git
```
#### Configuração do ambiente:

- Crie um ambiente virtual com seu sistema de gerenciamento favorito (conda, pyenv, virtualenv, etc);

- Ative o ambiente criado

#### Instalar dependências
<pre><code> $ pip install -r requirements.txt </code></pre>

Executar projeto:

<pre><code> $ python main.py </code></pre>

### Descrição do desáfio
O desáfio consiste em fazer em Python um programa que navega no site da Amazon, pesquisa o termo IPHONE, pegue todos os resultados da primeira página e para cada um, grava uma linha em um arquivo excel, com o nome do produto e o preço.


### Solução
A solução utilizada para este teste foi utilizando as bibliotecas as seguintes bibliotecas: selenium(para navegação nas páginas e coleta dos dados), pandas(para manipulação dos dados obtidos) e xlrwiter(gravação dos dados em xlsx).
