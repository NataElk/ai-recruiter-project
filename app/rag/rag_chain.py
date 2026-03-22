from app.utils.llm_factory import get_llm
from app.rag.retriever import get_retriever


def ask_rag(question: str,
            persist_directory: str = "chroma_db",
            collection_name: str = "job_description_collection",
            k: int = 3):
    """
    Retrieve relevant chunks from Chroma and ask the LLM
    to answer based only on that context.
    """

    retriever = get_retriever(
        persist_directory=persist_directory,
        collection_name=collection_name,
        k=k,
    )

    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful AI recruiter assistant.

Answer the question based only on the context below.
If the answer is not in the context, say:
"I could not find the answer in the provided job description."

Context:
{context}

Question:
{question}
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return {
        "question": question,
        "answer": response.content,
        "context": context,
        "documents": docs,
    }