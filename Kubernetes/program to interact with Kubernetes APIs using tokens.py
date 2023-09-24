import requests
import os

# Define Kubernetes API server URL and service account token
KUBE_API_SERVER = "https://your-kube-api-server-url"
SERVICE_ACCOUNT_TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"

# Define the API endpoint you want to access
API_ENDPOINT = "/api/v1/namespaces/default/pods"

def get_kubernetes_api_response():
    try:
        # Read the service account token from the file
        with open(SERVICE_ACCOUNT_TOKEN_PATH, 'r') as token_file:
            token = token_file.read().strip()

        # Create headers with the Bearer token
        headers = {
            'Authorization': f'Bearer {token}'
        }

        # Make a GET request to the Kubernetes API
        response = requests.get(f'{KUBE_API_SERVER}{API_ENDPOINT}', headers=headers)

        if response.status_code == 200:
            print("API Response:")
            print(response.json())
        else:
            print(f"Failed to fetch data from Kubernetes API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_kubernetes_api_response()
