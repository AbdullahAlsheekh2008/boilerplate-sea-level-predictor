import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# 1 hour and 30 min (it is fast compared with other prjects)
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    
    # Create scatter plot
    plt.scatter(x= df['Year'], y=df['CSIRO Adjusted Sea Level'], c='c' , s=6)

    # Create first line of best fit

    list_years = [i for i in range(1880, 2051)]
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_pred1 = fit1.intercept + fit1.slope * pd.Series(list_years)
    plt.plot(list_years, y_pred1, c='y')

    # Create second line of best fit
    recent_years = [i for i in range(2000, 2051)]
    loc_of_2000 = (pd.Index(df.Year).get_loc(2000))
    slope, intercept,_,_,_ = linregress(df.Year[loc_of_2000 : ] , df['CSIRO Adjusted Sea Level'][ loc_of_2000: ])
    y_pred2 = intercept + slope * pd.Series(recent_years)
    plt.plot(recent_years, y_pred2, color='red')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(['Data points', 'best fit of all years', 'best fit from 2000'])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
