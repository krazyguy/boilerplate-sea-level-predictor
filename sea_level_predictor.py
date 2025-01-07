import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df_extended = df.copy()
    future_years = list(range(df['Year'].iloc[-1] + 1, 2051))
    future_data = pd.DataFrame({'Year': future_years})
    df_extended = pd.concat([df_extended, future_data], ignore_index=True)
    future_line = [slope * x + intercept for x in df_extended['Year']]
    plt.plot(df_extended['Year'], future_line, color='green', linestyle='--', label='Line of Best Fit')
    

    # Create second line of best fit
    recent_df = df[df['Year'] > 1999].copy()
    Rslope, Rintercept, Rr_value, Rp_value, Rstd_err = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_future_years = list(range(recent_df['Year'].iloc[-1] + 1, 2051))
    recent_future_data = pd.DataFrame({'Year': recent_future_years})
    recent_extended = pd.concat([recent_df, recent_future_data], ignore_index=True)
    recent_future_line = [Rslope * x + Rintercept for x in recent_extended['Year']]
    plt.plot(recent_extended['Year'], recent_future_line, color='red', linestyle='--', label='Second line of best fit')
    


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()