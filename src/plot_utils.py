# Core data tools
import pandas as pd
import numpy as np
import geopandas as gpd
import math

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines

counties_gdf = gpd.read_file('../data/raw/CA_Counties.shp').to_crs(epsg=4326)

def plot_fire_damage(df,field='Estimated Damage'):

    damage = df[field]
    
    # Scale circle sizes
    circle_sizes = (np.sqrt(damage)+.001) / 10 # Square root to reduce skew, adjust divisor to taste

    # Plot
    fig, ax = plt.subplots(figsize=(10, 12))

    # Plot counties
    counties_gdf.boundary.plot(ax=ax, color='black', linewidth=0.5)

    # Plot fire points with scaled size
    df.plot(
        ax=ax,
        markersize=circle_sizes,
        color='red',
        alpha=0.6,
        edgecolor='black',
        linewidth=0.3
    )

    # Custom legend
    legend_values = [1e6, 1e7, 1e8]  # Reference damages
    legend_sizes = [np.sqrt(v) / 10 for v in legend_values]

    # Create dummy points for the legend
    for size, label in zip(legend_sizes, ['$1M', '$10M', '$100M']):
        ax.scatter([], [], s=size, color='red', alpha=0.6, edgecolor='black', label=label)

    # Apply vertical spacing and style
    ax.legend(
        title='Estimated Damage',
        loc='upper right',
        frameon=True,
        labelspacing=2.0,      # vertical spacing between labels
        handleheight=2.5,
        handlelength=3.0,  # increases size of blank marker handles
        borderpad=1.3,         # space between legend border and content
        borderaxespad=4.5,     # space between legend and axes
        title_fontsize=10,
        fontsize=9
    )


    # Add title and formatting
    ax.set_title("Wildfires in California Scaled by Estimated Damage", fontsize=16)
    ax.text(
        0.5, .987,  # X and Y position in axis coordinates (centered)
        "01/01/2018 to 12/31/2024",
        transform=ax.transAxes,
        ha='center',
        fontsize=11
    )
    ax.axis('off')
    plt.tight_layout()
    plt.savefig("../plots/fire_damage_circles.png", dpi=300)
    plt.show()

def correlation_map(df, title):

    # Compute the correlation matrix
    corr = df.corr()

    # Create a mask to show only the lower triangle (for cleaner layout)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(8, 6))
    sns.set(style="white")

    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5,
        square=True,
        cbar_kws={"shrink": .8},
        vmin=-1, vmax=1,
        annot_kws={"size": 10}
    )

    # Title and formatting
    plt.title(title, fontsize=14, pad=12)
    plt.xticks(rotation=30, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()
    
def plot_map(gdf, gdf_column, firename, ax=None, cali = False,):
    
    """Plots wildfire severity predictions on a California map with fire location markers and categorical styling."""

    # Use passed axis or create one if needed
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 10))

    # Base map
    counties_gdf.plot(ax=ax, color='whitesmoke', edgecolor='gray', linewidth=0.5)

    # Fire location(s)
    if firename == 'Palisades':
        fire_points = [
            {'name': 'Palisades Fire', 'lat': 34.07022, 'lon': -118.54453}
        ]
    else:
        fire_points = [{'name': 'Eaton Fire', 'lat': 34.203483, 'lon': -118.069155}]

    for fire in fire_points:
        ax.scatter(fire['lon'], fire['lat'], s=500, c='red', marker='*',
                   edgecolor='black', alpha=0.8, zorder=3)
        ax.text(fire['lon'] + 0.1, fire['lat'] - 0.03, fire['name'],
                fontsize=11, color='darkred', fontweight='bold')

    # Color palette
    prediction_colors = {
        0: '#4575b4',
        1: '#f46d43',
        2: '#d73027'
    }

    # Plot predictions
    for _, row in gdf.iterrows():
        ax.scatter(row['Longitude'], row['Latitude'],
                   color=prediction_colors.get(row[gdf_column], 'gray'),
                   s=200, edgecolor='black', alpha=0.7, zorder=2)

    # Custom legend (only for first axis if sharing)
    if ax.get_subplotspec().is_first_col():
        legend_handles = [
            mlines.Line2D([], [], marker='o', color='w', label=label,
                          markersize=10, markerfacecolor=color, markeredgecolor='black')
            for label, color in prediction_colors.items()
        ]
        ax.legend(handles=legend_handles, title="Predicted Severity", title_fontsize=13,
                  fontsize=11, frameon=False, loc='center left', bbox_to_anchor=(1.05, 0.5))

    ## Axis limits
    #if cali == False:
    #   ax.set_xlim(-119.5, -117)
     #   ax.set_ylim(32.5, 34.5)
    #elif firename == 'Dixie':
     #   ax.set_xlim(-125, -119)
      #  ax.set_ylim(39, 42.2)

    ax.set_title(f"{gdf_column} - {firename} Fire", fontsize=14, pad=10)
    ax.set_axis_off()

    return ax  # return the axis for optional external control

def grid_kde(df):
    # Configuration
    plots_per_col = 2  # 2 plots vertically stacked per column
    num_plots = len(df.columns)
    cols = math.ceil(num_plots / plots_per_col)
    rows = plots_per_col

    # Create subplots with wider width (for multiple columns)
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    axes = axes.flatten()

    sns.set(style="whitegrid")

    for i, column in enumerate(df.columns):
        sns.kdeplot(
            data=df[column].dropna(),
            ax=axes[i],
            fill=True,
            color='skyblue',
            linewidth=1.5
        )
        axes[i].set_title(column, fontsize=15, weight='bold')
        axes[i].set_xlabel('')
        axes[i].set_ylabel('Density')
        axes[i].tick_params(axis='x', labelsize=10)
        axes[i].tick_params(axis='y', labelsize=10)
        axes[i].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Remove any unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Title below plots
    #plt.figtext(0.5, -0.02, 'KDE Distributions of Damage Measures', 
    #            fontsize=20, weight='bold', ha='center')
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    plt.show()
    
def bar_group(df, target):
    eps = 1e-6
    
    # Assuming X is your feature DataFrame and y is your target Series
    df = df.copy()
    df['Severity Index'] = target

    # Group by severity and take means
    group_means = (
        df.groupby("Severity Index")
          .mean()
          .T
          .abs()
          .fillna(eps)        # replaces NaNs so log works
          .clip(lower=eps)    # forces zeros to eps so log is safe
          .pipe(np.log1p)
    )

    # Plot
    group_means.plot(kind='bar', figsize=(14, 6))
    plt.title("Mean Feature Values by Severity")
    plt.ylabel("Mean Value")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.legend(title='Severity Index')
    plt.show()
