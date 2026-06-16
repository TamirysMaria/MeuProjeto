import joblib
import pandas as pd

# Carrega o modelo uma única vez ao iniciar a aplicação
model = joblib.load('models/modelo_random_forest.pkl')

# Nomes das colunas exatamente como o modelo foi treinado
COLUNAS = [
    'IDADE', 'SEXO', 'IMC', 'FILHOS', 'FUMANTE',
    'REGIAO_noroeste', 'REGIAO_sudeste', 'REGIAO_sudoeste',
    'FAIXA_IDADE_adulto', 'FAIXA_IDADE_meia-idade', 'FAIXA_IDADE_idoso'
]

def calcular_faixa_idade(idade):
    """Retorna as flags de faixa etária baseado na idade."""
    adulto    = 1 if 18 <= idade <= 35 else 0
    meia_idade = 1 if 36 <= idade <= 59 else 0
    idoso     = 1 if idade >= 60 else 0
    return adulto, meia_idade, idoso

def prever_custo(idade, sexo, imc, filhos, fumante, regiao):
    """
    Recebe os dados do formulário e retorna o custo médico previsto.

    Parâmetros:
        idade    (int)   : idade do paciente
        sexo     (int)   : 0 = masculino, 1 = feminino
        imc      (float) : índice de massa corporal
        filhos   (int)   : número de filhos
        fumante  (int)   : 0 = não, 1 = sim
        regiao   (str)   : 'noroeste', 'sudeste', 'sudoeste' ou 'nordeste'
    """
    # Encode de região (one-hot — nordeste é a base: todas as flags = 0)
    reg_noroeste = 1 if regiao == 'noroeste' else 0
    reg_sudeste  = 1 if regiao == 'sudeste'  else 0
    reg_sudoeste = 1 if regiao == 'sudoeste' else 0

    # Encode de faixa de idade
    adulto, meia_idade, idoso = calcular_faixa_idade(idade)

    features = pd.DataFrame([[
        idade, sexo, imc, filhos, fumante,
        reg_noroeste, reg_sudeste, reg_sudoeste,
        adulto, meia_idade, idoso
    ]], columns=COLUNAS)

    predicao = model.predict(features)
    return round(float(predicao[0]), 2)
