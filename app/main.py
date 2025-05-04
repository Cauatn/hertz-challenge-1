from flask import Flask, jsonify
from interfaces.routes import routes_bp

def create_app():
    app = Flask(__name__)

    # Registrar as rotas
    app.register_blueprint(routes_bp)

    @app.route("/")
    def index():
        return jsonify({"msg": "API Hertz rodando"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
