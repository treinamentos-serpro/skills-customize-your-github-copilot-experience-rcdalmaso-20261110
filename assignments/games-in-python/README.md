
# 📘 Assignment: Games in Python

## 🎯 Objective

Crie um jogo da Forca em Python no qual a pessoa jogadora tenta descobrir uma palavra secreta, uma letra por vez. Você praticará strings, listas, seleção aleatória, condicionais, loops e entrada de dados.

## 📝 Tasks

### 🛠️ Prepare o estado do jogo

#### Descrição

Use a lista de palavras fornecida no código inicial para escolher a palavra secreta e inicializar as variáveis que controlam a partida.

#### Requisitos

O programa deve:

- Selecionar uma palavra aleatoriamente da lista `words`.
- Inicializar uma coleção de letras já tentadas, o número de erros e o limite de erros.
- Exibir o progresso da palavra oculta, mostrando as letras descobertas e espaços para as letras ainda não descobertas.

### 🛠️ Implemente a partida

#### Descrição

Complete o loop principal para receber palpites, atualizar o estado do jogo e encerrar a partida quando houver vitória ou quando o limite de erros for atingido.

#### Requisitos

O programa concluído deve:

- Solicitar um palpite de letra e informar se ele aparece na palavra secreta.
- Atualizar e exibir o progresso após cada palpite.
- Contabilizar palpites incorretos até o limite definido.
- Encerrar quando todas as letras forem descobertas ou os erros permitidos acabarem.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.