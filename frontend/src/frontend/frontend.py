import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# Add backend ip private network 
backend_host = os.getenv("BACKEND_HOST", "192.168.65.5")
backend_port = os.getenv("BACKEND_PORT", 8080)

@app.route('/', methods=['GET', 'POST'])
def index():
    template = "index.html"
    app.logger.info(template)
    if request.method == 'POST':
        id = request.form.get("id")
        name = request.form.get("name")
        try:
            status_code, response = create_user(id, name)
            return render_template(template, status_code=status_code, response=response)
        except Exception as e:
            app.logger.error(e)
    
    return render_template(template)

@app.route('/healthz', methods=['GET'])
def health():
    return jsonify({"frontend_status": "ok", "backend_status": "{}".format(backend_status())})

def backend_status():
    try:
        url = "http://{}:{}/healthz".format(backend_host, backend_port)
        app.logger.info(url)
        r = requests.get(url)
        return "ok"
    except Exception as e:
        app.logger.error(e)
        return "nok"

def create_user(id, name):
    app.logger.info("Received id: %s, name: %s", id, name)
    try:
        url = "http://{}:{}/users".format(backend_host, backend_port)
        json = {"id": int(id), "name": "{}".format(name)}
        app.logger.info("Url {}, Payload {}".format(url, json))

        r = requests.post(url, json=json)
        if r.status_code == 200:
            status_code, response = r.status_code, r.json()
        else:
            status_code, response = r.status_code, None
        
        app.logger.info("Result code {}, Reponse {}".format(status_code, response))
        return status_code, response

    except Exception as e:
        app.logger.error(e)
        
# Add frontend ip private network 
if __name__ == "__main__":
    app.run(debug=True, host="192.168.65.6", port=8000)
