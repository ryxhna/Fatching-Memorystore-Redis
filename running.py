import json
import pandas as pd
from main import get_redis_info 

def load_project_ids(json_path):
    """Load project IDs from the JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return data.get("projects", [])

def save_to_json(data, output_path):
    """Save data to a JSON file."""
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to JSON file: {output_path}")

def save_to_excel(data, output_path):
    """Save data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    print(f"Data saved to Excel file: {output_path}")

if __name__ == "__main__":
    input_path = "project/NON-PROD.json"
    json_output_path = "output/Asset List Memorystore Redis NON-PROD GCP.json"
    excel_output_path = "output/Asset List Memorystore Redis NON-PROD GCP.xlsx"

    # Load project IDs
    project_ids = load_project_ids(input_path)

    # Fetch Redis instance information for all projects
    all_redis_info = []
    for project_id in project_ids:
        redis_info = get_redis_info(project_id)
        all_redis_info.extend(redis_info)

    # Save the combined Redis instance information
    save_to_json(all_redis_info, json_output_path)
    save_to_excel(all_redis_info, excel_output_path)
