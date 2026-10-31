from pathlib import Path

# Read only the Mermaid architecture block from the README.
def load_architecture() -> str:
    readme_path = Path(__file__).with_name("README.md")
    readme = readme_path.read_text(encoding="utf-8")
    start = readme.index("```mermaid")
    end = readme.index("```", start + len("```mermaid"))
    return readme[start : end + 3]