import plotly.graph_objects as go

def generate_plot():
    # Calculated heat values (in kJ) based on T_eq = 190.359 °C
    Q1_solid_heating = 0.105
    Q2_solid_melting = 6.6
    Q3_melted_liquid_heating = 9.1627  # 0.030 * 2.13 * (190.359 - 47)
    Q_liquid_cooling = 15.8677 # 0.150065 * 2.13 * (240 - 190.359)

    # Categories for the bars
    labels = [
        "Heat Gained: Solid heating (42°C -> 47°C)",
        "Heat Gained: Solid melting (at 47°C)",
        "Heat Gained: Melted liquid heating (47°C -> T_eq)",
        "Heat Lost: Liquid cooling (240°C -> T_eq)"
    ]
    values = [Q1_solid_heating, Q2_solid_melting, Q3_melted_liquid_heating, Q_liquid_cooling]
    colors = ['#ADD8E6', '#87CEEB', '#4682B4', '#FA8072'] # Light blue for gained components, salmon for lost

    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=colors)])

    fig.update_layout(
        title=f'Heat Exchange in Paraffin Mixture (Equilibrium Temperature: {190.36:.2f} °C)',
        xaxis_title='Process Description',
        yaxis_title='Heat Energy (kJ)',
        # Optional: Add annotations to highlight total gained/lost heat
        annotations=[
            go.layout.Annotation(
                x=1, y=max(values[:3]) + 1.5, # Position above the highest 'gained' bar
                text=f"Total Heat Gained: {(Q1_solid_heating + Q2_solid_melting + Q3_melted_liquid_heating):.2f} kJ",
                showarrow=False,
                font=dict(size=12, color="blue")
            ),
            go.layout.Annotation(
                x=3, y=values[3] + 1.5, # Position above the 'lost' bar
                text=f"Total Heat Lost: {Q_liquid_cooling:.2f} kJ",
                showarrow=False,
                font=dict(size=12, color="red")
            )
        ],
        height=500, 
        width=900,
        xaxis_tickangle=-15 # Slightly tilt x-axis labels if they are long
    )
    return fig