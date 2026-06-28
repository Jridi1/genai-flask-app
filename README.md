# GenAI Flask Application

A web application powered by IBM WatsonX AI models (Granite and Mistral), built with Flask and LangChain. The app provides an interactive chat interface where users can send messages and receive structured AI-generated responses.

## Features

- Chat interface with multiple AI models (Granite, Mistral)
- Structured JSON outputs via LangChain
- Prompt engineering with model-specific templates
- Clean and responsive UI

## Prerequisites

- Python 3.11+
- An IBM Cloud account with WatsonX access
- An IBM Cloud API key

## Getting Your IBM API Key

1. Go to https://cloud.ibm.com/iam/apikeys
2. Click **Create an IBM Cloud API key**
3. Copy the key (it is only shown once)

## Getting Your Project ID

1. Go to https://dataplatform.cloud.ibm.com
2. Open your WatsonX project
3. Click **Manage** — the Project ID is displayed at the top

## Installation

1. Clone the repository
   ```
   git clone https://github.com/jridi1/genai-flask-app.git
   cd genai-flask-app
   ```

2. Create a virtual environment and activate it
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file at the root of the project
   ```
   IBM_API_KEY=your_api_key_here
   IBM_PROJECT_ID=your_project_id_here
   ```

5. Run the application
   ```
   py app.py
   ```

6. Open your browser and go to http://127.0.0.1:5000
