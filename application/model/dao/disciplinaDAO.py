from flask import current_app

from application.model.entity.Aula import Aula
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Prova import Prova



class disciplinaDAO:
    def __init__(self):
       self._lista_disciplina = []
       self._lista_disciplina.append(Disciplina(1, "Laboratorio de Interface com o Usuario", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(2, "Sistemas Operacionais", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(3, "Modelagem de Banco de Dados", "4º Periodo"))

    def get_lista_disciplina (self):
        return self._lista_disciplina
    


    def buscar_disciplina (self, id):
        disciplina = None
        for index, disciplinas in enumerate(self.get_lista_disciplina()):
            if disciplinas.get_id() == id:
                disciplina = disciplinas
                return disciplina
        return disciplina