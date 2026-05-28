import pandas as pd
def generate_analytics(csv_file_path):
    df=pd.read_csv(csv_file_path)
    print("\n------Analytics Report------")
    print(f"Total Records Processed: {len(df)}")
    category_counts=df.groupby('category').count()
    print(f"Total Categories Processed: {len(category_counts)}")
    issue_type_counts=df.groupby('issue_type').count()
    print(f"Total Issues Processed: {len(issue_type_counts)}")
