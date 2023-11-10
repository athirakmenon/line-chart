# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def Player_Origin(Ipl,IND,OVS):


    OVS_ds = Ipl[Ipl['Player Origin'] == OVS]
    IND_ds = Ipl[Ipl['Player Origin'] == IND]
    
    OVS_amount =OVS_ds.groupby('Year')['Amount'].sum().reset_index()
    IND_amount=IND_ds.groupby('Year')['Amount'].sum().reset_index()
    
    
    plt.figure(figsize=(10,6))
    
    plt.plot(OVS_amount['Year'],OVS_amount['Amount'], label = 'Overseas',
                 color="red")
    
    plt.plot(IND_amount['Year'],IND_amount['Amount'], label = 'Indian',
                color="orange")
    
    plt.legend()
    plt.title('Total Spending Between Overseas and Indian Players  Over Time',
              fontsize = 20)
    plt.xlabel('Year',fontsize = 20)
    plt.ylabel('Total Spending(million)',fontsize = 20)
    plt.show()
    

Ipl = pd.read_csv("IPLPlayerAuctionData.csv")

OVS = 'Overseas'
IND = 'Indian'

Player_Origin(Ipl,IND,OVS)
