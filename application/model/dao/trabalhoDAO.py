from flask import current_app

from application.model.entity.Aula import Aula
from application.model.entity.Disciplina import Disciplina
from application.model.entity.Prova import Prova
from application.model.entity.Trabalho import Trabalho



class trabalhoDAO:
    def __init__ (self):
        self._listar_trabalho = []
        self._listar_trabalho.append(Trabalho(1, "TRAB1 - Interface com o Usuario Complemento", 1, "Tassio Auad"))
        self._listar_trabalho.append(Trabalho(2, "TRAB2 - Interface com o Usuario - GRID", 1, "Tassio Auad"))
        self._listar_trabalho.append(Trabalho(3, "TRAB3 - Interface com o Usuario - FLEXBOX", 1, "Tassio Auad"))
        self._listar_trabalho.append(Trabalho(4, "TRAB1 - Sistemas Operacionais - macOS", 2, "Felipe"))
        self._listar_trabalho.append(Trabalho(5, "TRAB2 - Sistemas Operacionais - LINUS", 2, "Felipe"))
        self._listar_trabalho.append(Trabalho(6, "TRAB1 - Modelagem de Banco de Dados", 3, "Anrafel"))


    def get_listar_trabalho (self):
        return self._listar_trabalho


    def buscar (self, id):
        trabalho = None
        for index, trabalhos in enumerate(self.get_listar_trabalho()):
            if trabalhos.get_id() == id:
                trabalho = trabalhos
                return trabalho
        return trabalho