import os
from fastapi import FastAPI, Request
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.document_loaders import CSVLoader, JSONLoader
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(groq_api_key=groq_api_key,
               model_name="Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
    Responda las preguntas basándose en el contexto proporcionado.
    Proporcione la respuesta más precisa según la pregunta.
    <contexto>
    {context}
    </contexto>
    Preguntas: {input}
    """
)

@app.on_event("startup")
async def startup_event():
    embeddings = OllamaEmbeddings()

    pdf_loader = PyPDFDirectoryLoader("./ruta/al/directorio/pdf")
    pdf_docs = pdf_loader.load()

    csv_loader = CSVLoader("./ruta/al/archivo.csv")
    csv_docs = csv_loader.load()

    json_loader = JSONLoader("./ruta/al/archivo.json")
    json_docs = json_loader.load()

    docs = pdf_docs + csv_docs + json_docs

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    vectors = FAISS.from_documents(final_documents, embeddings)

    app.state.vectors = vectors

@app.post("/ask")
async def ask_question(request: Request):
    prompt1 = await request.json()
    prompt1 = prompt1["question"]

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = app.state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({'input': prompt1})

    return {"respuesta": response['respuesta'], "contexto": response["contexto"]}
