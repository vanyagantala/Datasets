# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:26:18 2021

@author: Kate Ingrid
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
#import requests
#import io

#url = "https://raw.githubusercontent.com/vanyagantala/trialversion/main/menu.csv"
#download = requests.get(url).content
df = pd.read_csv(r"https://raw.githubusercontent.com/vanyagantala/Datasets/main/World_Vaccination_Progress.csv")
fig = px.line(df, x="Country", y="Doses_Administered", 
                 hover_data=['Doses_per_1000','Fully_Vaccinated_Population_(%)', 'Vaccines'])
fig.show()

#fig2 = px.bar(df, x="Category", y="Calories", color="Item", title="Long-Form Input")
#fig2.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)