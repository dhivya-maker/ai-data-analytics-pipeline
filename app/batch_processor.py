import os
import json
import csv
from processor import read_file, process_text
def process_all_files(input_dir, output_dir):
    results = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_dir, file_name)
            text = read_file(input_file_path)
            result = process_text(text)
            results.append(result)
    json_output_file_path = os.path.join(output_dir, "batch_results.json")
    csv_output_file_path = os.path.join(output_dir, "csv_results.json")
    save_json(results, json_output_file_path)
    save_csv(results, csv_output_file_path)
    return results

def save_csv(results, output_file_path):
    if not results:
        return
    fieldnames = results[0].keys()
    with open(output_file_path, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

def save_json(results, output_file_path):
    with open(output_file_path, 'w') as f:
        json.dump(results, f, indent=4)