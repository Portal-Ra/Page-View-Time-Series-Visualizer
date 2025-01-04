import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data by removing the top and bottom 2.5% of page views
df = df[df["value"].between(df["value"].quantile(.025), df["value"].quantile(.975))]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

plt.ioff()  # Disable interactive mode

# Function to draw a line plot
def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(data=df, legend="brief", ax=ax)
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')
    # Save image and return fig
    fig.savefig('line_plot.png')
    plt.close(fig)  # Close the plot
    return fig

# Function to draw a bar plot
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(x="year", hue="month", y="value", data=df_bar, hue_order=months, errorbar=None, ax=ax)
    ax.set(xlabel='Years', ylabel='Average Page Views')
    # Save image and return fig
    fig.savefig('bar_plot.png')
    plt.close(fig)  # Close the plot
    return fig

# Function to draw box plots
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['monthnumber'] = df_box['date'].dt.month
    # Ensure the month order is correct in the box plots
    df_box['month'] = pd.Categorical(df_box['month'], categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ordered=True)

    # Draw box plots (with Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(y="value", x="year", data=df_box, ax=ax[0])
    ax[0].set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    sns.boxplot(y="value", x="month", data=df_box, ax=ax[1])
    ax[1].set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')
    # Save image and return fig
    fig.savefig('box_plot.png')
    plt.close(fig)  # Close the plot
    return fig

