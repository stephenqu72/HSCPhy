import plotly.graph_objects as go

def generate_plot():
    prices = [3.00, 3.50, 4.00, 4.50, 5.00]
    quantities = [550, 530, 520, 500, 400]
    total_outlay = [p * q for p, q in zip(prices, quantities)]

    data_points = []
    for i in range(len(prices)):
        data_points.append({
            "Price ($)": prices[i],
            "Quantity (number of bottles)": quantities[i],
            "Total Outlay ($)": total_outlay[i]
        })

    # Filter for the specific range for the plot if needed, or show all data
    relevant_prices = [4.00, 4.50]
    relevant_quantities = [520, 500]
    relevant_total_outlay = [2080, 2250]

    # Create a table to display the relevant calculations
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Price ($)', 'Quantity (bottles)', 'Total Outlay ($)'],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[relevant_prices, relevant_quantities, relevant_total_outlay],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(title_text='Total Outlay Calculation for Price Elasticity', title_x=0.5)

    return fig