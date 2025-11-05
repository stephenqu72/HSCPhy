import plotly.graph_objects as go
import json

def generate_plot():
    fig = go.Figure()

    # Electric field lines (conceptual representation)
    y_positions = [-0.1, 0, 0.1, 0.2]
    for y_pos in y_positions:
        fig.add_shape(
            type="line",
            x0=0.1, y0=y_pos, x1=0.9, y1=y_pos,
            line=dict(color="blue", width=2)
        )
        # Add arrowheads to represent direction of E field
        fig.add_annotation(
            x=0.9, y=y_pos, # Arrow tip
            ax=0.8, ay=y_pos, # Arrow base
            xref="x", yref="y", axref="x", ayref="y",
            showarrow=True,
            arrowhead=2, arrowsize=1, arrowwidth=1, arrowcolor="blue"
        )
    
    # Label for Electric Field E
    fig.add_annotation(
        x=0.95, y=-0.15,
        text="E",
        showarrow=False,
        font=dict(size=16, color="blue")
    )

    # Electron (negative charge symbol)
    fig.add_annotation(
        x=0.5, y=0.05,
        text="−e",
        showarrow=False,
        font=dict(size=20, color="red")
    )

    # Force on electron (opposite to E field)
    fig.add_annotation(
        x=0.4, y=0.05, # Arrow tip for force
        ax=0.6, ay=0.05, # Arrow base for force
        xref="x", yref="y", axref="x", ayref="y",
        text="F",
        showarrow=True,
        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="green",
        font=dict(size=16, color="green")
    )
    
    fig.update_layout(
        title="Force on Electron in Uniform Electric Field",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.2, 0.3]),
        plot_bgcolor='white',
        annotations=[
            # Invisible boundaries for better scaling of annotations
            dict(x=0, y=0, xref='paper', yref='paper', showarrow=False, text=''),
            dict(x=1, y=1, xref='paper', yref='paper', showarrow=False, text='')
        ]
    )
    
    return fig