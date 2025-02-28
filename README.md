# Sala.py
Este arquivo contém a classe `Sala`, que representa uma sala de aula com um professor e alunos.  
## 📌 Classes
- `Sala`: Define uma sala com capacidade máxima de 30 alunos.
- Métodos principais:
  - `add_aluno(alunos)`: Adiciona alunos à sala (se houver espaço).
  - `remover_aluno(aluno)`: Remove um aluno específico da sala.
  - `listar_alunos()`: Exibe a lista de alunos presentes na sala.
## 📌 Uso
Crie uma instância de `Sala`, passe o nome da turma e um professor, depois adicione alunos à sala.



# Aluno.py
Este arquivo contém a classe `Aluno`, que representa um estudante.
## 📌 Classes
- `Aluno`: Define um aluno com nome, idade e número de matrícula.
- Métodos principais:
  - `nome`, `idade`, `matricula`: Propriedades do aluno.
  - `notas`: Lista de notas do aluno.
## 📌 Uso
Crie instâncias de `Aluno` passando o nome, idade e matrícula.



# Professor.py
Este arquivo contém a classe `Professor`, que serve como classe base para professores de diferentes disciplinas.
## 📌 Classes
- `Professor`: Representa um professor genérico.
- Métodos principais:
  - `ensinar()`: Explica um tópico.
  - `bronca(aluno, motivo)`: Dá um sermão em um aluno.
  - `correcao(frase)`: Corrige expressões informais.
  - `ir_pra_casa(motivo)`: Simula o professor indo para casa.
## 📌 Uso
Crie uma instância de `Professor` e chame seus métodos para simular o comportamento do professor.



# ProfessorHistoria.py
Este arquivo contém a classe `ProfessorHistoria`, que herda da classe `Professor`.
## 📌 Classes
- `ProfessorHistoria`: Representa um professor de história.
- Métodos adicionais:
  - `ensinar(topico)`: Explica um tópico de história (exemplo: Guerra Fria).
  - `bronca(aluno, motivo)`: Dá um sermão em um aluno.
  - `ir_pra_casa(motivo)`: Simula o professor indo para casa.
## 📌 Uso
Crie uma instância de `ProfessorHistoria` e utilize os métodos para simular aulas e interações com alunos.



# ProfessorMatematica.py
Este arquivo contém a classe `ProfessorMatematica`, que herda da classe `Professor`.
## 📌 Classes
- `ProfessorMatematica`: Representa um professor de matemática.
## 📌 Uso
Crie uma instância de `ProfessorMatematica` e utilize os métodos herdados da classe `Professor`.



# ProfessorPortugues.py
Este arquivo contém a classe `ProfessorPortugues`, que herda da classe `Professor`.
## 📌 Classes
- `ProfessorPortugues`: Representa um professor de português.
- Métodos adicionais:
  - `ensinar(topico)`: Explica um tópico de português (exemplo: gramática).
  - `bronca(aluno, motivo)`: Dá um sermão em um aluno por erro de ortografia.
  - `preparar_aula(materia)`: Simula a preparação de uma aula.
## 📌 Uso
Crie uma instância de `ProfessorPortugues` e utilize os métodos para interações em sala de aula.



# main.py
Este é o arquivo principal do projeto, onde todas as classes são instanciadas e testadas.
## 📌 Funcionalidades
- Criação de professores e alunos.
- Adição de alunos às salas de aula.
- Teste dos métodos de ensino e interação dos professores.
## 📌 Como executar
Execute o script normalmente:
```bash
python main.py
