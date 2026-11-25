from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="dl-curriculum.pdf")

docs = loader.load()
# text = """Harshada, below are C-CAT-style MCQs covering all 18 topics you listed, with at least 3 questions per topic (54 questions total). These are practice questions modeled on common computer-fundamentals exam patterns, not verified questions from an actual CDAC paper.

# The questions focus on definitions, comparisons, numerical conversions, application-based concepts, and common exam traps. Choose one correct answer for each question."""

splitter = CharacterTextSplitter(
    chunk_size= 200,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs)
print(result[0])