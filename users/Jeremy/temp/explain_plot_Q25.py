import plotly.graph_objects as go

def generate_plot():
    # Data for the table
    data = {
        "Variable": ["R", "I₁", "I₂"],
        "Value": ["18 Ω", "0.50 A", "0.25 A"]
    }

    # Create a Plotly table
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.keys()),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[data[col] for col in data.keys()],
                   fill_color='lavender',
                   align='left'))
    ])
    
    fig.update_layout(title_text="Calculated Values for R, I₁, and I₂", title_x=0.5)
    return fig