from flask import current_app

from application.model.entity.Aula import Aula
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Prova import Prova



class disciplinaDAO:
    def __init__(self):
       self._lista_disciplina = []
       self._lista_disciplina.append(Disciplina(1, "Laboratorio de Interface do Usuario", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(2, "Sistemas Operacionais", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(3, "Modelagem de Banco de Dados", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(4, "Gestão Ambiental e Desenvolvimento Sustentável", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(5, "Gestão Estratégica de Pessoas", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(6, "Legislação Aplicada a Informatica", "4º Periodo"))
       self._lista_disciplina.append(Disciplina(7, "Laboratório de Empreendendorismo e Inovação", "4º Periodo"))

    def get_lista_disciplina (self):
        return self._lista_disciplina
    