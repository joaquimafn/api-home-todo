from fastapi import FastAPI

app = FastAPI()

#Authentication
@app.post('/auth/login')
def authLogin():
    return 'TODO: autenticar usando plataforma de autenticacao/autorizacao'

@app.post('/auth/register')
def authRegister():
    return 'TODO: registrar usando plataforma de autenticacao/autorizacao'

#Services
@app.get('/services')
def listServices():
    return 'TODO: listar servicos disponiveis na plataforma'

@app.post('/services')
def createServices():
    return 'TODO: criar de um novo serviço na plataforma'

#Requests
@app.get('/requests/{id}')
def listServices():
    return 'TODO: listar uma solicitacao especifica'

@app.post('/requests')
def createServices():
    return 'TODO: criar nova solicitacao ou orcamento de um servico'

#Reviews
@app.post('/reviews')
def listServices():
    return 'TODO: adicionar uma avaliacao de um prestador de servicos'
