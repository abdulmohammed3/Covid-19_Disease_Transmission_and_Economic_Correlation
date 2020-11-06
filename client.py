#imported Libraries
import pandas as pd
import plotly.express as px

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#Dashboard Name
app = dash.Dash("Covid-19 Economic Disparities");
# ----------------------------------------------------------------------
#import and clean data
df = pd.read_csv("county_cases.csv");

df = df.groupby(['county_name','cases','County FIPS code'])[['deaths']].mean();
df.reset_index(inplace = True);
print(df[:162]);
#----------------------------------------------------------------------------
#App Layout
