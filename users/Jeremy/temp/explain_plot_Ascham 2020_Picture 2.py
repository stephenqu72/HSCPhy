import plotly.graph_objects as go
import numpy as np

def generate_plot():
    fig = go.Figure()
    x = np.linspace(-5, 5, 100)
    y = (x + 1j)**4
    fig.add_trace(go.Scatter(x=x.real, y=y.real, mode='lines', name='Real part'))
    fig.add_trace(go.Scatter(x=x.real, y=y.imag, mode='lines', name='Imaginary part'))
    fig.update_layout(title='Roots of $z^4 + \cdots + E = 0$', xaxis_title='Real', yaxis_title='Imaginary')
    return fig