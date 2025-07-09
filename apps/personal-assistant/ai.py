from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

# Configure Google Gemini
model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    )

# def create_retriever(pdf_path):
#     loader = PyPDFLoader(pdf_path)  # Replace with your document path
#     documents = loader.load()
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     chunks = text_splitter.split_documents(documents)
#     db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db")
#     retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
#     return retriever


def predict(query):
    prompts = [
        SystemMessage(content="""You are a Helpful AI Bot."""),
        HumanMessage(content=query)
    ]

    return model.invoke(prompts).content