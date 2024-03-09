import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

data = df["reading score"].to_list()

mean = sum(data)/ len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start, first_std_deviation_end =mean-std_deviation,mean+std_deviation
second_std_deviation_start, second_std_deviation_end =mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end =mean-(3*std_deviation),mean+(3*std_deviation)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.03], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.03], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.03], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.03], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.03], mode="lines", name="STANDARD DEVIATION 2")) 
fig.show()