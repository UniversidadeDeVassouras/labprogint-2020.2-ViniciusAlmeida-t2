from flask import current_app


class Aula:
    def __init__ (self, id, disciplina_aula, disciplina_id, disciplina_periodo):
        self._id = id
        self._disciplina_aula = disciplina_aula
        self._disciplina_periodo = disciplina_periodo



    def get_id (self):
        return self._id

    def get_disciplina_aula (self):
        return self._disciplina_aula

    def get_disciplina_id (self):
        return self._disciplina_id
    
    def get_disciplina_periodo (self):
        return self._disciplina_periodo



