#  Minha Primeira API REST com Python & Flask

Olá, Esse é o repositório do meu primeiro projeto Backend "de verdade".

A ideia aqui foi criar uma API para gerenciar tarefas (To-Do List). Mas o objetivo não era só fazer a lista, mas sim **entender como funciona por "trás" do site**. Como a persistência de dados, qundo você clica em "Salvar" e o dado não se perde? É isso que eu construí aqui.

🔗 **Vê ela rodando online:** [https://anderson-api-todo.onrender.com/apidocs](https://flask-todo-api-yu62.onrender.com/apidocs/)
*(Nota: pode levar um tempo para o app funcionar de primeira, demora um pouco para carregar de primeira 😅)*

---

##  Mas o que é isso, afinal?

Se você não é da área técnica: eu construí o "motor" do carro, sem a lataria.
Não tem HTML nem CSS (a parte bonita), o foco total foi na **Lógica e nos Dados**.

Eu criei um sistema onde você manda informações (títulos, descrições) e o meu código Python:
1.  Recebe esse pedido.
2.  Verifica se tá tudo certo (Validação).
3.  Guarda no Banco de Dados com segurança.
4.  Devolve a resposta pro usuário.

Para a gente conseguir "ver" isso acontecendo, usei o **Swagger**, que cria uma tela cheia de botões para testar as rotas.

---

##  O que eu usei pra construir

* **Python:** A linguagem base.
* **Flask:** O framework que faz o Python funcionar na Web.
* **SQLAlchemy:** Pra conversar com o banco de dados sem precisar ficar escrevendo SQL puro na mão.
* **Swagger (Flasgger):** Pra criar a documentação visual (o link ali de cima).
* **Render:** Pra tirar o site do meu computador e colocar na internet pra todo mundo ver e testar.

---

##  Os "Perrengues" (Aprendizados Reais)

Não vou mentir obtive ajuda IA, mas não foi "copiar e colar". Tive que bater cabeça com algumas coisas que são abstratas pra quem tá começando:

* **O mistério do "Onde está o banco?":** No meu computador funcionava lindo. Quando subi pra nuvem (Render), o banco de dados sumia ou dava erro. Tive que aprender sobre caminhos absolutos no Linux e como o servidor trata arquivos de um jeito diferente do Windows.
* **Verbos HTTP:** Entendi na prática que GET é pra ler, POST é pra criar, e que se eu trocar um pelo outro, o navegador reclama.
* **Documentação:** Aprendi que código sem explicação é inútil. Configurar o Swagger foi chato no começo (o tal do YAML é sensível a qualquer espaço errado), mas ver a tela colorida funcionando valeu a pena.

---

##  As Rotas (Como usar)

O sistema faz o básico bem feito (**CRUD**):

* `POST /tasks` -> Cria a tarefa.
* `GET /tasks` -> Vê tudo o que tem lá.
* `PUT /tasks/id` -> Arruma uma tarefa ou marca como feita.
* `DELETE /tasks/id` -> Apaga a tarefa (sem dó).

---

## Quer rodar na sua máquina?

Se quiser ver o código funcionando aí no seu PC:

```bash
# 1. Clone este repo
git clone [https://github.com/SEU_USUARIO/flask-todo-api.git](https://github.com/SEU_USUARIO/flask-todo-api.git)

# 2. Instala as dependências (o "requirements.txt")
pip install -r requirements.txt

# 3. Roda o app
python app.py
