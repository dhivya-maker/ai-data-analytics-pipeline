def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def process_text(text):
    return {
        "summary":text[:50],
        "category":"Claims"
    }