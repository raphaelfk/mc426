from app import app, usuarios

class TestAvaliacao(unittest.TestCase):
    def test_avaliacao_valida(self):
        response = self.client.post('/avaliacao', json={
            'id_avaliador': 0,
            'id_avaliado': 1,
            'avaliacao': 5,
            'comentario': 'Muito bom'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Avaliacao registrada com sucesso', response.data)

    def test_autoavaliacao(self):
        response = self.client.post('/avaliacao', json={
            'id_avaliador': 0,
            'id_avaliado': 0,
            'avaliacao': 4
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'autoavaliar', response.data)

    def test_atividade_diferente(self):
        response = self.client.post('/avaliacao', json={
            'id_avaliador': 0,
            'id_avaliado': 2,
            'avaliacao': 4
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'mesma rota', response.data)

    def test_nota_invalida(self):
        response = self.client.post('/avaliacao', json={
            'id_avaliador': 0,
            'id_avaliado': 1,
            'avaliacao': 10
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Nota deve ser entre 1 e 5', response.data)

    def test_id_invalido(self):
        response = self.client.post('/avaliacao', json={
            'id_avaliador': 0,
            'id_avaliado': 10,
            'avaliacao': 4
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Usuario nao encontrado', response.data)

if __name__ == '__main__':
    unittest.main()
