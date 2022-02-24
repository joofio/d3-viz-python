from flask import Flask, render_template,jsonify
import json
app = Flask(__name__)

# Import DataFrame
PATH_IN = "static/data/miserables.json"

# Routing do define url
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-json', methods=['GET', 'POST'])
def get_json():
    ''' Send JSON data to Javascript '''
    # Import Data
    with open(PATH_IN) as f:
        json_to = json.load(f)
    #print(json_to)
    return jsonify(json_to)   


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, port=5000)