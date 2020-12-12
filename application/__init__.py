from flask import Flask 
import os
from application.model.dao.disciplinaDAO import disciplinaDAO
from application.model.dao.aulaDAO import aulaDAO
from application.model.dao.provaDAO import provaDAO
from application.model.dao.trabalhoDAO import trabalhoDAO
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Aula import Aula
from application.model.entity.Prova import Prova
from application.model.entity.Trabalho import Trabalho

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


disciplinas = disciplinaDAO()
aulas = aulaDAO()
provas = provaDAO()
trabalhos = trabalhoDAO()

app.config ['disciplinas'] = disciplinas
app.config ['aulas'] = aulas
app.config ['provas'] = provas
app.config ['trabalhos'] = trabalhos




from application.controller import home_controller
from application.controller import materia_controller