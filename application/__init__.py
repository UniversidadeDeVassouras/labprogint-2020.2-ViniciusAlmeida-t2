from flask import Flask 
import os
from application.model.dao.disciplinaDAO import disciplinaDAO

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


disciplinas = disciplinaDAO()

app.config ['disciplinas'] = disciplinas




from application.controller import home_controller