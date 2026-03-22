from app.rag.rag_chain import ask_rag


def test_rag_chain():
    """
    Test the RAG chain using the existing vector store.
    """

    question = "What skills are required?"

    result = ask_rag(
        question=question,
        persist_directory="chroma_db",
        collection_name="job_description_collection",
        k=3,
    )

    assert result is not None
    assert isinstance(result, dict)

    assert "question" in result
    assert "answer" in result
    assert "context" in result
    assert "documents" in result

    assert result["question"] == question
    assert result["answer"] is not None
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 0

    assert result["context"] is not None
    assert isinstance(result["context"], str)
    assert len(result["context"]) > 0

    assert result["documents"] is not None
    assert isinstance(result["documents"], list)
    assert len(result["documents"]) > 0

    print("\nQuestion:", result["question"])
    print("\nAnswer:\n")
    print(result["answer"])

    print("\n--- Context used ---\n")
    print(result["context"][:1500])


if __name__ == "__main__":
    test_rag_chain()