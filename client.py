import requests

API_URL = "http://localhost:5000"

def menu():
    while True:
        print("\nCluster Simulation CLI")
        print("1. Add Node")
        print("2. List Nodes")
        print("3. Launch Pod")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cpu = int(input("Enter CPU cores: "))
            response = requests.post(f"{API_URL}/add_node", json={"cpu": cpu})
            print(response.json())

        elif choice == "2":
            response = requests.get(f"{API_URL}/list_nodes")
            print(response.json())

        elif choice == "3":
            cpu = int(input("Enter required CPU: "))
            response = requests.post(f"{API_URL}/launch_pod", json={"cpu": cpu})
            print(response.json())

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
