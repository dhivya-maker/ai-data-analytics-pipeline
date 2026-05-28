from app.analytics import generate_analytics
from app.processor import save_json
from processor import read_file, process_text
#commenting this import to include the ai processor
#from batch_processor import process_all_files
from ai_batch_processor import process_all_files
#code to process single file
text=read_file("../input/sample_data_1.txt")
result=process_text(text)
save_json("../output/output.txt", result)

#for batch processing
input_folder = "../input"
output_folder = "../output"
results = process_all_files(input_folder, output_folder)
print("Batch processing complete")
print(f"Total files processed: {len(results)}")
csv_path = f"{output_folder}/csv_results.csv"
generate_analytics(csv_path)