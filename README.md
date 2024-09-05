# HomeService API

**Descrição**  
Esta API foi desenvolvida em Python para servir como backend de um aplicativo de solicitação de serviços domésticos, permitindo que usuários busquem prestadores de serviço, solicitem orçamentos, agendem serviços e acompanhem suas solicitações.

## Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI** - Framework para criação de APIs rápidas e modernas
- **SQLAlchemy** - ORM para interação com o banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Docker** - Para facilitar o deploy e gerenciamento de dependências
- **Pydantic** - Para validação e gerenciamento de dados

## Funcionalidades

1. **Cadastro de Usuários e Prestadores de Serviço**  
   - Criação de usuários (clientes) e prestadores de serviços (ex: faxineiras, jardineiros).

2. **Autenticação e Autorização**  
   - Login via token JWT.

3. **Busca de Prestadores de Serviço**  
   - Filtrar prestadores por categoria de serviço, localização e preço.

4. **Solicitação de Orçamento**  
   - Usuários podem solicitar orçamentos diretamente a prestadores.

5. **Agendamento de Serviços**  
   - Permite que usuários agendem serviços e recebam confirmações.

6. **Acompanhamento de Solicitações**  
   - Os usuários podem verificar o status dos serviços solicitados.

7. **Avaliação de Prestadores**  
   - Avaliação e comentários para prestadores após a conclusão do serviço.

## Instalação

### Pré-requisitos

- Python 3.9+
- Docker
- PostgreSQL

### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/homeservice-api.git
   cd homeservice-api

2. Crie um ambiente virtual e ative-o:

   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
   
   ```bash
   pip install -r requirements.txt

4. Crie um arquivo .env baseado no .env.example e configure as variáveis de ambiente, como credenciais do banco de dados.

5. Execute as migrações do banco de dados:
   
   ```bash
   alembic upgrade head

6. Execute a aplicação:

    ```bash
    uvicorn app.main:app --reload

