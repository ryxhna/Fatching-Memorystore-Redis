import json

def load_project_ids(json_path):
    """Load project IDs from the JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return data.get("projects", [])

def save_project_ids(project_ids, output_path):
    """Save project IDs to a separate JSON file."""
    with open(output_path, "w") as file:
        json.dump({"projects": project_ids}, file, indent=4)
    print(f"Project IDs saved to {output_path}")

if __name__ == "__main__":
    input_path = "project/NON-PROD.json"
    output_path = "projects_list.json"

    project_ids = load_project_ids(input_path)
    save_project_ids(project_ids, output_path)