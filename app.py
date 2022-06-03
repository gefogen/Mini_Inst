from utils import *
from flask import Flask

from blueprints.main.views import main_blueprint
from blueprints.errors.views import error_blueprint
from blueprints.api.views import api_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII']=False

app.register_blueprint(main_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":  # Запускаем
    app.run(debug=True)
