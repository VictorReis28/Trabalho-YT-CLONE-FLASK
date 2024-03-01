from app import app
from flask import render_template
from model.video_model import videosModel

@app.route("/videos/<id>")
def videos(id):
    video = videosModel().get_video(id)
    comentarios = videosModel().get_comentarios()
    if video != None:
        return render_template("telaVideos.html", id=id, video=video, comentarios = comentarios)
    else:
        return render_template("404.html")
    
    
    
    