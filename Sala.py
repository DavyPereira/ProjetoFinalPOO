class Sala:
    def __init__(self, turma, professor):
        self.__capacidade_maxima = 30
        self.__turma = turma
        self.__professor = professor
        self.__alunos = []  

    def add_aluno(self, alunos):
        for aluno in alunos:
            if len(self.__alunos) < self.__capacidade_maxima:
                self.__alunos.append(aluno)
                print(f"Aluno {aluno.nome} adicionado à sala {self.__turma}.")
            else:
                print(f"A sala {self.__turma} já atingiu sua capacidade máxima!")

    def remover_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            print(f"Aluno {aluno} removido da sala {self.__turma}.")
        else:
            print(f"Aluno {aluno} não encontrado na sala {self.__turma}.")

    def listar_alunos(self):
        print(f"A Sala {self.__turma} com o professor {self.__professor.nome} tem os seguintes alunos:")
        if self.__alunos:
            print(f"Alunos na sala:")
            for aluno in self.__alunos:
                print(f"{aluno.nome}")
        else:
            print(f"A sala {self.__turma} está vazia.")

    @property
    def nome(self):
        return self.__turma

    @property
    def capacidade_maxima(self):
        return self.__capacidade_maxima

    @property
    def turma(self):
        return self.__turma

    @property
    def professor(self):
        return self.__professor
