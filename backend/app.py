from flask import Flask, jsonify, send_from_directory, request
from wmr_cba import wmr_cba 
import os
from platformdirs import user_data_dir
import time
from flask_cors import CORS
INITIALDELAY = 0.78
app = Flask(__name__)
CORS(app)
cba = None
start_time = None
time_count = 0
current_values = []
drop_voltage_found = False
def connect():
    global cba
    devices = wmr_cba.CBA4.scan()
    if not devices:
        return jsonify({"message": "No devices found. Connect a CBA IV device and try again."}), 400
    try:
        cba = wmr_cba.CBA4()
        return jsonify({"message": "Connected!"}), 200
    except Exception as error:
        return jsonify({"message": f"Connection failed. Error: {str(error)}"}), 400

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/hello")
def hello():
    data = "a"
    return jsonify({"message": f"Hello from Flask! Data: {data}"})
@app.route("/api/sanity_test")
def sanity_test():
    if cba is None:
        return jsonify({"error": "CBA device is not initialized"}), 500
    schema = []
    cba.do_start(0.2)
    time.sleep(INITIALDELAY)
    for i in range(10):
        schema.append({"Time": f"{i}", "Voltage": cba.get_voltage()})
        time.sleep(1)
    cba.do_stop()
    print(schema)
    return jsonify(schema)

@app.route("/api/connect", methods=["GET"])
def connect_device():
    response, status_code = connect()
    return response, status_code



@app.route("/api/start_test", methods=["POST"])
def start_test():
    config = request.get_json()
    # print(config)
    global cba
    global start_time
    global time_count
    if cba is None:
        return jsonify({"error": "CBA device is not initialized"}), 500
    cba.do_start(config["current"], config["cutoff"])
    if config == {}:
        return jsonify({"error": "No configuration provided"}), 400
    time_count = 0
    start_time = time.time()
    time.sleep(INITIALDELAY)
    final_configuration = {"Battery": config["name"],
                    "Initial Voltage": cba.get_voltage(),
                    "Cutoff Voltage": config["cutoff"],
                    "Current": config["current"]}
    # print(final_configuration)
    return jsonify(final_configuration), 200


@app.route("/api/data_collection")
def test_collect():
    global cba
    global time_count
    global current_values
    global start_time
    if cba is None:
        return jsonify({"error": "CBA device is no longer initialized, physical intervention is recommended."}), 500
    if cba.is_running() == False:
        return jsonify({"Status": "Complete", "Peak Voltage": max(current_values), "End Time": time.time()-start_time}), 200
    a = cba.get_voltage()
    collection = {"Status": "Running","Time": time_count, "Voltage": a, 'Predicted Voltage': 0}
    current_values.append(a)
    if a > current_values[-1] and not drop_voltage_found:
        drop_voltage_found = True
        collection['Drop Voltage Detected'] = a
        current_values = []
    time_count += 1
    # print(collection)
    return jsonify(collection)

@app.route("/api/emergency" , methods=["GET"])
def emergency():
    try:
        cba.do_stop()
        return jsonify({"message": "EMERGENCY COMPLETED"})
    except Exception as error:
        return jsonify({"message": "EMERGENCY SHUTDOWN FAILED, PHYSICAL/DIVINE INTERVENTION NOW MANDATORY"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)