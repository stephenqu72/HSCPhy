import plotly.graph_objects as go

def generate_plot():
    fig = go.Figure()

    # Electric field lines
    y_coords = [-1, -0.5, 0, 0.5, 1]
    for y in y_coords:
        fig.add_shape(type="line", x0=-2, y0=y, x1=2, y1=y, line=dict(color="black", width=1))
        # Add arrow heads as annotations for simplicity
        fig.add_annotation(x=1.8, y=y, ax=1.5, ay=y, xref="x", yref="y", axref="x", ayref="y",
                           showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1, arrowcolor="black")

    # Electron
    fig.add_shape(type="circle", xref="x", yref="y",
                  x0=-0.15, y0=-0.15, x1=0.15, y1=0.15,
                  fillcolor="white", line=dict(color="black", width=1))
    fig.add_annotation(x=0, y=0, text="-", showarrow=False, font=dict(size=16, color="black"))

    # Label for Electric Field E
    fig.add_annotation(x=2.2, y=-0.8, text="E", showarrow=False, font=dict(size=18, color="black"))

    fig.update_layout(
        xaxis=dict(visible=False, range=[-2.5, 2.5]),
        yaxis=dict(visible=False, range=[-1.5, 1.5]),
        showlegend=False,
        width=500,
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig