from flask import Flask 
import os
from application.model.dao.disciplinaDAO import disciplinaDAO
from application.model.dao.aulaDAO import aulaDAO
from application.model.dao.provaDAO import provaDAO
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Aula import Aula
from application.model.entity.Prova import Prova

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


disciplinas = disciplinaDAO()
aulas = aulaDAO()
provas = provaDAO()

app.config ['disciplinas'] = disciplinas
app.config ['aulas'] = aulas
app.config ['provas'] = provas





from application.controller import home_controller
from application.controller import materia_controller