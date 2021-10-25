import pandas as pd
import os
from datetime import datetime
from dateutil import parser


class AtosPessoalDataset:

    def __init__(self, dts_path):
        self.dts_path = dts_path
        self.df = pd.read_csv(self.dts_path)
        self.tipo_atos = list(set(self.df['tipo_rel']))
    
    def pivot_all_acts(self, index=['id_dodf','id_rel'], columns=['tipo_ent'], values='texto_rel'):
        dict_df_atos = {}        
        for ato in self.tipo_atos:            
            df_ato = self.pivot(ato, index=index, columns=columns, values=values)
            dict_df_atos[ato] = df_ato
        return dict_df_atos
    
    def pivot(self, ato, index=['id_dodf','id_rel'], columns=['tipo_ent'], values='texto_rel'):
        df_ato = self.df[self.df['tipo_rel'] == ato]
        df_ato = df_ato.pivot_table(index=index, columns=columns, values=values, aggfunc='first')
        df_ato = df_ato[df_ato[ato].notna()]
        return df_ato
    
    @staticmethod
    def find_dodf(data, data_sep = '.', root_dir = '.'):
        dia, mes, ano = data.split(data_sep)
        f_data = parser.parse('/'.join([mes,dia,ano]))    
        larqs = os.listdir(root_dir)
        docs_path = []
        for arq in larqs:
            path_date = AtosPessoalDataset.extract_date(os.path.basename(dir))
            if path_date == f_data:
                docs_path.append(os.path.join(root_dir,arq))
        return docs_path


    @staticmethod
    def find_dodf_path(num, data, data_sep = '.', root_dir = '.'):
        dia, mes, ano = data.split(data_sep)
        f_data = parser.parse('/'.join([mes,dia,ano]))    
        meses = ['Desconhecido','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        path = os.path.join(root_dir,'')
        if not os.path.exists(path): return [] 
        ldir = os.listdir(path)
        docs_path = []
        if any(ano in dir for dir in ldir):
            path = os.path.join(path, str(f_data.year))
            if not os.path.exists(path): return []
            ldir = os.listdir(path)
            m = next((dir for dir in ldir if meses[int(mes)] in dir),'')
            if m != '':
                path = os.path.join(path,m)
                if not os.path.exists(path): return []
                ldir = os.listdir(path)
                for dir in ldir:
                    path_date = AtosPessoalDataset.extract_date(os.path.basename(dir))
                    if path_date == f_data:
                        docs_path.append(os.path.join(path,dir))
        return docs_path
        
    
    @staticmethod
    def extract_date(s):
        s = s.split('.')[0].split()[2]
        dia, mes, ano = s.split('-')
        date = parser.parse('/'.join([mes,dia,ano]))
        return date



    
    

            

    

