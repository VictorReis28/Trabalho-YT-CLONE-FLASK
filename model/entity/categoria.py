class Categoria:
    def __init__(self, id, nome, descricao) -> None:
        self.id = id
        self.nome = nome
        self.videos = []
        self.descricao = descricao