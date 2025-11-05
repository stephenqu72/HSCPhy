import plotly.graph_objects as go

def generate_plot():
    # Data points for Sam's journey based on calculations:
    # Phase 1: Walk to park (0-15 min) at 2 m/s
    # Phase 2: Sit at park (15-20 min) at 0 m/s
    # Phase 3: Walk back home (20-40 min) at 1.5 m/s
    
    time_points = [0, 15, 15, 20, 20, 40]
    speed_points = [2, 2, 0, 0, 1.5, 1.5]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_points, y=speed_points, mode='lines', name='Sam\'s Journey',
                             line=dict(color='blue', width=2),
                             hoverinfo='x+y'
                            ))

    fig.update_layout(
        title="Sam's Journey (Speed vs Time)",
        xaxis_title="Time (minutes)",
        yaxis_title="Speed (m s<sup>-1</sup>)",
        xaxis=dict(range=[0, 40], tick0=0, dtick=10, showgrid=True, zeroline=True),
        yaxis=dict(range=[0, 3], tick0=0, dtick=0.5, showgrid=True, zeroline=True),
        hovermode="x unified",
        template="plotly_white",
        showlegend=False,
        height=400, width=600 # Adjust dimensions to resemble options
    )
    return fig