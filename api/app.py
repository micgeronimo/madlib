"""Api endpoints of this service."""
from flask import Flask

from api import word_provider


flask_app = Flask(__name__)


@flask_app.route('/madlib')
def aggregate_data():
    """Gather data from third party provider and return it."""
    noun = word_provider.get_noun()
    verb = word_provider.get_verb()
    adjective = word_provider.get_adjective()

    payload = f'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. I asked, "Does the stew need fresh {noun}?"'
    return payload


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000)
