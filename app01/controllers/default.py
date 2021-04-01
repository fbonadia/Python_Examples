from app01 import app

# Aplica uma rota / a função index
@app.route("/")
def index():
    return "Hello World!"

@app.route("/profile/<name>")
def profile (name):
    return name

@app.route("/profile_id/<int:id>")
def profile_id (id):
    return str(id)

# Only Allow GET Methods
@app.route("/test", methods=['GET'])
def test():
    return 'Olá'
