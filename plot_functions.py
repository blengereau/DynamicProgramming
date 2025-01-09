import plotly.graph_objects as go

def plot_graph(xaxis_title, yaxis_title, title, variable1, variable2=None, variable3=None, variable4=None, showlegend=False):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=variable1[0],
        y=variable1[1],
        mode = "lines",
        name = variable1[2]
    ))
    if variable2:
        fig.add_trace(go.Scatter(
            x=variable2[0],
            y=variable2[1],
            mode = "lines",
            name = variable2[2]
        ))
    if variable3:
        fig.add_trace(go.Scatter(
            x=variable3[0],
            y=variable3[1],
            mode = "lines",
            name = variable3[2]
        ))
    if variable4:
        fig.add_trace(go.Scatter(
            x=variable4[0],
            y=variable4[1],
            mode = "lines",
            name = variable4[2]
        ))
    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        title={
        "text": title,
        "x": 0.5,
        "xanchor": "center"
        },
        showlegend=showlegend
    )
    fig.show()
