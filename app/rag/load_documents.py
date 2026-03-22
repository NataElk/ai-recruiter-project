from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_job_documents(file_path: str | None = None):
    """
    Load the job description PDF from the data folder.
    Returns a list of LangChain Document objects.
    """

    if file_path is None:
        project_root = Path(__file__).resolve().parents[2]
        file_path = project_root / "app" / "data" / "job_description.pdf"
    else:
        file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    loader = PyPDFLoader(str(file_path))
    documents = loader.load()

    return documents