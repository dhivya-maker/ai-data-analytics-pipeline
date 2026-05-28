
import json
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def process_text(text):
    category="Unknown"
    if "claim" in text.lower():
        category="Claim"
    if "provider" in text.lower():
        issue_type="Missing Provider Information"
    else:
        issue_type="General Issue"
    processed_data = {
        "Summary": text[:100],
        "category": category,
        "issue_type": issue_type
  }
    return processed_data
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)