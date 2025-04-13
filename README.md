
# 🧹 RAG Backend + Streamlit App

This project allows you to **chat with your PDF documents** using Retrieval-Augmented Generation (RAG), powered by **Google Gemini API**, **Langchain**, and **Streamlit**.

You'll upload a PDF, and the app will:

- Parse and chunk the document
- Embed the chunks using Google's Generative AI embeddings
- Store and retrieve embeddings using ChromaDB
- Generate answers to your questions about the document

### 🚀 Features

- 📝 Upload any PDF
- 🔍 Ask natural language questions
- ⚡ Instant answers from your document context
- 🌐 Deploy with Streamlit + Ngrok

---

## 🔮 Future Improvements

- ✅ Support for multiple PDFs
- ✅ Better UI/UX in Streamlit
- ✅ Add caching for embeddings
- ✅ Deployment to cloud platforms (GCP / AWS / HuggingFace Spaces)
- ✅ Multi-language support

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install streamlit langchain langchain-google-genai langchain_community pypdf chromadb sentence-transformers pdfplumber pyngrok

```

### 2. Configure API Keys

Make sure to set your environment variables. In Colab, you can use:

```python
from google.colab import userdata
os.environ['GOOGLE_API_KEY'] = userdata.get('GEMINI_API_KEY')
os.environ['NGROK_AUTH_TOKEN'] = userdata.get('NGROK_API_KEY')

```

If running locally, set them manually in your terminal or `.env` file.

---

## 🧹 Project Structure

```
.
├── app.py               # Streamlit frontend app
├── rag_backend.py       # RAG backend logic
└── README.md            # Project documentation (this file)

```

---

## 📄 Backend Code (rag_backend.py)

The backend handles:

- PDF parsing with `pdfplumber`
- Splitting text into chunks
- Generating embeddings with Gemini
- Storing and querying embeddings using ChromaDB
- Building context and generating responses

> Tip: You can customize chunk_size, model, or even use different embedding models as per your use case.
> 

---

## 🎨 Streamlit App ([app.py](http://app.py/))

The Streamlit app:

- Lets you upload PDFs
- Processes the PDF and generates embeddings
- Takes user input questions
- Displays the AI-generated answers

Run locally:

```bash
streamlit run app.py --server.port=8989

```

---

## 🌍 Deploy via Ngrok (Colab)

In Colab, Ngrok is used to expose the Streamlit app:

```python
from pyngrok import ngrok

ngrok.set_auth_token(userdata.get('NGROK_API_KEY'))
ngrok_tunnel = ngrok.connect(8989)
print("Streamlit App:", ngrok_tunnel.public_url)

```

You’ll get a public URL like:

```
Streamlit App: <https://xxxx-xx-xx-xx.ngrok-free.app>

```

---

## 👍 Stop Running App

To kill the running Streamlit app:

```bash
ngrok.kill()
!ps -ef | grep streamlit
!sudo kill -9 <process_id>

```

---

> Note: Replace RAG-PDFReader with your actual GitHub repository name.
> 

---

## 🔄 Optional: Run Fully Locally (No Colab)

1. Clone the repository

```bash
git clone <https://github.com/your-username/your-repo.git>
cd your-repo

```

1. Set your environment variables manually or use a `.env` file:

```bash
export GOOGLE_API_KEY='your-google-api-key'
export NGROK_AUTH_TOKEN='your-ngrok-token'

```

1. Install the dependencies and run:

```bash
pip install -r requirements.txt
streamlit run app.py --server.port=8989

```

1. Expose your local app (optional):

```bash
ngrok http 8989

```

---

## 🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests to enhance it!

---

## 📨 Contact

Contact details in my Github Profile

For any questions or feedback, feel free to reach out!

---

## 📜 License

This project is licensed under the MIT License.

---
