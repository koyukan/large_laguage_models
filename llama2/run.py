import http.client
import json
import time

API_HOST = "localhost"
API_PORT = 8000


def generate_text(prompt):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)
    headers = {"Content-type": "application/json"}
    data = {"prompt": prompt}
    json_data = json.dumps(data)
    conn.request("POST", "/generate/", json_data, headers)
    response = conn.getresponse()
    result = json.loads(response.read().decode())
    conn.close()
    return result["task_id"]


def get_task_status(task_id):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)
    conn.request("GET", f"/task/{task_id}")
    response = conn.getresponse()
    status = response.read().decode()
    conn.close()
    return status


def main():
    # Create a while loop to keep asking for prompts 
    # and displaying the generated text until the user exits
    while True:
        # Get the prompt from the user
        prompt = input("Enter the prompt: ")

        # Generate the text using the prompt
        task_id = generate_text(prompt)
        while True:
            status = get_task_status(task_id)
            if "Task not completed yet" not in status:
                print(status)
                break
            time.sleep(2)

        # Ask the user if they want to continue
        continue_prompt = input("Do you want to continue? (y/n): ")
        if continue_prompt.lower() != "y":
            break



if __name__ == "__main__":
    main()
