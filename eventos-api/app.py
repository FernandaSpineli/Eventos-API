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
    data = json.loads(request.data)
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


@app.route('api/eventos/<int:id>/')
def detalhar_evento(id):
    for ev in eventos:
        if ev.id == id:
            return jsonify(ev.__dict__)
    abort(404, 'Evento não encontrado')
    #return make_response(jsonify(data), 404)
    
@app.route('api/eventos/<int:id>/', methods=['DELETE'])
def deletar_evento(id):
    for ev in eventos:
        if ev.id == id:
            eventos.remove(ev)
            return jsonify(id=id)
    abort(404, 'Evento não encontrado')    