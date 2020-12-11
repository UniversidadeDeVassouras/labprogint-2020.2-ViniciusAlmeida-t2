from application import app
from flask import render_template, request, current_app
from application.model.dao.disciplinaDAO import disciplinaDAO
from application.model.dao.aulaDAO import aulaDAO
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Aula import Aula




@app.route("/materia/<int:materia_id>")
def materia(materia_id):
    prova = current_app.config ['provas']
    provas = prova.buscar(materia_id)
    listar_prova = prova.get_listar_prova()
    aula = aulaDAO().buscar(materia_id)
    aulas = aulaDAO()
    listar_aula = aulas.get_listar_aula()
    qtd_aula = len(aula.get_aula_disciplina_id())
    qtd_prova = len(provas.get_prova_disciplina_id())
    return render_template("materias.html", aula = aula, listar_aula = listar_aula, qtd_aula = qtd_aula, provas = provas, listar_prova = listar_prova, qtd_prova = qtd_prova)
