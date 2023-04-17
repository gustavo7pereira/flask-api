from flask_restx import fields
from src.server.instace import server


book = server.api.model('Book', {
    'id': fields.String(description='O ID do registro.'),
    'title': fields.String(required=True, description='O titulo do livro.')
})