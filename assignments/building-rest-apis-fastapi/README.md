# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI para consultar e gerenciar um catálogo de itens. Você praticará rotas HTTP, validação de dados com Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar Rotas de Leitura

#### Descrição
Use o código inicial para criar uma API que liste os itens do catálogo e consulte um item pelo ID. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`. A documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /items` para retornar todos os itens como uma lista JSON
- Implementar `GET /items/{item_id}` para retornar o item correspondente ao ID
- Retornar o código HTTP `404` quando o ID solicitado não existir
- Confirmar as duas rotas pela documentação interativa do FastAPI


### 🛠️ Implementar Operações CRUD

#### Descrição
Adicione as rotas para criar, atualizar e remover itens. Use o modelo Pydantic fornecido para validar os dados recebidos e mantenha o catálogo atualizado enquanto a aplicação estiver em execução.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` para criar um item e retornar o item criado com um ID e código HTTP `201`
- Implementar `PUT /items/{item_id}` para substituir os dados de um item existente
- Implementar `DELETE /items/{item_id}` para remover um item existente e retornar código HTTP `204`
- Retornar código HTTP `404` ao tentar atualizar ou remover um ID inexistente
- Rejeitar preços menores ou iguais a zero usando a validação do modelo Pydantic
- Verificar os casos de sucesso e de erro pela documentação interativa do FastAPI