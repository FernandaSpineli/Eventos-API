from operator import ifloordiv
from flask import Flask, abort, jsonify, request, json

from eventos import Evento
from eventosOnline import EventoOnline


### FLASK_APP=app.py FLASK_ENV=development flask run

ev_online = EventoOnline('Live de Python')
ev2_online = EventoOnline('Live de Java')
ev = Evento('Aula de Python', 'São Paulo')
eventos = [ev_online, ev2_online, ev]


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Flask configurado com sucesso</h1>'

@app.route('/api/eventos/')
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
        return jsonify(eventos_dict)

@app.route('api/eventos/', methods=['POST'])    
def criar_evento():
    data = request.get_json()
    nome = data.get('nome')
    local = data.get('local')

    if not nome:
        abort(400, '"nome" precisa ser informado!')

    if local:
        evento = Evento(nome=nome, local=local)
    else:
        evento = EventoOnline(nome=nome)
    eventos.append(evento)

    return {
        'id': evento.id,
        'url': f'api/eventos/{evento.id}/'
    }
    
@app.errorhandler(404)    
def not_found(erro):
    return (jsonify(erro=str(erro)), 404)

@app.errorhandler(400)    
def bad_request(erro):
    return (jsonify(erro=str(erro)), 400)

def get_evento(id):
    for ev in eventos:
        if ev.id == id:
            return ev
    abort(404, 'Evento não encon')

@app.route('api/eventos/<int:id>/')
def detalhar_evento(id):
    ev = get_evento(id)
    return jsonify(ev.__dict__)
    
@app.route('api/eventos/<int:id>/', methods=['DELETE'])
def deletar_evento(id):
    ev = get_evento(id)
    eventos.remove(ev)
    return jsonify(id=id)

@app.route('api/eventos/<int:id>/', methods=['PUT'])
def editar_evento(id):
    #Parsing
    data = request.get_json()
    nome = data.get('nome')
    local = data.get('local')
    
    #Validação
    if not nome:
        abort(400, '"nome" precisa ser informado!')
    if not local:
        abort(400, '"local" precisa ser informado!')

    #Modificação
    ev = get_evento(id)
    ev.nome = nome
    ev.local = local

    return jsonify(ev.__dict__)
    
@app.route('api/eventos/<int:id>/', methods=['PATCH'])
def editar_evento_parcial(id):
    data = request.get_json()
    ev = get_evento(id)
    if 'nome' in data.keys():
        nome = data.get('nome')
        if not nome:
            abort(400, '"nome" precisa ser informado!')
        ev.nome = nome
    if 'local' in data.keys():
        local = data.get('local')
        if not local:
            abort(400, '"local" precisa ser informado!')
        ev.local = local
    return jsonify(ev.__dict__)    