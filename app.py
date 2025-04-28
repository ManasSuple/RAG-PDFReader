# import streamlit as st
# from rag_backend import *
# import os

# st.set_page_config(page_title="RAG PDF Reader", page_icon="📄")
# st.title("📄 Chat with Your PDF")

# pdf = st.file_uploader("Upload a PDF", type="pdf")

# if pdf:
#     with open(f"./{pdf.name}", "wb") as f:
#         f.write(pdf.read())

#     pdf_path = f"./{pdf.name}"
#     text = parse_pdf(pdf_path)
#     chunks = create_document_chunks(text)
#     embedding_model, chunks = embed_documents(chunks)
#     vectorstore = store_embeddings(embedding_model, chunks)

#     query = st.text_input("Ask a question about the document:")
#     if query:
#         relevant_chunks = retrieve_relevant_chunks(vectorstore, query)
#         context = get_context_from_chunks(relevant_chunks)
#         prompt = build_prompt(context, query)
#         response = generate_response(prompt)
#         st.markdown("### 📢 Answer")
#         st.write(response)

import streamlit as st
from rag_backend import *
import os

st.set_page_config(page_title="RAG PDF Reader", page_icon="📄")
st.title("📄 Chat with Your PDF")

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    with st.spinner('📚 Reading and processing your PDF... Please wait!'):
        with open(f"./{pdf.name}", "wb") as f:
            f.write(pdf.read())

        pdf_path = f"./{pdf.name}"
        text = parse_pdf(pdf_path)
        chunks = create_document_chunks(text)
        embedding_model, chunks = embed_documents(chunks)
        vectorstore = store_embeddings(embedding_model, chunks)

    st.success('✅ PDF loaded and ready! Ask your question below.')

    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner('🤔 Thinking... Fetching the answer...'):
            relevant_chunks = retrieve_relevant_chunks(vectorstore, query)
            context = get_context_from_chunks(relevant_chunks)
            prompt = build_prompt(context, query)
            response = generate_response(prompt)
        
        st.markdown("### 📢 Answer")
        st.write(response)

