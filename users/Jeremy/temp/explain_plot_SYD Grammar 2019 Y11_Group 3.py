import plotly.graph_objects as go
import numpy as np
import base64

def generate_plot():
    # Time array
    t = np.linspace(0, 10, 100)

    # Positions for Go Kart A and B
    # Line A: (0, 20) to (10, 140)
    # Slope A = (140 - 20) / (10 - 0) = 120 / 10 = 12 m/s
    # Position A = 12*t + 20
    position_A = 12 * t + 20

    # Line B: (0, 0) to (10, 100)
    # Slope B = (100 - 0) / (10 - 0) = 100 / 10 = 10 m/s
    # Position B = 10*t + 0
    position_B = 10 * t

    fig = go.Figure()

    # Add trace for Go Kart A
    fig.add_trace(go.Scatter(x=t, y=position_A, mode='lines', name='A', line=dict(color='black')))

    # Add trace for Go Kart B
    fig.add_trace(go.Scatter(x=t, y=position_B, mode='lines', name='B', line=dict(color='black')))

    # Add labels A and B directly on the lines
    fig.add_annotation(x=10, y=140, text='A', showarrow=False, xanchor='left', yanchor='middle', font=dict(color='black'))
    fig.add_annotation(x=10, y=100, text='B', showarrow=False, xanchor='left', yanchor='middle', font=dict(color='black'))

    # Update layout
    fig.update_layout(
        title='Relative Positions of Go Karts A and B',
        xaxis_title='time (seconds)',
        yaxis_title='Position (metres)',
        xaxis=dict(range=[0, 10], tickmode='linear', dtick=1, showgrid=True, gridwidth=1, gridcolor='LightGrey'),
        yaxis=dict(range=[0, 150], tickmode='linear', dtick=10, showgrid=True, gridwidth=1, gridcolor='LightGrey'),
        plot_bgcolor='white',
        showlegend=False,
        height=500, width=700
    )

    return fig

if __name__ == '__main__':
    fig = generate_plot()
    # For displaying the plot
    # fig.show()
    
    # To save as base64 for embedding (optional, just for demonstration of output format)
    # import io
    # from PIL import Image
    # img_bytes = fig.to_image(format="png")
    # img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    # print(img_base64)