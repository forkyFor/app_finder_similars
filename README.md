## Prerequisites
Before running this application, ensure you have **Python** installed on your machine. You can download and install it from [python.org](https://www.python.org/downloads/).

## Installation and Setup
Follow these steps to set up and run the application:

### 1️⃣ Update the `.env` file
Add your **OpenAI API Key** to the `.env` file. Open the file and replace `YOUR_OPENAI_API_KEY` with your actual key:

```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

### 2️⃣ Install dependencies
Run the following command to install all required dependencies:

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the application
Start the Streamlit app with:

```sh
streamlit run app.py
```

## Usage
Once the app is running, open your browser and navigate to the provided **localhost URL** (usually `http://localhost:8501`).

You can now interact with the application by entering queries and retrieving similar results based on FAISS and OpenAI embeddings.

## Support
If you encounter any issues, feel free to open an issue on the **GitHub repository**.
