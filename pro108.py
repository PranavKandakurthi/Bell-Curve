import pandas as pd
import plotly.figure_factory as ff
import csv

from google.colab import files
data_to_load = files.upload()

df = pd.read_csv("stab.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Avg Rating"])
fig.show