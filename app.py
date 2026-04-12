from flask import Flask, render_template
import pandas as pd
import os

from models.data_loader import ElectionDataLoader
from models.analyzer import ElectionAnalyzer, VoteAggregator
from models.chart_builder import ChartBuilder

app = Flask(__name__)

df_nacional_t1 = None
df_estadual_t1 = None
df_nacional_t2 = None
df_estadual_t2 = None


def initialize_data():

    global df_nacional_t1, df_estadual_t1
    global df_nacional_t2, df_estadual_t2

    filepath = os.path.join('data', 'votacao_candidato_munzona_2022_BR.csv')

    loader = ElectionDataLoader(filepath)
    df_raw = loader.load_data()

    analyzer = ElectionAnalyzer(df_raw)

    # ---------- PRIMEIRO TURNO ----------

    df_t1 = analyzer.get_president_data(turno=1)

    df_nacional_t1 = VoteAggregator.aggregate_national(df_t1)
    df_estadual_t1 = VoteAggregator.aggregate_by_state(df_t1)

    # ---------- SEGUNDO TURNO ----------

    df_t2 = analyzer.get_president_data(turno=2)

    df_nacional_t2 = VoteAggregator.aggregate_national(df_t2)
    df_estadual_t2 = VoteAggregator.aggregate_by_state(df_t2)


initialize_data()


# ---------- HOME ----------

@app.route('/')
def index():
    return render_template('index.html')


# ---------- PRIMEIRO TURNO ----------

@app.route('/primeiro_turno')
def primeiro_turno():

    grafico_nacional = ChartBuilder.build_national_bar_chart(df_nacional_t1)
    grafico_estados = ChartBuilder.build_state_bar_chart(df_estadual_t1)

    tabela = df_nacional_t1.to_dict(orient='records')

    return render_template(
        'primeiro_turno.html',
        grafico_nacional=grafico_nacional,
        grafico_estados=grafico_estados,
        dados=tabela
    )


# ---------- SEGUNDO TURNO ----------

@app.route('/segundo_turno')
def segundo_turno():

    grafico_nacional = ChartBuilder.build_national_bar_chart(df_nacional_t2)
    grafico_estados = ChartBuilder.build_state_bar_chart(df_estadual_t2)

    tabela = df_nacional_t2.to_dict(orient='records')

    return render_template(
        'segundo_turno.html',
        grafico_nacional=grafico_nacional,
        grafico_estados=grafico_estados,
        dados=tabela
    )


# ---------- CONTEXTO ----------

@app.route('/contexto')
def contexto():
    return render_template('contexto.html')


if __name__ == '__main__':
    app.run(debug=True)