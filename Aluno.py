class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
        self.__notas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def matricula(self):
        return self.__matricula

    @property
    def notas(self):
        return self.__notas
