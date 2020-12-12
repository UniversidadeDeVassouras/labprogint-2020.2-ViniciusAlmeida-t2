from flask import current_app


class Trabalho:
    def __init__ (self, id, materia_trabalho, disciplina_id, professor_trabalho):
        self._id = id
        self._disciplina_id = disciplina_id
        self._materia_trabalho = materia_trabalho
        self._professor_trabalho = professor_trabalho



    def get_id (self):
        return self._id

    def get_materia_trabalho (self):
        return self._materia_trabalho

    def get_disciplina_id (self):
        return self._disciplina_id

    def get_professor_trabalho (self):
        return self._professor_trabalho



    def get_trabalho_disciplina_id (self):
        trabalhos = current_app.config ['trabalhos']
        trabalho_disciplina = []
        for i, trabalho in enumerate (trabalhos.get_listar_trabalho()):
            if trabalho.get_disciplina_id () == self.get_id():
                trabalho_disciplina.append (trabalho)
        return trabalho_disciplina
