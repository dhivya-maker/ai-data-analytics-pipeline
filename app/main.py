from app.processor import save_json
from processor import read_file, process_text
text=read_file("../input/sample.txt")
result=process_text(text)
save_json("../output/output.txt", result)
