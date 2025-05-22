class UserRepository:
    def __init__(self):
        self._usuarios = []
    
    def add(self, usuario):
        self._usuarios.append(usuario)
        return usuario
    
    def get_all(self):
        return self._usuarios.copy()  # Retorna cópia para evitar modificação externa
    
    def find_by_id(self, id):
        try:
            return self._usuarios[id]
        except IndexError:
            return None
    
    # Outros métodos necessários podem ser adicionados aqui
