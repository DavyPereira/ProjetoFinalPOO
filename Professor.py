class Professor:
    def __init__(self, nome, topico, genero):
        self.__genero = genero
        self.__nome = nome
        self.__topico = topico

    def ensinar(self):
        print(f"O professor está ensinando sobre {self.__topico}")

    def bronca(self, aluno, motivo="desatenção"):
        print(f"O professor {self.__nome} está dando um sermão no aluno {aluno.nome} por {motivo}.")

    def correçao(self, frase):
        frase_corrigida = frase.replace("vc", "você").replace("pq", "porque")
        print(f"Frase corrigida: {frase_corrigida}")

    def ir_pra_casa(self, motivo="Enxaqueca"):
        print(f"O Professor precisou ir pra casa pois estava com {motivo}")

    @property
    def nome(self):
        return self.__nome

    @property
    def topico(self):
        return self.__topico