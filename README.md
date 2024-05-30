# Chat Application with Multilingual Support

This is a simple chat application built with Streamlit that supports multiple languages (English, Korean, and German). The application uses OpenAI's language model to generate responses and translates them as necessary.

## Setup and Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/chat-multilingual-app.git
    cd chat-multilingual-app
    ```

2. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Streamlit application**:

    ```sh
    streamlit run webProgram.py
    ```

2. **Access the application**:

    Open your web browser and go to `http://localhost:8501` to interact with the application.

## Usage

1. **Enter your OpenAI API key** in the sidebar.
2. **Type your message** in the text area and click "Submit".
3. The application will **detect the language**, generate a response, and display it in the appropriate language.

## Notes

- This application uses `googletrans` for translation, which is a free and unofficial API for Google Translate. For production-level applications, consider using the official Google Cloud Translation API or another reliable translation service.
- Be mindful of API rate limits for both OpenAI and translation services.
