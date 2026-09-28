import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# 10 min + 
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df.head())
    # print(df.tail())
    # print(df.info())
    # print(df.info())
    # print(df.loc[df.shape[0] -1 , 'Year'])

    # افهم البينات
    
    # Create scatter plot
    plt.scatter(x= df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # 1st best fit
    list_years = [i for i in range(1880, 2051)]
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # print(fit1.intercept, '_' * 20, fit1.slope)
    y_pred1 = fit1.intercept + fit1.slope * pd.Series(list_years)
    # Create second line of best fit
    plt.plot(list_years, y_pred1)


    # 2nd best fit
    recent_years = [i for i in range(2000, 2051)]
    loc_of_2000 = (pd.Index(df.Year).get_loc(2000))
    # print([i for i  in range(10)].index(4))
    slope, intercept,_,_,_ = linregress(df.Year[loc_of_2000 : ] , df['CSIRO Adjusted Sea Level'][ loc_of_2000: ])
    # print(slope, intercept)
    y_pred2 = intercept + slope * pd.Series(recent_years)
    plt.plot(recent_years, y_pred2)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
