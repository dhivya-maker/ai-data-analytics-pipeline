# Getting Started

## Prerequisites

Before running the project, make sure you have the following installed:

* Python 3.10 or higher
* Git
* OpenAI API Key
* PyCharm (optional)

---

## Clone the Repository

```bash
git clone https://github.com/<your-github-username>/ai-data-analytics-pipeline.git
cd ai-data-analytics-pipeline
```

---

## Create a Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## Configure OpenAI API Key

### Mac/Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Windows

```cmd
set OPENAI_API_KEY=your_api_key_here
```

---

## Project Structure

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
└── README.md
```

---

## Run Batch Processing

Process all input files and generate analytics outputs:

```bash
python3 app/main.py
```

Generated outputs:

```text
output/batch_results.json
output/batch_results.csv
```

---

## Run the Streamlit Dashboard

Launch the dashboard:

```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

## Sample Workflow

1. Add text files to the `input` folder.
2. Run the batch processing pipeline.
3. Review generated JSON and CSV outputs.
4. Launch the Streamlit dashboard.
5. Analyze AI-generated insights and visualizations.

---

## Current Features

* Batch processing of unstructured text files
* OpenAI-powered text analysis
* Structured JSON output
* CSV generation for analytics
* Category classification
* Issue type classification
* Sentiment analysis
* Interactive Streamlit dashboard

---

## Future Enhancements

* File upload through dashboard
* Executive summary generation
* Google Cloud Storage (GCS) integration
* Advanced analytics and visualizations
* Requirement-to-User Story generation
* Product Management workflow automation

```
```
