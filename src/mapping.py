import pandas as pd
import geopandas as gpd 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    usa_shapes = gpd.read_file('data/states_21basic/states.shp')
    usa_sightings = pd.read_pickle('data/State_Counts_pickled_df')
    usa_sightings.reset_index(inplace=True) 
    usa_sightings = usa_sightings.rename(columns={'index': 'STATE_NAME', 0 : 'SIGHTINGS'})
    usa_sightings = usa_sightings.append([{'STATE_NAME': 'Hawaii', 'SIGHTINGS': 0}, {'STATE_NAME': 'District of Columbia', 'SIGHTINGS': 0}])
    usa = usa_shapes.merge(usa_sightings, on='STATE_NAME')

    fig, ax = plt.subplots(figsize=(15, 10))
    usa.boundary.plot(ax=ax, edgecolor="black", linewidth = 0.5)
    usa.plot(column='SIGHTINGS',ax=ax, cmap='YlOrRd', legend=True, legend_kwds={'label': "Bigfoot Sightings by State",'orientation': "horizontal"})
    ax.set_title("Where's Bigfoot?", fontsize = 28)
    fig.savefig('images/sighting_map.png', dpi = 125)
    plt.close('all')