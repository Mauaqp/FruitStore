from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "estoessecreto"

listaUsuarios = []

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    registroUsuario = {
        "primer_nombre" : request.form["first_name"],
        "apellido" : request.form["last_name"],
        "id_estudiante" : request.form["student_id"]
    }
    order = {
        "strawberry" : request.form["strawberry"],
        "raspberry" : request.form["raspberry"],
        "apple" : request.form["apple"]
    }
    #session para registroUsuario
    session["primer_nombre"] = request.form["first_name"]
    session["apellido"] = request.form["last_name"]
    session["id_estudiante"] = request.form["student_id"]
    #session para order
    session["strawberry"] = int(request.form["strawberry"])
    session["raspberry"] = int(request.form["raspberry"])
    session["apple"] = int(request.form["apple"])

    listaUsuarios.append(registroUsuario)
    print(request.form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    