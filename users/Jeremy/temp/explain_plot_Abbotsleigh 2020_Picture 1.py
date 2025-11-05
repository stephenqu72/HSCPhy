import plotly.graph_objects as go
import math
import base64

def generate_plot():
    boys = 5
    girls = 3

    # Step 1: Treat girls as a single unit
    num_units = boys + 1 # 5 boys + 1 group of girls
    arrangement_units = math.factorial(num_units)

    # Step 2: Arrange girls within their unit
    arrangement_girls_internal = math.factorial(girls)

    # Step 3: Total arrangements
    total_arrangements = arrangement_units * arrangement_girls_internal

    # Create a Plotly table to represent the data and steps
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Description', 'Calculation', 'Result'],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[
            ['Number of Boys', 'Number of Girls', 'Girls treated as 1 block', 'Total items (units) to arrange', 'Arrangements of units (N!)', 'Arrangements within girls block (M!)', 'Total Ways (N! * M!)'],
            [boys, girls, '1 block', f'{boys} + 1 = {num_units}', f'{num_units}!', f'{girls}!', f'{num_units}! × {girls}!'],
            ['-', '-', '-', '-', arrangement_units, arrangement_girls_internal, total_arrangements]
        ],
        fill_color='lavender',
        align='left'))
    ])
    fig.update_layout(title_text="Combinatorics Problem Breakdown")
    return fig

# The function is called elsewhere to generate the figure.
# For the purpose of this JSON structure, the code for the function itself is provided.