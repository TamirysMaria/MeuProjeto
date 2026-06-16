# Previsão de Custo Médico

Aplicação web desenvolvida com **Flask** e **scikit-learn** que utiliza um modelo de **Random Forest** 
para prever o custo médico de um paciente com base em suas características pessoais e de saúde.


## Sobre o Projeto

O sistema recebe dados do paciente por meio de um formulário web e retorna uma estimativa do custo médico,
processando automaticamente os encodings necessários para alimentar o modelo de machine learning.


## Tecnologias Utilizadas

- **Python 3.13**
- **Flask** — framework web
- **scikit-learn 1.6.1** — modelo preditivo (Random Forest Regressor)
- **pandas** — manipulação dos dados de entrada
- **joblib** — carregamento do modelo `.pkl`
- **numpy** — suporte numérico


## Estrutura do Projeto

```
meu_projeto/
├── app.py                       
├── predictor.py                  # Lógica de predição e encoding das features
├── requirements.txt              
├── models/
│   └── modelo_random_forest.pkl  # Modelo treinado
├── templates/
│   └── index.html                
└── static/
    └── style.css                 
```

## Como Executar Localmente

### Pré-requisitos

- Python 3.10 ou superior instalado
- Git (para clonar o repositório)

### Passo a passo

```bash
# 1. Clone o repositório (ou extraia o ZIP)
git clone https://github.com/seu-usuario/seu-repositorio.git
cd meu_projeto

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie a aplicação
python app.py
```

Acesse **http://127.0.0.1:5000** no navegador.


## Variáveis do Modelo

| Variável |               Descrição                  |       Tipo       |
| `IDADE`  |           Idade do paciente              |     Numérico     |
| `SEXO`   |       0 = Masculino, 1 = Feminino        |     Binário      |
| `IMC`    |        Índice de Massa Corporal          | Numérico decimal |
| `FILHOS` |            Número de filhos              |     Numérico     |
| `FUMANTE`|            0 = Não, 1 = Sim              |      Binário     |
| `REGIAO` | noroeste / sudeste / sudoeste / nordeste |    Categórico    |

**Variável alvo (y):** `CUSTO_MEDICO` — valor numérico em reais estimado pelo modelo.


## Dependências

```
Flask
scikit-learn==1.6.1
joblib
numpy
pandas
```

Instale com:

```bash
pip install -r requirements.txt
```

---

## Observações

- O modelo foi treinado com `scikit-learn 1.6.1`. Use a mesma versão para evitar incompatibilidades ao carregar o arquivo `.pkl`.
- O servidor Flask em modo `debug=True` é voltado para desenvolvimento. Para produção, utilize um servidor WSGI como **Gunicorn**.
