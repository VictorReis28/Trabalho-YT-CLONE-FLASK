from model.entity.canal import Canal
from model.entity.categoria import Categoria
from model.entity.video import Video
from model.entity.comentario import Comentario
from random import sample

class videosModel:

    def __init__(self):
        Lives_do_alanzoka = Canal(0,"Lives do alanzoka","3,03 MI","Canal oficial com as lives do Alanzoka. ",'/static/photos/LogoCanal1.jpg')
        Cortes_do_Casimito = Canal(1, "Cortes do casimito","3,43 MI","Cortes da live do Casimiro!",'/static/photos/LogoCanal2.jpg')
        Mc_Caverinha = Canal(2, "Mc Caverinha","2,1 MI","Caverinha okay?",'/static/photos/LogoCanal3.jpg')
        Hybe_Labels = Canal(3, "HYBE LABELS","70,7 MI","HYBE LABELS",'/static/photos/LogoCanal4.jpg')
        Fifty_fifty = Canal(4, "FIFTY FIFTY Official","1,14 MI","FIFTY FIFTY OFFICIAL ",'/static/photos/LogoCanal5.jpg')
        Curso_em_video = Canal(5, "Curso em video","2,03 MI","Curso em video",'/static/photos/LogoCanal6.jpg')
        Leviano = Canal(6,"Leviado","50,4 mil","Canal leviano",'/static/photos/LogoCanal7.jpg')

        jogos = Categoria(0,"Jogos","Categoria de jogos")
        react  = Categoria(1,"React","Categoria de Reacts")
        musica = Categoria(2,"Musica","Categoria de Musica")
        recomendado = Categoria(3,"Recomendado","Categoria de Recomendados")

        video1 = Video(1,Lives_do_alanzoka,"alanzoka jogando Zelda: Tears of the Kingdom - Parte #1","Jogando zeldinha",jogos,25024,124,"346 mil","/static/photos/img1.jpg","6 dias","https://www.youtube.com/embed/MTd_Nf2AzTk")
        video2 = Video(2,Lives_do_alanzoka,"alanzoka jogando Zelda: Tears of the Kingdom - Parte #2","Jogando zeldinha",jogos,9612,42,"139 mil","/static/photos/img2.jpg","6 dias","https://www.youtube.com/embed/lpheaVl1nt8")
        video3 = Video(3,Lives_do_alanzoka,"alanzoka jogando Zelda: Tears of the Kingdom - Parte #3","Jogando zeldinha",jogos,7452,62,"104 mil","/static/photos/img3.jpg","5 dias","https://www.youtube.com/embed/ZTWxU_ocMe4")
        video4 = Video(4,Lives_do_alanzoka,"alanzoka jogando Zelda: Tears of the Kingdom - Parte #4","Jogando zeldinha",jogos,8642,23,"166 mil","/static/photos/img4.jpg","5 dias","https://www.youtube.com/embed/_L3gTUlZcEE")
        video5 = Video(5,Lives_do_alanzoka,"alanzoka jogando Zelda: Tears of the Kingdom - Parte #5","Jogando zeldinha",jogos,3612,50,"500 mil","/static/photos/img11.jpg","7 dias","https://www.youtube.com/embed/z3ysLOtiG5Q")
        video6 = Video(6,Cortes_do_Casimito,"CASIMIRO REAGE: GRÊMIO 1 X 1 CRUZEIRO PELA COPA DO BRASIL 2023 | Cortes do Casimito","React grêmio e cruzeiro",react,18324,59,"208 mil","/static/photos/img5.jpg","1 dia","https://www.youtube.com/embed/EQ7IdHfMhqE")
        video7 = Video(7,Cortes_do_Casimito,"CASIMIRO REAGE: BALDASSO MUITO BRAVO! AMÉRICA-MG 2X0 INTER PELA COPA DO BRASIL | Cortes do Casimito","React América e Inter",react,19145,58,"280 mil","/static/photos/img6.jpg","1 dia","https://www.youtube.com/embed/OUUTva7TGnM")
        video8 = Video(8,Cortes_do_Casimito,"CASIMIRO FALA SOBRE MANCHESTER CITY 4X0 REAL MADRID - CHAMPIONS LEAGUE 2022/23 | Cortes do Casimito","React Manchester city e Real",react,31421,159,"336 mil","/static/photos/img7.jpg","8 dia","https://www.youtube.com/embed/c2LG8ChAWdM")
        video9 = Video(9,Cortes_do_Casimito,"CASIMIRO REAGE: DEFANTE COM BOCA DE 09 - PÃO COM PÃO ft. Neymar - RANGO BRABO | Cortes do Casimito","React com Boca de 09",react,44852,54,"624 mil","/static/photos/img8.jpg","2 dia","https://www.youtube.com/embed/AlzjpXW066A")
        video10 = Video(10,Cortes_do_Casimito,"CASIMIRO REAGE: SUSTOS COM DICAS EM HOMENAGEM AO DIA DO ENTREGADOR | Cortes do Casimito","React ao dia do entregador",react,17342,42,"78 mil","/static/photos/img9.jpg","1 dia","https://www.youtube.com/embed/p5g8m3Gya0Y")
        video11 = Video(11,Mc_Caverinha,"MC Caverinha, Kayblack - Cartão Black (Clipe Oficial)","Esse é o videoclipe oficial da faixa Cartão Black do MC Caverinha, Kayblack, Wall Hein.",musica,45500,500,"15 MI","/static/photos/img10.jpg","6 dia","https://www.youtube.com/embed/OZgQnRcGZXs")
        video12 = Video(12,Mc_Caverinha,"MC Caverinha - Evoque","Clipe Oficial",musica,99,200,"2 MI","/static/photos/img12.jpg","1 mês","https://www.youtube.com/embed/514I-7momNY")
        video13 = Video(13,Hybe_Labels,"LE SSERAFIM (르세라핌) 'UNFORGIVEN (feat. Nile Rodgers)' OFFICIAL M/V"," This content has been filmed under the full guidance of professional trainers and well-trained stunt horses.",musica,1028400,24021,"70,7 MI","/static/photos/img13.jpg","2 meses atrás","https://www.youtube.com/embed/UBURTj20HXI")
        video14 = Video(14,Leviano,"Kylie","Kylie · Leviano · Brandão85 · Tz da Coronel · Hash Produções · RUAN FRANCHI MOURA SILVA · GABRIEL BRANDÃO DA COSTA · Tz da Coronel",musica,20400,12601,"537.537 mil","/static/photos/img14.jpg","5 meses atrás","https://www.youtube.com/embed/gBXtlN9YDCw?list=OLAK5uy_kXzlTiWteODSDaSkiPDMpejzP-QXUNFK0")
        video15 = Video(15,Fifty_fifty,"FIFTY FIFTY (피프티피프티) - 'Cupid' Official MV","[ The 1st Single Album “The Beginning: Cupid]",musica,2470200,12010,"1 MI","/static/photos/img15.jpg","6 meses atrás","https://www.youtube.com/embed/Qc7_zRjH808")
        video16 = Video(16, Curso_em_video,"O que é Git? O que é versionamento? - Curso de Git e GitHub","Neste vídeo vamos entender o que é o Git e o que é versionamento de código.",recomendado,14020,144,"28.040 mil","/static/photos/img16.jpg","3 ano atrás","https://www.youtube.com/embed/xEKo29OWILE?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA")
        video17 = Video(17,Curso_em_video,"O que é GitHub? Pra que ele serve? - Curso de Git e GitHub","Neste vídeo vamos entender o que é o GitHub e para que ele serve.",recomendado,20450,31,"40.900 mil","/static/photos/img17.jpg","3 ano atrás","https://www.youtube.com/embed/hcZ0qtwvN1w?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA")
        video18 = Video(18,Curso_em_video,"A Evolução do Git e GitHub - Curso de Git e GitHub","Neste vídeo vamos entender como o Git e o GitHub evoluíram ao longo do tempo.",recomendado,27520,59,"68.800 mil","/static/photos/img18.jpg","3 ano atrás","https://www.youtube.com/embed/CJtrNuTTs4Q?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA")
        video19 = Video(19,Curso_em_video,"Instalações e configurações importantes - Curso de Git e GitHub","Neste vídeo vamos aprender a instalar e configurar o Git e o GitHub.",recomendado,20023,148,"40.046 mil","/static/photos/img19.jpg","3 ano atrás","https://www.youtube.com/embed/gMh6lrXibWY?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA")
        video20 = Video(20,Curso_em_video,"Criando o primeiro Repositório - Curso de Git e GitHub","Neste vídeo vamos aprender a criar o primeiro repositório no GitHub.",recomendado,32027,100,"96.081 mil","/static/photos/img20.jpg","3 ano atrás","https://www.youtube.com/embed/5BYm7UdCrX0?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA")

        self.video_list = [video16,video17,video18,video19,video20]
        self.video_list_j = [video1,video2,video3,video4,video5]
        self.video_list_m = [video11,video12,video13,video14,video15]
        self.video_list_r = [video6,video7,video8,video9,video10]

        comentario1 = Comentario ("Carlos", "Excelente vídeo! Adorei a forma como você explicou cada detalhe de maneira clara e concisa. Seus conhecimentos são impressionantes. Continue compartilhando seu talento conosco!")
        comentario2 = Comentario ("Ana", "Uau! Esse vídeo foi incrível! Fiquei maravilhada com a sua habilidade em transmitir informações de maneira tão envolvente. Parabéns pelo excelente trabalho!")
        comentario3 = Comentario ("Pedro", "Simplesmente sensacional! A maneira como você abordou o assunto me deixou fascinado. É nítido o seu domínio no tema. Mal posso esperar para ver mais vídeos seus!")
        comentario4 = Comentario ("Mariana", "Que vídeo fantástico! Sua didática é impecável e consegui entender tudo facilmente. Estou ansiosa para ver mais conteúdos como esse. Parabéns!")
        comentario5 = Comentario ("Lucas", "você sempre entrega vídeos de alta qualidade! Sua paixão pelo assunto é inspiradora e contagia quem assiste. Continue nos presenteando com esse excelente trabalho!")
        comentario6 = Comentario ("Carolina", "Incrível! Esse vídeo me ajudou a solucionar diversas dúvidas que eu tinha. Sua expertise no assunto é admirável. Obrigada por compartilhar seu conhecimento!")
        comentario7 = Comentario ("Gabriel", "Esse vídeo foi uma verdadeira aula! A maneira como você explora os detalhes e traz exemplos práticos é impressionante. Sem dúvida, um dos melhores canais sobre esse tema!")
        comentario8 = Comentario ("Luísa", "Parabéns pelo conteúdo enriquecedor! Seu vídeo me deixou empolgada para colocar em prática tudo o que aprendi. Continue nos surpreendendo com seu talento!")
        comentario9 = Comentario ("Rafael", "Esse vídeo merece todos os elogios! A forma como você articula as informações é cativante e fácil de acompanhar. Seu trabalho é simplesmente brilhante!")
        comentario10 = Comentario ("Juliana", "eu adoro assistir aos seus vídeos! A cada novo conteúdo, aprendo algo valioso. Sua dedicação em compartilhar conhecimento é inspiradora. Parabéns pelo excelente trabalho!")
        comentario11 = Comentario ("Gustavo", "Esse vídeo foi simplesmente fenomenal! Sua habilidade em explicar conceitos complexos de forma acessível é impressionante. Estou sempre ansioso pelo próximo conteúdo!")
        comentario12 = Comentario ("Isabela", "parabéns pelo seu canal incrível! Seus vídeos são informativos, interessantes e cheios de insights. É um prazer acompanhar seu trabalho e aprender com você!")
        comentario13 = Comentario ("Thiago", "Mais um vídeo incrível! Sua paixão pelo tema transparece em cada palavra. A clareza e a profundidade das informações são excepcionais. Continue assim!")
        comentario14 = Comentario ("Camila", "Adorei esse vídeo! A maneira como você traz exemplos práticos e situações reais torna o conteúdo muito mais envolvente. Parabéns pelo excelente trabalho!")
        comentario15 = Comentario ("Ricardo", "você é um verdadeiro mestre! Seus vídeos são fontes preciosas de conhecimento e inspiração. Agradeço por compartilhar seu talento conosco!")
        comentario16 = Comentario ("Mariana", "Excelente vídeo! Sua voz tranquila e segura transmite confiança e deixa a experiência de aprendizado ainda melhor. Continue produzindo conteúdos incríveis!")
        comentario17 = Comentario ("Felipe", "Esse vídeo é simplesmente fantástico! Sua habilidade em simplificar assuntos complexos é admirável. Obrigado por tornar o aprendizado tão prazeroso!")
        comentario18 = Comentario ("Larissa", "Incrível como você consegue transformar um tema aparentemente complicado em algo compreensível e interessante. Seus vídeos são verdadeiras aulas de excelência!")
        comentario19 = Comentario ("Eduardo", "Mais um vídeo incrível! Sua dedicação em pesquisar e trazer informações relevantes é notável. Seu canal é uma referência para todos que buscam conhecimento!")
        comentario20 = Comentario ("Patrícia", "Adoro seus vídeos! A qualidade da produção, aliada ao seu carisma e conhecimento, faz com que eu me sinta completamente engajada em cada tema abordado. Parabéns pelo trabalho excepcional!")
        comentario21 = Comentario ("Fernando", " você é um verdadeiro mestre na arte de transmitir conhecimento. Seus vídeos são didáticos, envolventes e repletos de insights valiosos. Parabéns pelo seu trabalho incrível!")
        comentario22 = Comentario ("Laura", "Esse vídeo me deixou completamente fascinada! Sua capacidade de simplificar conceitos complexos é impressionante. Aprendi muito e mal posso esperar pelos próximos conteúdos!")
        comentario23 = Comentario ("Rodrigo", "Parabéns por mais um vídeo brilhante! Sua paixão e entusiasmo pelo assunto são contagiantes. Continue inspirando e educando pessoas como eu!")
        comentario24 = Comentario ("Vanessa", "Seus vídeos são uma verdadeira fonte de inspiração! Sua expertise no tema e a forma como você o explora são admiráveis. Obrigada por compartilhar seu conhecimento conosco!")
        comentario25 = Comentario ("Alexandre", "Esse vídeo superou todas as minhas expectativas! A clareza das explicações e a maneira como você apresenta os exemplos práticos tornam o conteúdo extremamente acessível. Excelente trabalho!")
        comentario26 = Comentario ("Gabriela", "Adorei o seu vídeo! Sua habilidade em conectar teoria e prática é notável. Aprendi muito e já estou ansiosa pelo próximo conteúdo que você vai compartilhar!")
        comentario27 = Comentario ("Matheus", "Mais um vídeo sensacional! Seus insights e dicas são extremamente valiosos. É incrível como você consegue transmitir tanta informação de forma tão envolvente. Parabéns!")
        comentario28 = Comentario ("Letícia", "Seus vídeos são verdadeiras aulas magistrais! Sua didática é impecável e sua capacidade de prender a atenção do espectador é surpreendente. Obrigada por compartilhar seu talento!")
        comentario29 = Comentario ("Guilherme", "Esse vídeo me deixou sem palavras! Sua expertise no assunto é evidente e a forma como você transmite conhecimento é inspiradora. Continue nos brindando com esses conteúdos excepcionais!")
        comentario30 = Comentario ("Beatriz", "Simplesmente amei o seu vídeo! Você consegue transformar assuntos complexos em explicações claras e envolventes. É um prazer acompanhar seu canal e aprender com você!")

        self.comentarios_list = [comentario1,comentario2,comentario3,comentario4,comentario5,comentario6,comentario7,comentario8,comentario9,comentario10,comentario11,comentario12,comentario13,comentario14,comentario15,comentario16,comentario17,comentario18,comentario19,comentario20,comentario21,comentario22,comentario23,comentario24,comentario25,comentario26,comentario27,comentario28,comentario29,comentario30]
        
        
    def lista_video_recomendado(self): 
        videos = []
        for video in self.video_list:
            videos.append(video)
        return videos
    
    def lista_video_jogos(self): 
        videos_j = []
        for video in self.video_list_j:
            videos_j.append(video)
        return videos_j
    
    def lista_video_musica(self): 
        videos_m = []
        for video in self.video_list_m:
            videos_m.append(video)
        return videos_m
    
    def lista_video_react(self): 
        videos_r = []
        for video in self.video_list_r:
            videos_r.append(video)
        return videos_r
    
    def get_video(self, id):
        for video in self.video_list:
            if video.id == int(id):
                return video
        for video in self.video_list_j:
            if video.id == int(id):
                return video
        for video in self.video_list_m:
            if video.id == int(id):
                return video
        for video in self.video_list_r:
            if video.id == int(id):
                return video
            
    def get_comentarios(self):
        comentarios = sample(self.comentarios_list, 10)
        return comentarios
