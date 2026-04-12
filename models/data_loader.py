import pandas as pd
import os

'''
Responsabilidade: Carregar e limpar os dados CSV. Esta classe será encarregada de
ler o arquivo bruto do TSE usando o Pandas. Ela lidará com questões como a
codificação de caracteres (frequentemente latin1 ou iso-8859-1 em dados do
governo brasileiro) e a seleção apenas das colunas necessárias, economizando
memória.
'''
class ElectionDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.filepath}")

        colunas_uteis = ['NR_TURNO', 'SG_UF', 'NM_MUNICIPIO', 'DS_CARGO','NM_CANDIDATO', 'QT_VOTOS_NOMINAIS']

        self.data = pd.read_csv(self.filepath, sep=';', encoding='latin1', usecols=colunas_uteis)
        return self.data