import flask
import time
app = flask.Flask(__name__)

@app.route("/")
def starting_url():
	time.sleep(1)
	status_code = flask.Response(status=201)
	return status_code

app.run(host="0.0.0.0", port=8080, threaded=False)