from flask import Flask, jsonify
from helpers import languages_dictionary


app = Flask(__name__)


@app.route('/languages/JSON')
def langs_endpoint():
    langs = languages_dictionary()
    return jsonify({'Languages': [{'language': lang['language'],
                     'number_of_repos': lang['number_of_repos'],
                     'repos': lang['repos']} for lang in langs]})


if __name__ == "__main__":
   app.debug = True
   app.run(host='0.0.0.0', port=8080)

