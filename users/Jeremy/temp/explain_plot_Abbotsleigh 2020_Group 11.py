import plotly.graph_objects as go
import numpy as np

def generate_plot():
    fig = go.Figure()

    # Original function y = f(x) (approximated as ln(x) for plotting)
    # x_f_original = np.linspace(0.01, 4.5, 500)
    # y_f_original = np.log(x_f_original)
    # fig.add_trace(go.Scatter(x=x_f_original, y=y_f_original, mode='lines', name='f(x)', line=dict(color='lightgray', dash='dash')))

    # Step 1: f(|x|) = ln(|x|) (for visualization purposes)
    # x_f_abs = np.concatenate((np.linspace(-4.5, -0.01, 250), np.linspace(0.01, 4.5, 250)))
    # y_f_abs = np.log(np.abs(x_f_abs))
    # fig.add_trace(go.Scatter(x=x_f_abs, y=y_f_abs, mode='lines', name='f(|x|)', line=dict(color='gray', dash='dot')))

    # Step 2: y = 1 / f(|x|) = 1 / ln(|x|) (actual target function)
    # Define x ranges to avoid |x|=0 and |x|=1 due to asymptotes/undefined points
    x1 = np.linspace(-4.5, -1.01, 200)
    y1 = 1 / np.log(np.abs(x1))
    x2 = np.linspace(-0.99, -0.01, 200)
    y2 = 1 / np.log(np.abs(x2))
    x3 = np.linspace(0.01, 0.99, 200)
    y3 = 1 / np.log(np.abs(x3))
    x4 = np.linspace(1.01, 4.5, 200)
    y4 = 1 / np.log(np.abs(x4))

    # Filter out extreme values for better visualization (Plotly automatically handles NaNs by breaking lines)
    y1[np.abs(y1) > 10] = np.nan # Cap vertical range for display clarity
    y2[np.abs(y2) > 10] = np.nan
    y3[np.abs(y3) > 10] = np.nan
    y4[np.abs(y4) > 10] = np.nan

    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', line=dict(color='blue'), showlegend=False))
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', line=dict(color='blue'), showlegend=False))
    fig.add_trace(go.Scatter(x=x3, y=y3, mode='lines', line=dict(color='blue'), showlegend=False))
    fig.add_trace(go.Scatter(x=x4, y=y4, mode='lines', line=dict(color='blue'), showlegend=False))

    # Add vertical asymptotes for y = 1/f(|x|) at x = +/- 1
    fig.add_vline(x=1, line_width=1, line_dash='dash', line_color='red')
    fig.add_vline(x=-1, line_width=1, line_dash='dash', line_color='red')

    # Add horizontal asymptote for y = 1/f(|x|) at y = 0
    fig.add_hline(y=0, line_width=1, line_dash='dash', line_color='red')

    # Add open circle at (0,0) to indicate the limit as x->0 and undefined point
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='blue', size=8, line=dict(width=2, color='blue')), showlegend=False))

    fig.update_layout(
        title='Graph of y = 1 / f(|x|) (f(x) approximated as ln(x))',
        xaxis_title='x',
        yaxis_title='y',
        xaxis_range=[-4.5, 4.5],
        yaxis_range=[-4.5, 2.5], # Adjusted range to better match the options' view
        showlegend=False,
        height=400, width=600
    )

    return fig