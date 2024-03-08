# Sistema de Cadastro de Pessoas

Este é um sistema simples de cadastro de pessoas que permite inserir, listar, buscar e remover pessoas a partir de um arquivo de texto chamado `pessoas.txt`. O programa é executado no terminal e oferece as seguintes funcionalidades:

## Funcionalidades

1. **Inserir Pessoa:** Permite inserir uma nova pessoa com informações como nome, CPF, endereço e telefones associados.

2. **Listar Pessoas Cadastradas:** Lista todas as pessoas cadastradas no sistema, exibindo nome, CPF, endereço e telefones associados.

3. **Buscar Pessoa por CPF:** Busca e exibe as informações de uma pessoa a partir do CPF fornecido.

4. **Buscar Pessoa por Telefone:** Busca e exibe as informações de uma pessoa a partir do telefone fornecido.

5. **Remover Pessoa por CPF:** Remove uma pessoa do sistema a partir do CPF fornecido.

## Estrutura do Arquivo de Dados

O arquivo de dados `pessoas.txt` segue a seguinte estrutura: `nome;cpf;endereco;qntd_telefones;telefones`

- `nome`: Nome da pessoa.
- `cpf`: CPF da pessoa (identificador único).
- `endereco`: Endereço da pessoa.
- `qntd_telefones`: Quantidade de telefones associados à pessoa.
- `telefones`: Lista de telefones associados à pessoa.