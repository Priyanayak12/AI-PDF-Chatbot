
import streamlit as st
import chromadb
import os

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.title("AI PDF Question Answering Assistant")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    if not text.strip():
        st.warning("No readable text found in this PDF.")

    else:
        st.success("PDF text extracted!")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_text(text)

        st.write("Total chunks:", len(chunks))

        if chunks:

            embeddings = model.encode(chunks)

            db = chromadb.Client()

            collection = db.get_or_create_collection(
                name="pdf_data"
            )

            old_data = collection.get()

            if old_data["ids"]:
                collection.delete(ids=old_data["ids"])

            collection.add(
                ids=[str(i) for i in range(len(chunks))],
                documents=chunks,
                embeddings=embeddings.tolist()
            )

            st.success("PDF stored in ChromaDB!")

            st.subheader("Ask your question")

            question = st.text_input("Enter your question")

            if st.button("Get Answer"):

                if not question.strip():
                    st.warning("Please enter a question.")

                else:

                    question_embedding = model.encode(question)

                    results = collection.query(
                        query_embeddings=[
                            question_embedding.tolist()
                        ],
                        n_results=min(3, len(chunks))
                    )

                    context = "\n\n".join(
                        results["documents"][0]
                    )

                    api_key = os.getenv("GEMINI_API_KEY")

                    if not api_key:
                        st.error("Gemini API key not found in .env file.")

                    else:
                        try:
                            with st.spinner("Generating answer..."):

                                client = genai.Client(
                                    api_key=api_key
                                )

                                response = client.interactions.create(
                                    model="gemini-3.8-flash",
                                    input=f"""
Answer the question using only the PDF content below.

If the answer is not present, say:
"The information is not available in the uploaded PDF."

PDF content:
{context}

Question:
{question}
"""
                                )

                            st.subheader("Answer")
                            st.write(response.output_text)

                        except Exception as e:
                            st.error(f"Gemini error: {e}")
