import pandas as pd

class ElectionAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def get_president_data(self, turno = 1):
        '''Filtra os dados para o cargo de Presidente e o turno
            especificado
        '''
        filtro = (self.df["DS_CARGO"] == "Presidente") & (self.df['NR_TURNO'] == turno)
        return self.df[filtro]

class VoteAggregator:
    @staticmethod
    def aggregate_national(df_presidente):
        """Agrupa os votos totais por candidato em nível nacional."""
        agrupado = df_presidente.groupby('NM_CANDIDATO')['QT_VOTOS_NOMINAIS'].sum().reset_index()
        # Ordena do mais votado para o menos votado
        return agrupado.sort_values(by='QT_VOTOS_NOMINAIS', ascending=False)

    @staticmethod
    def aggregate_by_state(df_presidente):
        """Agrupa os votos por estado e candidato."""

        agrupado = df_presidente.groupby(['SG_UF', 'NM_CANDIDATO'])['QT_VOTOS_NOMINAIS'].sum().reset_index()
        return agrupado
