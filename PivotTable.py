# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import numpy as np

data = pd.read_csv('data/epl/all_players_stats.csv')
data
# -

pd.pivot_table(data=data,index='Team',values='YellowCards',columns='Position',aggfunc=np.mean)

df = pd.pivot_table(data=data,index='Team',values='YellowCards',columns='Position',aggfunc=[np.mean,np.sum]).reset_index()

# +
# df1 = pd.pivot_table(data=data,index='Team',values='YellowCards',columns='Position',aggfunc='mean').reset_index()
# df2 = pd.pivot_table(data=data,index='Team',values='YellowCards',columns='Position',aggfunc='sum').reset_index()
# -

data.query('Position==["Forward","Midfielder","Defender"]').pivot_table(index='Team',values='YellowCards',columns='Position',aggfunc=[np.mean,np.sum]).reset_index()
