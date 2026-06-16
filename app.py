from flask import Flask, request, render_template
from predictor import prever_custo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            idade   = int(request.form.get("idade"))
            sexo    = int(request.form.get("sexo"))
            imc     = float(request.form.get("imc"))
            filhos  = int(request.form.get("filhos"))
            fumante = int(request.form.get("fumante"))
            regiao  = request.form.get("regiao")

            resultado = prever_custo(idade, sexo, imc, filhos, fumante, regiao)

        except Exception as e:
            erro = f"Erro ao processar os dados: {str(e)}"

    return render_template("index.html", resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
