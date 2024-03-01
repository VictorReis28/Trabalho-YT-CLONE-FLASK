class Canal:
    def __init__(self, id, nome, inscritos, descricao, logocanal) -> None:
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.inscritos =  inscritos
        self.videos = []
        self.logocanal = logocanal