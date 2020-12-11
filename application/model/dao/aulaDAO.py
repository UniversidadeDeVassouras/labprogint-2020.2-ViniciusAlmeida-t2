from flask import current_app

from application.model.entity.Aula import Aula
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Prova import Prova


class aulaDAO:
    def __init__ (self):
        self._listar_aula = []
        self._listar_aula.append(Aula(1, "Aula 1 - Não me faça pensar!", 1, "4º Periodo"))
        self._listar_aula.append(Aula(2, "Aula 2 - Os 10 Principais Erros de Design de Aplicativos Segundo Jacob Nielsen", 1, "4º Periodo"))
        self._listar_aula.append(Aula(3, "Aula 3 - Personas", 1, "4º Periodo"))
        self._listar_aula.append(Aula(4, "Aula 4 - Grid Layout", 1, "4º Periodo"))
        self._listar_aula.append(Aula(5, "AULA 1 - INTRODUÇÃO A SISTEMAS OPERACIONAIS - (On-line)", 2, "4º Periodo"))
        self._listar_aula.append(Aula(6, "AULA 2 - PROCESSOS - (On-line)", 2, "4º Periodo"))
        self._listar_aula.append(Aula(7, "AULA 3 - ESCALONAMENTO DE CPU / DEADLOCKS - (On-line)", 2, "4º Periodo"))
        self._listar_aula.append(Aula(8, "AULA 4 - GERENCIAMENTO DE MEMORIA / MEMORIA VIRTUAL - (On-line)", 2, "4º Periodo"))
        self._listar_aula.append(Aula(9, "Aula 01 - Modelagem de Banco de Dados 17.09.2020", 3, "4º Periodo"))
        self._listar_aula.append(Aula(10, "Aula 02 - BD - Slides 23.09.2020", 3, "4º Periodo"))
        self._listar_aula.append(Aula(11, "Aula 03 - Modelagem de Banco de Dados (Slides)", 3, "4º Periodo"))
        self._listar_aula.append(Aula(12, "Aula 04 - MBD - Normalização e Introdução ao SQL", 3, "4º Periodo"))


    def get_listar_aula (self):
        return self._listar_aula


    def buscar (self, id):
        materia = None
        for index, materias in enumerate(self.get_listar_aula()):
            if materias.get_id() == id:
                materia = materias
                return materia
        return materia