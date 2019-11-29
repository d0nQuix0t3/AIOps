import dash
import flask
import dash_core_components as dcc
import dash_html_components as html
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
server.config['ELASTIC_APM'] = {
  # Set required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'apm-dash-service',

  # Use if APM Server requires a token
  'SECRET_TOKEN': '',

  # Set custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'apm-dash:5556',
}
apm = ElasticAPM(server, server_url='http://apmserver:8200', service_name='apm-dash', logging=False)



@server.route('/')
def index():
    return 'Hello Flask app'

@server.route('/test')
def test():
    return 'Hello Test'

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div("My Dash app")

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=5556, debug=False)