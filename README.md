# sistemas_distribuidos_projeto_1
Projeto 1 para sistemas distribuídos.


# Como rodar
Considerando que já tem instalado o Python no computador e grpcio e protobuf:

`pip install grpcio`

`pip install protobuf`

### Utilizar o comando 
`py Sdserver.py`

Criar um cliente

### Utilizar o comando
`py Sdclient.py`

Criar as tasks do cliente


# Outras Informações

No arquivo SDclient.py contém o lado do painel do cliente, com um painel interativo, e é possível cadastrar os dados do cliente que serão salvos em um arquivo file_cliente.txt.

No arquivo SDserver.py contém o lado do servidor, com um painel interativo, e é possível cadastrar o cliente que será salvo em um arquivo file.txt.

No arquivo RWLock são as informações relacionadas ao Mutex, Writing, Reading e outros para arquivos.

No arquivo protos está relacionado as declarações utilizadas nos outros arquivos.
