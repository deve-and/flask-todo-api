from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração da Documentação (Swagger)
app.config['SWAGGER'] = {
    'title': 'To-Do API - Portfólio Anderson',
    'uiversion': 3
}
swagger = Swagger(app)

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'

# Cria o banco de dados para funcionar no gunicorn/Render  
with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return 'API Online! Acesse <a href="/apidocs">/apidocs</a> para testar.'

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Cria uma nova tarefa
    ---
    tags:
      - Tarefas
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Estudar Python"
            description:
              type: string
              example: "Criar API com Flask e Swagger"
    responses:
      201:
        description: Tarefa criada com sucesso
      400:
        description: Erro de validação (Título obrigatório)
    """
    data = request.get_json()

    if 'title' not in data:
        return {'error': 'O título é obrigatório.'}, 400
    
    new_task = Task(
        title=data['title'],
        description=data.get('description', '')
    )

    db.session.add(new_task)
    db.session.commit()

    return {
        'id': new_task.id,
        'title': new_task.title,
        'description': new_task.description,
        'done': new_task.done
    }, 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Lista todas as tarefas
    ---
    tags:
      - Tarefas
    responses:
      200:
        description: Lista de tarefas retornada com sucesso
    """
    tasks_list = Task.query.all()
    output = []

    for task in tasks_list:
        output.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        })

    return {'tasks': output}, 200

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """
    Atualiza uma tarefa existente
    ---
    tags:
      - Tarefas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            done:
              type: boolean
    responses:
      200:
        description: Tarefa atualizada com sucesso
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get(id)

    if not task:
        return {'erro': 'Tarefa não encontrada'}, 404
    
    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)

    db.session.commit()

    return {
        'mensagem': 'Tarefa atualizada!',
        'task': {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        }
    }

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Apaga uma tarefa
    ---
    tags:
      - Tarefas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get(id)
    
    if not task:
        return {'erro': 'Tarefa não encontrada'}, 404
        
    db.session.delete(task)
    db.session.commit()
    
    return {'mensagem': 'Tarefa deletada com sucesso!'}, 200

if __name__ == '__main__':
    app.run(debug=True)