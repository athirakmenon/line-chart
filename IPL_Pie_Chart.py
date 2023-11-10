# -*- coding: utf-8 -*-

#importing libraries

import pandas as pd
import matplotlib.pyplot as plt

#creating a function 
def Player_Origin_Distribution(Ipl,Year1,Year2):
    
# Create two DataFrames for the selected years
    data_2014 = Ipl[Ipl['Year'] == 2014]
    data_2020 = Ipl[Ipl['Year'] == 2020]
    
    # Count the number of players for each origin in each year
    player_origin_counts_2014 = data_2014['Player Origin'].value_counts()
    player_origin_counts_2020 = data_2020['Player Origin'].value_counts()
    
    # Plotting both pie charts in a single plot
    plt.figure(figsize=(12, 6))
    
    # Pie chart for the year 2014
    plt.subplot(1, 2, 1)
    plt.pie(player_origin_counts_2014, labels=player_origin_counts_2014.index,
        autopct='%1.1f%%', startangle=90, colors=['darkgreen', 'lightgreen'])
    plt.title('Player Origin Distribution - 2014')
    
    # Pie chart for the year 2020
    plt.subplot(1, 2, 2)
    plt.pie(player_origin_counts_2020, labels=player_origin_counts_2020.index,
        autopct='%1.1f%%', startangle=90, colors=['darkgreen', 'lightgreen'])
    plt.title('Player Origin Distribution - 2020')
    
    plt.savefig("Player Origin Distribution in 2014 and 2016")
    plt.show()
    
    
Ipl = pd.read_csv("IPLPlayerAuctionData.csv")
 
Year1 = 2014
Year2 = 2020

Player_Origin_Distribution(Ipl,Year1,Year2)

    
    




