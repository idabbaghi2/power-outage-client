import requests
import json

BASE_URL = "http://localhost:5000/v1"

def report_power_outage(outage_data):
    url = f"{BASE_URL}/poweroutage"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=outage_data)
    if response.status_code == 201:
        print("Outage reported successfully.")
    else:
        print(f"Error {response.status_code}: {response.text}")
    return response.json() if response.content else None

def get_all_power_outages():
    url = f"{BASE_URL}/poweroutage"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def get_power_outage_by_id(outage_id):
    url = f"{BASE_URL}/poweroutage/{outage_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Outage not found.")
    else:
        print(f"Error {response.status_code}: {response.text}")
    return None

# Example usage:
if __name__ == "__main__":
    example_outage = {
        "grid_operator": "BKW",
        "outage_type": "Power Outage",
        "description": "Maintenance due to grid overload.",
        "start_time": "2025-03-04T14:00:00Z",
        "estimated_end": "2025-03-04T18:00:00Z",
        "status": "In Progress",
        "affected_areas": [
            {
                "name": "Bern",
                "coordinates": {
                    "latitude": 46.9481,
                    "longitude": 7.4474
                }
            }
        ],
        "affected_customers": 1500,
        "report_source": "Automated Monitoring",
        "last_update": "2025-03-04T14:30:00Z"
    }




