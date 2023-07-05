
class BaseException(Exception):

    @property
    def serializer(self):
        return {
            'message': getattr(self, 'message', 'Problema interno.')
        }


class DadosInvalidosError(BaseException):

    def __init__(self, message="Dados inválidos."):
        self.message = message
        super().__init__(self.message)
