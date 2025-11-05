import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # Constants from the problem
    m_object = 15  # kg
    m_block = 45   # kg
    mu_s = 0.63    # coefficient of static friction
    g = 9.8        # m/s^2

    # Calculate F_f_max (maximum static friction on the object)
    N_object = m_object * g
    F_f_max = mu_s * N_object

    # Calculate a_max (maximum acceleration before slipping)
    a_max = F_f_max / m_object

    # Calculate F_max (maximum applied force F on the block for no slipping)
    m_total = m_object + m_block
    F_max = m_total * a_max

    # Range for F for the plot
    # The plot should go from 0 to F_max
    F_values = np.linspace(0, F_max, 100)

    # Relationship for F_f vs F when they move together
    # F_f = m_object * a
    # a = F / m_total
    # So, F_f = m_object * (F / m_total) = (m_object / m_total) * F
    F_f_values = (m_object / m_total) * F_values

    # Create the plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=F_values,
        y=F_f_values,
        mode='lines',
        name='Static Friction',
        line=dict(color='blue', width=2)
    ))

    # Add a marker for F_max point
    fig.add_trace(go.Scatter(
        x=[F_max],
        y=[F_f_max],
        mode='markers',
        marker=dict(size=8, color='red'),
        name='Limiting Point'
    ))
    
    # Add annotation for the limiting point
    fig.add_annotation(
        x=F_max,
        y=F_f_max,
        text=f'F_max={F_max:.0f} N<br>F_f_max={F_f_max:.1f} N',
        showarrow=True,
        arrowhead=1,
        ax=40,
        ay=-40,
        bordercolor="#c7c7c7",
        borderwidth=1,
        borderpad=4,
        bgcolor="#fffaee",
        opacity=0.8
    )

    fig.update_layout(
        title='Static Friction vs. Applied Force F on the Object',
        xaxis_title='Applied Force F (N)',
        yaxis_title='Static Friction F_f (N)',
        xaxis=dict(range=[0, F_max * 1.1], showgrid=True, gridcolor='lightgray', gridwidth=1, showline=True, linewidth=2, linecolor='black'),
        yaxis=dict(range=[0, F_f_max * 1.1], showgrid=True, gridcolor='lightgray', gridwidth=1, showline=True, linewidth=2, linecolor='black'),
        hovermode='x unified',
        plot_bgcolor='white',
        font=dict(size=12)
    )

    return fig