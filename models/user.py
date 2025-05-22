class User:
    def __init__(self, nome, cpf, email, senha, atividade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.atividade = atividade
        self.avaliacoes = []

    @staticmethod
    def validar_email(email):
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def validar_cpf(cpf):
        import re
        return re.match(r"\d{11}$", cpf)

    def to_dict(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'senha': self.senha,
            'atividade': self.atividade,
            'avaliacoes': self.avaliacoes
        } 