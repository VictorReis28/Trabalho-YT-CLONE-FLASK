from flask import Flask
import os

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

from controller.Home_controller import *
from controller.videos_controller import *