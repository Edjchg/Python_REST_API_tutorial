import flask
# Tutorial: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
from flask import jsonify, request

main_api = flask.Flask(__name__)
main_api.config["DEBUG"] = False

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@main_api.route('/', methods=['GET'])
def api_home():
    return "Hello from Python"


@main_api.route('/resources/books/all', methods=['GET'])
def take_books():
    return jsonify(books)


@main_api.route('/resources/book', methods=['GET'])
def take_certain_book():
    ide = 0
    if 'id' in request.args:
        ide = int(request.args['id'])

    result = []
    for book in books:
        if book['id'] == ide:
            result.append(book)
    return jsonify(result)


@main_api.route('/book/delete', methods=['DELETE'])
def delete_book():

    ide = 0
    if 'id' in request.args:
        ide = int(request.args['id'])

    for book in books:
        if book['id'] == ide:
            books.remove(book)
    return jsonify(books)


if __name__ == "__main__":
    main_api.run()
