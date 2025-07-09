import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from langchain_core.runnables import RunnablePassthrough


# Configure Google Gemini
model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    )
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)
    
def create_retriever(pdf_path):
    loader = PyPDFLoader(pdf_path)  # Replace with your document path
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db")
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    return retriever


def predict(retriever, query):
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="""You are a Helpful AI Bot.
                    Given a context and question from user,
                    you should answer based on the given context."""),
        HumanMessagePromptTemplate.from_template("""Answer the question based on the given context.
        Context: {context}
        Question: {question}
        Answer: """)
    ])
    chain = ({
        "context": retriever,
        "question": RunnablePassthrough()
    } | prompt_template | model)

    return chain.invoke(query).content