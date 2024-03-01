class Video:
    def __init__(self, id, canal, nome, descricao, categoria, likes, deslikes,visualizacoes, tumb, dia, link) -> None:
        self.id = id
        self.canal = canal
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.likes = likes
        self.deslikes = deslikes
        self.visualizacoes = visualizacoes
        self.comentarios = []
        self.tumb = tumb
        self.dia = dia
        self.link = link
