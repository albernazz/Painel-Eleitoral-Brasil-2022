import plotly.express as px

class ChartBuilder:

    @staticmethod
    def build_national_bar_chart(df_national):
        """Gera um gráfico de barras com os resultados nacionais."""

        # Filtra brancos e nulos para focar nos candidatos
        df_candidatos = df_national[
            ~df_national['NM_CANDIDATO'].isin(['VOTO BRANCO', 'VOTO NULO'])
        ]

        fig = px.bar(
            df_candidatos,
            x='NM_CANDIDATO',
            y='QT_VOTOS_NOMINAIS',
            title='Votos Totais por Candidato (Nacional)',
            labels={
                'NM_CANDIDATO': 'Candidato',
                'QT_VOTOS_NOMINAIS': 'Quantidade de Votos'
            },
            color='NM_CANDIDATO'
        )

        # Retorna o HTML do gráfico para ser embutido no template
        return fig.to_html(full_html=False)

    @staticmethod
    def build_state_bar_chart(df_state, top_n_candidatos=4):
        """Gera um gráfico de barras agrupadas por estado para os principais candidatos."""

        # Pega apenas os N candidatos mais votados no geral
        top_candidatos = (
            df_state
            .groupby('NM_CANDIDATO')['QT_VOTOS_NOMINAIS']
            .sum()
            .nlargest(top_n_candidatos)
            .index
        )

        df_filtered = df_state[df_state['NM_CANDIDATO'].isin(top_candidatos)]

        fig = px.bar(
            df_filtered,
            x='SG_UF',
            y='QT_VOTOS_NOMINAIS',
            color='NM_CANDIDATO',
            barmode='group',
            title='Votos por Estado (Principais Candidatos)',
            labels={
                'SG_UF': 'Estado',
                'QT_VOTOS_NOMINAIS': 'Votos',
                'NM_CANDIDATO': 'Candidato'
            }
        )

        return fig.to_html(full_html=False)