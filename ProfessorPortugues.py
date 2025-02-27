from Professor import Professor

class ProfessorPortugues(Professor):
    def __init__(self, nome, idade, genero):
        super().__init__(nome, idade, genero)

    def ensinar(self, topico="Gramática"):
        print(f"O professor de Português está explicando regras de {topico}.")
        return f"Aula de {topico} sobre conjugações verbais e acentuação."

    def bronca(self, aluno, motivo="erro de ortografia"):
        print(f"O professor de Português está corrigindo {aluno.nome} por {motivo}.")
        return f"{aluno.nome}, revise suas regras ortográficas com mais atenção!"

    def preparar_aula(self, materia):
        print(f"O professor está preparando a aula de {materia}.")
        return f"Slides e exercícios sobre {materia} foram preparados."

    def ir_pra_casa(self, motivo="Gripe"):
        print(f"O Professor precisou ir pra casa pois estava com {motivo}")