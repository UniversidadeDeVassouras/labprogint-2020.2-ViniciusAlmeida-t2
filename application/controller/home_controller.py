from application import app
from flask import render_template, request, current_app
from application.model.dao.disciplinaDAO import disciplinaDAO
from application.model.entity.Disciplina import Disciplina


@app.route("/")
def home():
    disciplinas = current_app.config ['disciplinas']
    exibir_disciplina = disciplinas.get_lista_disciplina()
    return render_template('index.html', exibir_disciplina = exibir_disciplina)
