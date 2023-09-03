import json, pprint

from flask import Flask, request, jsonify



users = [
    {
        "name": "Alex",
        "age": 20,
        "occupation" : "worker"
    },
    {
        "name":"Anne",
        "age":19,
        "occupation":"banker"
    },
    {
        "name":"Levi",
        "age":23,
        "occupation":"capitan"
    }

]
app = Flask(__name__)

@app.route("/")
def index():
    return "It is working"

@app.route("/users", methods=['GET'])
def get_users():
    return users

@app.route("/<string:name>", methods=['GET'])
def find_user(name):
    for user in users:
        user = dict(user)
        if name in user.values():
            return user
    return "ERROR 404 : User not found"
@app.route("/users", methods=['POST'])
def add_user():
    request_body = request.get_json()

    #new_user = json.loads(request.get_json())
    print(type(request.get_json()))
    print(request.get_json())
    # new_user = {
    #     "name": request_body['name'],
    #     "age" : request_body['age'],
    #     'occupation' : request_body['occupation']
    # }
    users.append(request_body)
    #users.append(new_user)
    print(users)
    #return jsonify({"status code" : "201"})
    return json.dumps(request_body)

@app.route("/<string:name>", methods=['DELETE'])
def delete_user(name):
    for index, user in enumerate(users):
        if name == user['name']:
            del users[index]
            pprint.pprint(users)
            return jsonify({
                "http response": 200
            })
    return jsonify({
        "error" : 404
    })





if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
