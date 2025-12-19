from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# -------------------------
# Sample data
# -------------------------
df = pd.DataFrame({
    "year": [2018, 2019, 2020, 2021, 2022],
    "fires": [1200, 1350, 1100, 1600, 1450],
    "acres": [400000, 520000, 300000, 700000, 610000]
})

# -------------------------
# Create figures
# -------------------------
fig1 = px.line(df, x="year", y="fires", title="Fires Over Time")
fig2 = px.line(df, x="year", y="acres", title="Acres Burned Over Time")
fig3 = px.bar(df, x="year", y="fires", title="Fires by Year")
fig4 = px.scatter(df, x="fires", y="acres", title="Fires vs Acres")

# -------------------------
# Create Dash app
# -------------------------
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H4("Model Notes"),
        html.P("• Weather variables show weak standalone correlation."),
        html.P("• Spatial context improves performance."),
        html.P("• Severe fires remain rare (class imbalance).")
    ],
    style={
        "padding": "15px",
        "border": "1px solid #ddd",
        "borderRadius": "5px"
    }),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig4)
],
style={
    "display": "grid",
    "gridTemplateColumns": "1fr 1fr",
    "gap": "20px"
})

# -------------------------
# Run server
# -------------------------
import os

if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8050))
    )