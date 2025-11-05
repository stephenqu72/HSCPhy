import plotly.graph_objects as go
import numpy as np

fig = go.Figure()

# Circle: |z - 2i| = 1, center (0, 2), radius 1
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = 2 + np.sin(theta)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Circle'))

# Tangent point at (-√3/2, 3/2)
fig.add_trace(go.Scatter(x=[-np.sqrt(3)/2], y=[3/2], mode='markers', marker=dict(size=10, color='red'), name='Maximum arg(z)'))

# Origin and tangent line (y = -√3 x)
fig.add_trace(go.Scatter(x=[-np.sqrt(3)/2, 0], y=[3/2, 0], mode='lines', name='Tangent Line'))

# Real axis
fig.add_trace(go.Scatter(x=[-1, 1], y=[0, 0], mode='lines', name='Real Axis'))

# Set title and labels
fig.update_layout(
    title='Circle and Maximum Argument of z',
    xaxis_title='Real Axis',
    yaxis_title='Imaginary Axis',
    showlegend=True
)

fig.show()