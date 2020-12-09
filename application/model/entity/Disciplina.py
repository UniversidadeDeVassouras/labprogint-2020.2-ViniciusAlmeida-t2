from flask import current_app


class Disciplina:
    def __init__ (self, id, nome_disciplina, periodo_disciplina):
        self._id = id 
        self._nome_disciplina = nome_disciplina
        self._periodo_disciplina = periodo_disciplina


    
    def get_id (self):
        return self._id

    def get_nome_disciplina (self):
        return self._nome_disciplina

    def get_periodo_disciplina (self):
        return self._periodo_disciplina

