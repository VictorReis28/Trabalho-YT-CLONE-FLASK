from app import app
from flask import render_template
from model.video_model import videosModel

@app.route("/")
def inicial():
    videos = videosModel().lista_video_recomendado()
    videos_j = videosModel().lista_video_jogos()
    videos_m = videosModel().lista_video_musica()
    videos_r = videosModel().lista_video_react()
    return render_template("telaInicial.html", video_list= videos,video_list_j= videos_j, video_list_m = videos_m, video_list_r = videos_r)