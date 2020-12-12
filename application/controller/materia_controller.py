from application import app
from flask import render_template, request, current_app
from application.model.dao.disciplinaDAO import disciplinaDAO
from application.model.dao.aulaDAO import aulaDAO
from application.model.dao.provaDAO import provaDAO
from application.model.dao.trabalhoDAO import trabalhoDAO
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Aula import Aula
from application.model.entity.Prova import Prova
from application.model.entity.Trabalho import Trabalho




@app.route("/materia/<int:materia_id>")
def materia(materia_id):
    disciplinas = disciplinaDAO().buscar_disciplina(materia_id)

    provas = provaDAO().buscar(materia_id)
    
    aula = aulaDAO().buscar(materia_id)

    trabalhos = trabalhoDAO().buscar(materia_id)

    qtd_aula = len(aula.get_aula_disciplina_id())
    qtd_prova = len(provas.get_prova_disciplina_id())
    qtd_trabalho = len(trabalhos.get_trabalho_disciplina_id())

    return render_template("materias.html", aula = aula, qtd_aula = qtd_aula, provas = provas, qtd_prova = qtd_prova, disciplinas = disciplinas, trabalhos = trabalhos, qtd_trabalho = qtd_trabalho)
