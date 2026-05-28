from app.processor import save_json
from processor import read_file, process_text
from batch_processor import process_all_files
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
for result in results:
    print(result)
