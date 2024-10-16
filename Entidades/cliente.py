from Entidades.abstractpessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: int, endereco: str, telefone: int):
        super().__init__(nome, idade, cpf, endereco, telefone)
        self.__pedidos = []

    def pedido_atual(self):
        return self.__pedidos[0]

    @property
    def pedidos(self):
        return self.__pedidos

    def realiza_pedido(self, data: str):
        from Entidades.pedido import Pedido
        if type(data) == str:
            pedido = Pedido(self, data)
            return pedido
        return None
