from flask import current_app

from application.model.entity.Aula import Aula
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Prova import Prova



class provaDAO:
    def __init__ (self):
        self._listar_prova = []
        self._listar_prova.append(Prova(1, "P1 - Interface com o Usuario", 1, "Tassio Auad"))
        self._listar_prova.append(Prova(2, "P1 - Sistemas Operacionais - Pratica", 2, "Felipe"))
        self._listar_prova.append(Prova(3, "P1 - Modelagem de Banco de Dados", 3, "Anrafel"))


    def get_listar_prova (self):
        return self._listar_prova


    def buscar (self, id):
        prova = None
        for index, provas in enumerate(self.get_listar_prova()):
            if provas.get_id() == id:
                prova = provas
                return prova
        return prova