from flask import Flask, request, jsonify

app = Flask(__name__)

nodes = {}  # Dictionary to store nodes
pods = []  # List to store pods

@app.route("/add_node", methods=["POST"])
def add_node():
    node_id = f"node-{len(nodes) + 1}"
    cpu = request.json.get("cpu", 1)
    nodes[node_id] = {"cpu": cpu, "status": "Healthy", "pods": []}
    return jsonify({"message": f"Node {node_id} added", "node_id": node_id})

@app.route("/list_nodes", methods=["GET"])
def list_nodes():
    return jsonify(nodes)

@app.route("/launch_pod", methods=["POST"])
def launch_pod():
    required_cpu = request.json.get("cpu", 1)
    for node_id, node in nodes.items():
        if node["cpu"] >= required_cpu:
            pod_id = f"pod-{len(pods) + 1}"
            node["pods"].append(pod_id)
            pods.append(pod_id)
            return jsonify({"message": f"Pod {pod_id} assigned to {node_id}", "pod_id": pod_id})
    return jsonify({"message": "No available node found"}), 400

@app.route('/')
def home():
    return jsonify({"message": "Cluster Simulation API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
