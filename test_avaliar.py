from avaliar import app, usuarios

# Inicializa os usuários aqui
usuarios[:] = [
  {
    'nome': 'Alice', 
    'cpf': '22289765398', 
    'email': 'alice.petlover@hotmail.com', 
    'senha': 'senha1234',
    'atividade': 'caminhada', 
    'avaliacoes': []
  },
  {
    'nome': 'Bob', 
    'cpf': '22289777781', 
    'email': 'boblu@hotmail.com', 
    'senha': 'se1234nha',
    'atividade': 'caminhada', 
    'avaliacoes': []
  },
  {
    'nome': 'Carol', 
    'cpf': '11122233345', 
    'email': 'carol@mail.com', 
    'senha': 'senhasegura',
    'atividade': 'pedalada', 
    'avaliacoes': []
  }
]


def test_avaliacao_valida():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 1,
    'nota': 5,
    'comentario': 'Muito bom'
  })
  assert resposta.status_code == 201
  assert resposta.get_json()['mensagem'] == 'Avaliação registrada com sucesso'


def test_sem_id_avaliador():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={})
  assert resposta.status_code == 400
  assert resposta.get_json()['erro'] == 'ID do avaliador é obrigatório'

def test_sem_id_avaliado():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
  })
  assert resposta.status_code == 400
  assert resposta.get_json()['erro'] == 'ID do avaliado é obrigatório'

def test_autoavaliacao():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 0,
    'nota': 4
  })
  assert resposta.status_code == 400
  assert resposta.get_json()['erro'] == 'Usuário não pode se autoavaliar'

def test_id_invalido():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 10,
    'nota': 4
  })
  assert resposta.status_code == 404
  assert resposta.get_json()['erro'] == 'Usuário não encontrado'

def test_atividade_diferente():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 2,
    'nota': 4
  })
  assert resposta.status_code == 400
  assert resposta.get_json()['erro'] == 'Compartilhamento da mesma rota é obrigatório'

def test_sem_nota():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 1
  })
  assert resposta.status_code == 400
  assert 'Nota' in resposta.get_json()['erro']

def test_nota_invalida():
  cliente = app.test_client()
  resposta = cliente.post('/avaliacao', json={
    'id_avaliador': 0,
    'id_avaliado': 1,
    'nota': 10
  })
  assert resposta.status_code == 400
  assert resposta.get_json()['erro'] == 'Nota deve ser entre 1 e 5'
