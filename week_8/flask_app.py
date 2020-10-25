from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return "Hello, World from flask server!"



persons = [
    {
        'id': 1,
        'name': 'Person 1'
    },
    {
        'id': 2,
        'name': 'Person 2'
    },
    {
        'id': 3,
        'name': 'Person 3'
    },    
    {
        'id': 4,
        'name': 'Person 4'
    },
    {
        'id': 5,
        'name': 'Person 5'
    }
]



@app.route('/showpersons/', methods=['GET'])
def get_persons():
    return jsonify({'persons': persons})


@app.route('/person/<int:person_id>/', methods=['GET'])
def get_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    return jsonify({'person': person[0]})



@app.route('/person/', methods=['POST'])
def create_person():
    if not request.json or not 'name' in request.json:
        abort(400)
    person = {
        'id': persons[-1]['id'] + 1,
        'name': request.json['name']
    }
    persons.append(person)
    return jsonify({'person': person}), 201




@app.route('/person/<int:person_id>/', methods=['PUT'])
def update_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    if not request.json or not 'name' in request.json:
        abort(400)
    person[0]['name'] = request.json.get('name', person[0]['name'])
    return jsonify({'person': person[0]})



@app.route('/person/<int:person_id>/', methods=['DELETE'])
def delete_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    persons.remove(person[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
