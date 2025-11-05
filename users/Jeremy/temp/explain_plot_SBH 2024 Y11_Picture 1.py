import plotly.graph_objects as go

def generate_plot():
    time = [0, 2, 6, 10]
    velocity = [0, 15, 15, 0]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=time, y=velocity, mode='lines', name='Velocity'))

    fig.update_layout(
        title='Velocity-Time Graph of a Toy Remote Control Car',
        xaxis_title='Time (seconds)',
        yaxis_title='Velocity (ms⁻¹)',
        xaxis=dict(tickvals=[0, 2, 4, 6, 8, 10], range=[0, 10.5]),
        yaxis=dict(tickvals=[0, 5, 10, 15], range=[0, 16]),
        hovermode='x unified',
        font=dict(family="Arial", size=12, color="black")
    )

    # Add vertical dashed lines as in the original image
    fig.add_vline(x=2, line_width=1, line_dash="dash", line_color="gray")
    fig.add_vline(x=6, line_width=1, line_dash="dash", line_color="gray")

    fig.update_yaxes(gridcolor='lightgray')
    fig.update_xaxes(gridcolor='lightgray')

    return fig