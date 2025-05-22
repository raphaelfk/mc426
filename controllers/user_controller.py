from models.user import User

class UserController:
    def __init__(self):
        self.users = []

    def cadastrar_usuario(self, data):
        # Validações
        if not data.get('nome'):
            return {'erro': 'Nome é obrigatório'}, 400
        if not data.get('cpf') or not User.validar_cpf(data['cpf']):
            return {'erro': 'CPF inválido (deve conter 11 dígitos numéricos)'}, 400
        if not data.get('email') or not User.validar_email(data['email']):
            return {'erro': 'E-mail inválido'}, 400
        if not data.get('senha') or len(data['senha']) < 6:
            return {'erro': 'Senha deve ter no mínimo 6 caracteres'}, 400
        if data.get('atividade') not in ['caminhada', 'pedalada', 'ambos']:
            return {'erro': 'Tipo de atividade inválido'}, 400

        # Verificar se usuário já existe
        if self.buscar_por_email(data['email']):
            return {'erro': 'E-mail já cadastrado'}, 400
        if self.buscar_por_cpf(data['cpf']):
            return {'erro': 'CPF já cadastrado'}, 400

        # Criar novo usuário
        usuario = User(
            nome=data['nome'],
            cpf=data['cpf'],
            email=data['email'],
            senha=data['senha'],
            atividade=data['atividade']
        )
        
        self.users.append(usuario)
        return {'mensagem': 'Usuário cadastrado com sucesso!'}, 201

    def buscar_por_email(self, email):
        return next((user for user in self.users if user.email == email), None)

    def buscar_por_cpf(self, cpf):
        return next((user for user in self.users if user.cpf == cpf), None) 