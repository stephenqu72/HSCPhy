import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # Define the base function f(x) = sin^-1(x)
    x_f = np.linspace(-1, 1, 100)
    y_f = np.arcsin(x_f)

    # Define the transformed function g(x) = 2 sin^-1(3x)
    x_g = np.linspace(-1/3, 1/3, 100)
    y_g = 2 * np.arcsin(3 * x_g)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x_f, y=y_f,
        mode='lines',
        name='$f(x) = \sin^{-1}(x)$',
        line=dict(color='blue', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=x_g, y=y_g,
        mode='lines',
        name='$g(x) = 2\sin^{-1}(3x)$',
        line=dict(color='red', width=2)
    ))

    fig.update_layout(
        title='Graph Transformations: $f(x) = \sin^{-1}(x)$ to $g(x) = 2\sin^{-1}(3x)$',
        xaxis_title='x',
        yaxis_title='y',
        hovermode='x unified',
        template='plotly_white',
        legend_title='Functions',
        annotations=[
            dict(
                x=0.5, y=np.arcsin(0.5),
                xref='x', yref='y',
                text='f(x)',
                showarrow=True,
                arrowhead=2,
                ax=30, ay=-30
            ),
            dict(
                x=0.15, y=2*np.arcsin(3*0.15),
                xref='x', yref='y',
                text='g(x)',
                showarrow=True,
                arrowhead=2,
                ax=-30, ay=30
            )
        ]
    )
    return fig