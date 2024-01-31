import os
import folium
import pandas as pd

curr_workdir = os.getcwd()
data_dir = os.path.join(curr_workdir, 'data')
data_covid19_path = os.path.join(data_dir, "world_coronavirus_cases.xlsx")

df_covid19 = pd.read_excel(data_covid19_path)

world_map = folium.Map(tiles="Cartodb dark_matter")

world_map.save("CoronaWorldMap.html")