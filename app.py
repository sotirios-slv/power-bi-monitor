from dash import Dash, html, dcc

from shared_power_bi import get_refresh_history

power_bi_refresh_history = get_refresh_history()
columns = ['Workspace', 'Refresh status', 'Attempted refreshes', 'Failed refreshes']

def generate_table(refresh_history):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in columns])
        ),
        html.Tbody([
            html.Tr()
        ])
    ])

app = Dash(__name__)


app.layout = html.Div([
    html.H1(children='PebbleDash')
])


if __name__== '__main__':
    app.run_server(debug=True)