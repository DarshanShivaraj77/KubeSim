# KubeSim - Kubernetes-like Cluster Simulation Framework

## Overview
KubeSim is a lightweight, Kubernetes-like **Distributed Cluster Simulation Framework** built with Python, Flask, and Docker. It allows users to:
- Add and manage nodes.
- Schedule and launch pods.
- Monitor system health and detect failures.

This project is designed for educational and research purposes to simulate distributed systems without needing a full Kubernetes setup.

---

## Features
✅ **Node Management** - Add, remove, and list nodes dynamically.  
✅ **Pod Scheduling** - Simulate resource-based pod allocation.  
✅ **Health Monitoring** - Detect and manage unhealthy nodes.  
✅ **Docker Integration** - Nodes are simulated as Docker containers.  
✅ **CLI & API** - Interact via CLI and REST API.

---

## Getting Started
Follow these steps to set up and run KubeSim on your local system.

### **1. Clone the Repository**
```sh
# Clone the repository
git clone https://github.com/DarshanShivaraj77/KubeSim.git

# Navigate into the project directory
cd KubeSim
```

### **2. Setup Virtual Environment** (Recommended)
```sh
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Start the API Server**
```sh
python3 api_server.py
```
The server should now be running at `http://127.0.0.1:5000`.

### **5. Build and Run Nodes with Docker**

#### **5.1 Create a Dockerfile**
Create a file named `Dockerfile` inside the project directory with the following content:
```Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY node.py .
RUN pip install requests
CMD ["python3", "node.py"]
```

#### **5.2 Build and Run Node Containers**
```sh
# Build the Docker image
docker build -t node_simulation .

# Run a new container instance
docker run -d node_simulation
```

### **6. Run the CLI Interface**
```sh
python3 client.py
```
This will start the CLI for managing the cluster.

---

## API Endpoints
| Endpoint          | Method | Description               |
|------------------|--------|---------------------------|
| `/add_node`      | POST   | Adds a new node           |
| `/list_nodes`    | GET    | Lists all nodes           |
| `/launch_pod`    | POST   | Launches a new pod        |

---

## Usage Guide
### **6.1 Adding a Node**
```sh
Enter CPU cores: 4
Response: {"message": "Node node-1 added", "node_id": "node-1"}
```

### **6.2 Listing Nodes**
```sh
Response: {"node-1": {"cpu": 4, "status": "Healthy", "pods": []}}
```

### **6.3 Launching a Pod**
```sh
Enter required CPU: 2
Response: {"message": "Pod pod-1 assigned to node-1", "pod_id": "pod-1"}
```

---

## Contributing
Feel free to contribute to this project! Follow these steps:
```sh
# Fork the repository
# Make changes and commit
# Push changes to your fork
# Open a Pull Request
```

---

## License
This project is open-source under the MIT License.

---

## Contact
For any questions, reach out via GitHub Issues or email `darshanshivaraj77@gmail.com`.

