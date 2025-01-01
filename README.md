# CSV Reader Agent

## Overview
The CSV Reader Agent is designed to provide comprehensive analysis of data from CSV files. It performs data overview, descriptive statistics, feature analysis, data quality assessment, and provides market insights.

## Features
- **Data Overview**: Examines the basic structure of the dataset, reports the number of rows and columns, identifies data types, and checks for missing values.
- **Descriptive Statistics**: Calculates key statistics, identifies outliers, and analyzes the distribution of key variables.
- **Feature Analysis**: Identifies key features impacting housing prices, analyzes correlations, and examines categorical variables.
- **Data Quality Assessment**: Checks for data inconsistencies, identifies potential data quality issues, and suggests data cleaning steps.
- **Market Insights**: Provides insights based on the data analysis.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/pschoudhary-dot/phi-webseacrch-agent.git
    cd phi-webseacrch-agent
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your database credentials:
    ```plaintext
    DB_URL=postgresql+psycopg://ai:ai@localhost:5532/ai
    ```

## Usage

Run the [csv-reader_agent.py](http://_vscodecontentref_/1) script to start the agent:
```bash
python csv-reader_agent.py
```

# Web Search Agent

## Overview
The Web Search Agent is designed to assist in content research by gathering, analyzing, and summarizing information on specified topics. It conducts keyword research, identifies trending topics, collects data from reputable sources, and provides summaries and briefs to streamline the research phase for human content creators.

## Features
- **Keyword Research**: Identifies relevant keywords and trending topics.
- **Data Collection**: Gathers data and insights from reputable sources.
- **Summarization**: Provides concise summaries and briefs for content creators.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/pschoudhary-dot/phi-webseacrch-agent.git
    cd phi-webseacrch-agent
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your Google API credentials:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    GOOGLE_ENGINE_ID=your_google_engine_id
    ```

## Usage

Run the [Multi_search_agent.py](http://_vscodecontentref_/1) script to start the agent:
```bash
python Multi_search_agent.py
```

