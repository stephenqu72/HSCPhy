import pandas as pd
import plotly.graph_objects as go

def generate_plot():
    data = {
        "Description": [
            "Number of Junior Teams",
            "Penalty Threshold (players)",
            "Max players per team without penalty",
            "Calculated max total players (no penalty)",
            "Actual total players above age limit"
        ],
        "Value": [
            12,
            "> 3 (i.e., 4 or more)",
            3,
            12 * 3,
            38
        ]
    }
    df = pd.DataFrame(data)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.Description, df.Value],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(title_text="Summary of Information for Penalty Check")
    return fig