from flask import current_app


class Prova:
    def __init__ (self, id, materia_prova, disciplina_id, professor_prova):
        self._id = id
        self._materia_prova = materia_prova
        self.professor_prova = professor_prova



    def get_id (self):
        return self._id

    def get_materia_prova (self):
        return self._materia_prova

    def get_disciplina_id (self):
        return self._disciplina_id

    def get_professor_prova (self):
        return self.get_professor_prova

