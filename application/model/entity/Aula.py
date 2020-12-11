from flask import current_app


class Aula:
    def __init__ (self, id, disciplina_aula, disciplina_id, disciplina_periodo):
        self._id = id
        self._disciplina_aula = disciplina_aula
        self._disciplina_id = disciplina_id
        self._disciplina_periodo = disciplina_periodo



    def get_id (self):
        return self._id

    def get_disciplina_aula (self):
        return self._disciplina_aula

    def get_disciplina_id (self):
        return self._disciplina_id
    
    def get_disciplina_periodo (self):
        return self._disciplina_periodo

    
    def get_aula_disciplina_id (self):
        aulas = current_app.config ['aulas']
        aula_disciplina = []
        for i, aula in enumerate (aulas.get_listar_aula()):
            if aula.get_disciplina_id () == self.get_id():
                aula_disciplina.append (aula)
        return aula_disciplina


