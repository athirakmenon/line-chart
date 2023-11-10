# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

'''plotting a bar chart in order to get a team-wise spending 
   on IPL Player Auction'''
   
   #creating a function

def Team_Wise_Spending(Ipl):
    # Group by team and calculate the total spending
    team_spending = Ipl.groupby('Team')['Amount'].sum().reset_index()
    
    # Plotting the bar chart
    plt.figure(figsize=(16, 8))
    plt.bar(team_spending['Team'], team_spending['Amount'], color='purple')
    plt.xlabel('Teams', fontsize = 20)
    plt.ylabel('Total Spending(million)', fontsize = 20)
    plt.title('Overall Team-wise Spending on IPL Player Auctions',fontsize =30)
    plt.xticks(rotation=45, ha='right')
    
    plt.savefig("Overall Team-wise Spending on IPL Player Auctions")
    

    plt.show()
    
    
Ipl = pd.read_csv("IPLPlayerAuctionData.csv")
    
Team_Wise_Spending(Ipl)


