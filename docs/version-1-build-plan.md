# Version 1 Build Documentation

# AI Data Analytics Pipeline

## Project Goal

Build a Python-based AI data analytics pipeline that processes unstructured text files, uses OpenAI to extract structured insights, generates JSON and CSV outputs, and displays the results in a Streamlit dashboard.

---

## Version 1 Scope

Version 1 focuses on building the core end-to-end workflow:

```text
Unstructured text files
→ Batch processing
→ OpenAI analysis
→ Structured JSON output
→ CSV analytics file
→ Streamlit dashboard
```

---

## Step 1: Create GitHub Repository

Repository name:

```text
ai-data-analytics-pipeline
```

Repository description:

```text
AI-powered data analytics pipeline for processing unstructured data and generating actionable business insights.
```

Purpose:

* Showcase AI workflow development
* Practice Python and data analytics
* Build a portfolio project for Technical Product Owner / AI Product roles

---

## Step 2: Set Up Local Development Environment

Tools used:

* PyCharm
* Python 3
* Git
* GitHub
* GitHub Copilot

Actions completed:

* Installed Python 3
* Configured Python interpreter in PyCharm
* Connected local project to GitHub
* Made first Git commit

---

## Step 3: Create Project Structure

Initial folder structure:

```text
ai-data-analytics-pipeline/

├── app/
│   ├── main.py
│   ├── processor.py
│   ├── ai_processor.py
│   ├── ai_batch_processor.py
│   └── analytics.py
│
├── input/
│   ├── sample_data.txt
│   ├── sample_data_2.txt
│   └── sample_data_3.txt
│
├── output/
│   ├── batch_results.json
│   └── batch_results.csv
│
├── dashboard.py
├── requirements.txt
├── README.md
└── docs/
```

---

## Step 4: Add Sample Unstructured Data

Created sample text files inside the `input` folder.

Example:

```text
Customer reported delayed claim processing.
Provider information missing.
Escalated to claims team.
```

Purpose:

* Simulate real-world unstructured customer support or claims notes
* Provide test data for the pipeline
* Keep the project simple but business-relevant

---

## Step 5: Build Basic Text Processor

Created `processor.py`.

Purpose:

* Read text files
* Provide basic rule-based processing before AI integration

Key functions:

```python
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
```

This established the first part of the pipeline:

```text
Read file → Extract text
```

---

## Step 6: Build Batch Processing

Created `ai_batch_processor.py`.

Purpose:

* Read all `.txt` files from the `input` folder
* Process each file
* Store results in a list
* Save output as JSON and CSV

Workflow:

```text
Loop through input folder
→ Read each text file
→ Send text for AI processing
→ Add source file name
→ Save batch results
```

Outputs generated:

```text
output/batch_results.json
output/batch_results.csv
```

---

## Step 7: Integrate OpenAI Processing

Created `ai_processor.py`.

Purpose:

* Send unstructured text to OpenAI
* Extract structured fields

Fields extracted:

* Summary
* Category
* Issue Type
* Priority
* Sentiment

Model used:

```text
gpt-4.1-mini
```

Reason for choosing this model:

* Low cost
* Fast response
* Good for summarization and classification
* Suitable for learning and portfolio projects

---

## Step 8: Fix AI JSON Response Parsing

Issue encountered:

OpenAI returned responses inside markdown code blocks:

````text
```json
{
  "summary": "...",
  "category": "..."
}
````

````

Problem:

`json.loads()` failed because markdown text is not valid JSON.

Fix added:

```python
result = response.output_text.strip()
result = result.replace("```json", "")
result = result.replace("```", "")
result = result.strip()
````

Learning:

This showed an important real-world GenAI challenge:

```text
AI output must be cleaned and validated before downstream processing.
```

---

## Step 9: Generate Analytics Report

Created `analytics.py`.

Purpose:

* Read processed CSV file
* Generate basic analytics

Analytics included:

* Total records processed
* Category distribution
* Issue type distribution
* Sentiment distribution

Example output:

```text
Total Records Processed: 3
Category Distribution: Claims, Billing, Eligibility
Issue Type Distribution: Payment Delay, Coverage Status, Delayed Processing
```

---

## Step 10: Create Streamlit Dashboard

Created `dashboard.py`.

Purpose:

* Display processed AI output visually
* Make the project easier to understand for recruiters and reviewers

Dashboard features:

* Display processed records in a table
* Show category distribution
* Show issue type distribution
* Show sentiment distribution
* Display total records processed

Run command:

```bash
streamlit run dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## Step 11: Add Requirements File

Created `requirements.txt`.

Packages included:

```text
openai
pandas
streamlit
google-cloud-storage
matplotlib
```

Purpose:

* Help others install project dependencies
* Make the project easier to run locally

Install command:

```bash
python3 -m pip install -r requirements.txt
```

---

## Step 12: Add README Documentation

Updated `README.md` with:

* Project overview
* Business problem
* Solution architecture
* Features
* Technology stack
* Project structure
* Setup instructions
* How to run batch processing
* How to run Streamlit dashboard
* Future enhancements

Purpose:

* Make the GitHub repository professional
* Help others understand and run the project
* Support portfolio presentation

---

## Version 1 Final Workflow

```text
1. Add text files to input folder
2. Run main.py
3. AI processes each file
4. Results are saved to JSON and CSV
5. Analytics are generated
6. Streamlit dashboard displays the insights
```

---

## Version 1 Features Completed

* GitHub repository setup
* Local PyCharm project setup
* Python environment configuration
* Batch processing of text files
* OpenAI API integration
* JSON response cleanup
* CSV and JSON output generation
* Basic analytics reporting
* Streamlit dashboard
* README documentation
* Git commits for project tracking

---

## Key Problems Solved

### Problem 1: Environment Setup Issues

Resolved:

* Old Git path issue
* Old pip/Python 2 issue
* Python interpreter setup in PyCharm

### Problem 2: API Key Setup

Resolved:

* Configured OpenAI API key
* Tested available OpenAI models
* Confirmed access to `gpt-4.1-mini`

### Problem 3: AI Response Parsing

Resolved:

* Cleaned markdown formatting from AI output
* Converted AI output into valid JSON

---

## Skills Demonstrated

This project demonstrates:

* Python development
* AI API integration
* Prompt engineering
* JSON and CSV processing
* Batch file processing
* Data analytics
* Streamlit dashboard development
* Git and GitHub workflow
* Debugging and problem solving
* AI workflow orchestration
* Business insight generation

---

## Product Thinking Behind Version 1

The project solves a real business problem:

Organizations often receive large amounts of unstructured text data. Manually reviewing this data is time-consuming and inconsistent.

This project helps convert raw text into structured business insights that can support:

* Customer support analysis
* Claims analysis
* Operational reporting
* Business decision-making
* Executive dashboards

---

## Version 2 Project Plan

Planned next features:

### 1. File Upload Through Dashboard

Allow users to upload files directly through Streamlit instead of manually placing files in the `input` folder.

### 2. AI Executive Summary

Generate a high-level summary such as:

```text
Three records were analyzed. Billing and claims issues were the most common. Two high-priority cases require follow-up.
```

### 3. Better Dashboard Visuals

Add:

* KPI cards
* Bar charts
* Sentiment charts
* Priority breakdown
* Issue distribution

### 4. Google Cloud Storage Integration

Future workflow:

```text
GCS bucket
→ Read input files
→ AI processing
→ Upload structured results
```

### 5. Product Management Extension

Add a new workflow:

```text
Requirement document
→ AI summary
→ Epics
→ User stories
→ Acceptance criteria
```

---

## Version 1 Status

Status:

```text
Completed
```

Version 1 successfully proves the core concept:

```text
Unstructured data can be processed with AI and transformed into structured analytics for business insights.
```
