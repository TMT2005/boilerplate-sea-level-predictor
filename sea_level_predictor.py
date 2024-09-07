import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color= 'blue', label = 'Data')

    # Create first line of best fit
    Line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880, 2051)])
    y = Line.slope * x + Line.intercept
    plt.plot(x, y, 'r', label='Fit 1880-2050')

    # Create second line of best fit
    dfRecent = df[df['Year'] >= 2000]
    newLine = linregress(dfRecent['Year'], dfRecent['CSIRO Adjusted Sea Level'])
    newX = pd.Series([i for i in range(2000, 2051)])
    newY = newLine.slope * newX + newLine.intercept
    plt.plot(newX, newY, 'g', label='Fit 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
