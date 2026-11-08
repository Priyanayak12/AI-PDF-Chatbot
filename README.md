# AI PDF Question Answering Assistant

An AI-powered PDF Question Answering application built using Python, Streamlit, Gemini API, and Retrieval-Augmented Generation (RAG).

Users can upload PDF documents and ask questions. The application retrieves relevant information from the uploaded document and uses Google's Gemini model to generate answers based on the PDF content.

## Features

- Upload PDF documents.
- Extract text from PDF files.
- Split document text into smaller chunks.
- Generate text embeddings using Sentence Transformers.
- Store and retrieve embeddings using ChromaDB.
- Retrieve relevant content based on user questions.
- Generate natural-language answers using the Gemini API.
- Avoid answering questions when the information is not available in the uploaded PDF.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PyPDF | PDF text extraction |
| LangChain Text Splitters | Document chunking |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database and similarity search |
| Google Gemini API | AI-powered answer generation |

## How It Works

The application follows a Retrieval-Augmented Generation (RAG) workflow.

1. **PDF Upload:** The user uploads a PDF document.
2. **Text Extraction:** PyPDF extracts text from the document.
3. **Text Chunking:** LangChain splits the extracted text into smaller chunks.
4. **Embedding Generation:** Sentence Transformers converts the chunks into numerical embeddings.
5. **Vector Storage:** ChromaDB stores the embeddings and corresponding text.
6. **Information Retrieval:** When a user asks a question, the application retrieves the most relevant chunks.
7. **Answer Generation:** Gemini receives the retrieved content and question, then generates an answer based on the provided context.

## Project Structure

```text
AI-PDF-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**Note:** The `.env` file is created locally and is not uploaded to GitHub because it contains the private Gemini API key.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Priyanayak12/AI-PDF-Chatbot.git
```

Navigate to the project directory:

```bash
cd AI-PDF-Chatbot
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Create a file named `.env` in the project root directory.

Add your API key:

```env
GEMINI_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your own Gemini API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 4. Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Example Usage

1. Open the application.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter a question related to the uploaded PDF.
5. Click **Get Answer**.
6. View the AI-generated response.

If the requested information is not present in the uploaded PDF, the application is instructed to respond:

"The information is not available in the uploaded PDF."

## What I Learned

Through this project, I gained practical experience with:

- Building a Retrieval-Augmented Generation (RAG) application.
- Working with Large Language Models (LLMs).
- Generating text embeddings.
- Understanding vector databases and similarity search.
- Extracting and processing PDF documents.
- Integrating the Gemini API with Python.
- Building interactive applications using Streamlit.

## Future Improvements

- Support multiple PDF documents.
- Improve document retrieval accuracy.
- Add chat history.
- Display relevant source pages.
- Improve the user interface.

## Author

**Priya Rajesh Nayak**

- GitHub: [Priyanayak12](https://github.com/Priyanayak12)
- LinkedIn: [Priya Nayak](https://www.linkedin.com/in/priya-nayak-b9902b316/)

---

If you find this project useful, feel free to explore the repository and try it with your own PDF documents.
