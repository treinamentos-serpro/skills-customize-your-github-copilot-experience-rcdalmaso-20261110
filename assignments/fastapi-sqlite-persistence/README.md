# 📘 Assignment: Persistência de Dados com SQLite

## 🎯 Objective

Atualize uma API FastAPI para armazenar seus itens em um banco SQLite em vez de mantê-los apenas na memória. Você praticará consultas SQL e persistência de dados usando `sqlite3`, que faz parte da biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Consultar Itens no SQLite

#### Descrição
Prepare o banco SQLite e substitua as rotas de leitura do catálogo para consultar os dados armazenados. Instale as dependências da API com `python -m pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma tabela `items` com ID, nome, descrição e preço
- Inserir os itens de exemplo somente quando a tabela ainda estiver vazia
- Implementar `GET /items` e `GET /items/{item_id}` usando consultas SQL
- Retornar código HTTP `404` quando o item solicitado não existir
- Manter os itens disponíveis depois de reiniciar o servidor


### 🛠️ Persistir Alterações da API

#### Descrição
Atualize as rotas de criação, edição e remoção para usar o banco SQLite. Faça cada operação de escrita dentro de uma transação e confirme o resultado consultando novamente a API.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` usando `INSERT` e retornar o ID gerado pelo SQLite
- Implementar `PUT /items/{item_id}` usando `UPDATE` e retornar `404` se o item não existir
- Implementar `DELETE /items/{item_id}` usando `DELETE` e retornar `404` se o item não existir
- Persistir as alterações mesmo depois de reiniciar o servidor
- Confirmar criação, edição, remoção e tratamento de IDs inexistentes pela documentação em `/docs`