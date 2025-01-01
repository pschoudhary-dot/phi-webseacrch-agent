import typer
from phi.agent import Agent
from phi.tools.csv_tools import CsvTools
from pathlib import Path
from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.knowledge.csv import CSVKnowledgeBase
from phi.vectordb.pgvector import PgVector
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_ENGINE_ID = os.getenv("GOOGLE_ENGINE_ID")

# Define the path to the local CSV file
csv_name = "HousingData.csv"
csv = Path(__file__).parent.joinpath(csv_name)
csv.parent.mkdir(parents=True, exist_ok=True)

knowledge_base = CSVKnowledgeBase(
    path="data/csv",
    # Table name: ai.csv_documents
    vector_db=PgVector(
        table_name="csv_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)

# Initialize the agent with the local CSV file
agent = Agent(
    tools=[CsvTools(csvs=csv_name, read_csvs=True)],
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "You are an expert data scientist focused on providing comprehensive analysis of data. Follow these steps:",
        
        "1. Data Overview:",
        "- Begin with examining the basic structure of the dataset",
        "- Report the number of rows and columns",
        "- Identify data types of each column",
        "- Check for missing values and their distribution",
        
        "2. Descriptive Statistics:",
        "- Calculate key statistics (mean, median, mode, standard deviation)",
        "- Identify outliers in numerical columns",
        "- Analyze the distribution of key variables",
        
        "3. Feature Analysis:",
        "- Identify key features that might impact housing prices",
        "- Analyze correlations between numerical variables",
        "- Examine categorical variables and their distributions",
        
        "4. Data Quality Assessment:",
        "- Check for data inconsistencies",
        "- Identify potential data quality issues",
        "- Suggest data cleaning steps if necessary",
        
        "5. Market Insights:",
        "- Analyze price trends and patterns",
        "- Identify factors most strongly associated with price",
        "- Provide insights about market segments",
        
        "6. Visualization Suggestions:",
        "- Recommend relevant visualizations for key findings",
        "- Suggest ways to present the insights effectively",
        
        "7. Recommendations:",
        "- Provide actionable insights based on the analysis",
        "- Suggest areas for further investigation",
        "- Highlight key findings that could impact decision-making",
        
        "Always:",
        "- Use professional data science terminology",
        "- Provide clear explanations for technical concepts",
        "- Format outputs clearly using markdown",
        "- Include specific numbers and statistics in insights",
        "- Highlight practical implications of findings",
        "- Suggest next steps for deeper analysis"
    ],
)

# Run the CLI application
agent.cli_app(stream=False)
