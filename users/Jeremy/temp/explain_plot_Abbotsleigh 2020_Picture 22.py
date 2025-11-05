import plotly.graph_objects as go

def generate_plot():
    # Coordinates of the 9 points
    # 4 collinear points (approximated from the image, on a line y=0)
    x_collinear = [-2, 0, 2, 4]
    y_collinear = [0, 0, 0, 0]

    # 5 non-collinear points (approximated from the image)
    x_non_collinear = [-3, 1, 3, -1, 5]
    y_non_collinear = [2, -2, 2, -2, -1]

    fig = go.Figure()

    # Plot collinear points
    fig.add_trace(go.Scatter(
        x=x_collinear,
        y=y_collinear,
        mode='markers',
        marker=dict(size=10, color='blue', symbol='circle'),
        name='Collinear Points (4)'
    ))

    # Plot non-collinear points
    fig.add_trace(go.Scatter(
        x=x_non_collinear,
        y=y_non_collinear,
        mode='markers',
        marker=dict(size=10, color='red', symbol='circle'),
        name='Other Points (5)'
    ))

    # Draw the line through the collinear points
    fig.add_trace(go.Scatter(
        x=[min(x_collinear) - 1, max(x_collinear) + 1], # Extend the line slightly
        y=[0, 0],  # All collinear points have y=0
        mode='lines',
        line=dict(color='black', width=2),
        name='Line of Collinearity'
    ))

    fig.update_layout(
        title='Nine Points with Four Collinear',
        xaxis_title='X-coordinate',
        yaxis_title='Y-coordinate',
        showlegend=True,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-4, 6]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3, 3]),
        height=400,
        width=600,
        plot_bgcolor='white'
    )
    return fig