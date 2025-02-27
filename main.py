from ProfessorHistoria import ProfessorHistoria
from ProfessorPortugues import ProfessorPortugues
from ProfessorMatematica import ProfessorMatematica
from Sala import Sala
from Aluno import Aluno

def test (Professor, aluno):
    print(f"\nTestando {Professor.__class__.__name__}")
    Professor.correçao("Agora sim está certo")
    Professor.ensinar()
    Professor.bronca(aluno)
    Professor.ir_pra_casa()

if __name__ == "__main__":
    professor_portugues = ProfessorPortugues("Antonio", 33, "Masculino")
    professor_historia = ProfessorHistoria("Paulo", 30,"Masculino")
    professor_matematica = ProfessorMatematica("Cláudia", "Fração", "Feminino")
    sala = Sala("2B", professor_portugues)
    sala1 = Sala("3A", professor_historia)
    aluno = Aluno("Davy", 19, "558609")
    aluno2 = Aluno("Yuri",18, "227654")
    aluno3 = Aluno("Gabriel", 20, "778912")
    aluno4 = Aluno("Kelvin", 19, "889845")
    aluno5 = Aluno("Gabriela", 19, "112398")
    aluno6 = Aluno("Reginaldo", 21, "443278")
    aluno7 = Aluno("Marcos", 18, "659354")
    aluno8 = Aluno("Joao", 20, "772672")
    aluno9 = Aluno("Juliana", 19, "448291")
    aluno10 = Aluno("Roberta", 20, "551948")
    sala.add_aluno([aluno, aluno2, aluno3, aluno4, aluno5])
    sala1.add_aluno([aluno6, aluno7, aluno8, aluno9, aluno10])
    test(professor_historia, aluno3)
    test(professor_portugues, aluno7)
    test(professor_matematica,aluno8)
    sala.listar_alunos()
    sala1.listar_alunos()
