import pandas as pd

class AtosPessoalDataset:

    def __init__(self, dts_path):
        self.dts_path = dts_path
        self.df = pd.read_csv(self.dts_path)
        self.tipo_atos = list(set(self.df['tipo_rel']))

    
    def pivot_all_acts(self, index=['id_dodf','id_rel'], columns=['tipo_ent'], values='texto'):
        dict_df_atos = {}        
        for ato in self.tipo_atos:            
            df_ato = self.pivot(ato, index=index, columns=columns, values=values)
            dict_df_atos[ato] = df_ato
        return dict_df_atos
    
    def pivot(self, ato, index=['id_dodf','id_rel'], columns=['tipo_ent'], values='texto'):
        df_ato = self.df[self.df['tipo_rel'] == ato]
        df_ato = df_ato.pivot_table(index=index, columns=columns, values=values, aggfunc='first')
        df_ato = df_ato[df_ato[ato].notna()]
        return df_ato

    
    

            

    

