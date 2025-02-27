from Professor import Professor

class ProfessorHistoria(Professor):
    def __init__(self, nome, idade, genero):
        super().__init__(nome, idade, genero)

    def ensinar(self, topico="Guerra Fria"):
        print(f"O professor de historia está explicando sobre {topico}")
        return f"A aula de {topico} está abordando sobre a queda do Muro de Berlim"

    def bronca(self, aluno, motivo = "Atrapalhou a aula"):
        print(f"O professor de Historia está corrigindo o {aluno.nome} porque {motivo}")
        return f"{aluno.nome} se comporte, por favor"

    def ir_pra_casa(self, motivo="Dor de Cabeça"):
        print(f"O Professor precisou ir pra casa pois estava com {motivo}")