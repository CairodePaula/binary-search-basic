📘 Projeto: Árvore Binária de Busca (BST) com Leitura de Arquivo

Este projeto implementa a lógica de leitura de números a partir de um arquivo de texto e utiliza busca binária para localizar um valor informado pelo usuário.
Ele foi desenvolvido como parte da disciplina Estruturas de Dados, com base no fluxograma fornecido para o processo de busca em uma Árvore Binária de Busca (BST).

📂 Estrutura do Projeto
/ProjetoBST
│
├── numeros.txt        # Arquivo contendo números (um por linha)
├── main.py            # Código principal do programa
└── README.md          # Documentação do projeto

📑 Objetivo

O objetivo é:

Ler valores de um arquivo texto.

Realizar uma busca eficiente pelo número fornecido pelo usuário.

Utilizar o algoritmo de busca binária, inspirado no fluxograma de busca em árvore binária.

Exibir a posição do número caso ele exista na lista.

📥 Entrada

Um arquivo chamado numeros.txt, contendo números inteiros, um por linha.
Exemplo:

5
18
22
40
65
71


O usuário deve digitar, via teclado, o número que deseja procurar.

📤 Saída

Caso o número exista no vetor:

O número X está na posição Y.


Caso não exista:

Número não encontrado.

# Como Executar

Abra o projeto no Visual Studio ou VS Code.

Certifique-se de ter o arquivo numeros.txt na mesma pasta do código.

Execute o script principal:

python main.py


Digite o número que deseja procurar quando solicitado.

🧠 Lógica do Programa
✔ Leitura do arquivo

O programa lê o arquivo e converte cada linha em um número inteiro.

✔ Busca Binária Recursiva

A função divide a lista repetidamente até encontrar o valor procurado.
Caso a lista fique vazia, o elemento não existe.

✔ Base no Fluxograma

O código segue a ideia do fluxograma apresentado para busca em árvore, verificando:

Se o elemento atual é o alvo

Se o alvo é menor ou maior

Movendo para esquerda ou direita conforme necessário

# Requisitos

Python 3.8 ou superior

Visual Studio ou VS Code

Arquivo numeros.txt com números válidos

