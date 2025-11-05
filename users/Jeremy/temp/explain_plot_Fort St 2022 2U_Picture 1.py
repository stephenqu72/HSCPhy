```python
import plotly.express as px
import pandas as pd

# Data for 2010
ages_2010 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
values_2010 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2500]

# Data for 2000
ages_2000 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
values_2000 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2500]

# Create a DataFrame
df_2010 = pd.DataFrame({'Age': ages_2010, 'Count': values_2010})
df_2000 = pd.DataFrame({'Age': ages_2000, 'Count': values_2000})

# Function to generate the plot
def generate_plot(df, year):
    fig = px.box(df, x='Age', y='Count', title=f'Distribution of the ages of children in Numbertown {year}',
                 labels={'Age': 'Age (years)', 'Count': 'Number of children'},
                 points='all', notched=True)
    fig.update_layout(margin=dict(l=100, r=100, t=100, b=100))
    return fig

# Generate the plot for 2010
fig_2010 = generate_plot(df_2010, 2010)
fig_2010
```