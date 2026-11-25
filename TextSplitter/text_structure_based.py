from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Harshada, below are C-CAT-style MCQs covering all 18 topics you listed, with at least 3 questions per topic (54 questions total). These are practice questions modeled on common computer-fundamentals exam patterns, not verified questions from an actual CDAC paper.

The questions focus on definitions, comparisons, numerical conversions, application-based concepts, and common exam traps. Choose one correct answer for each question."""

spiltter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = spiltter.split_text(text)
print(len(chunks))
print(chunks)