from pathlib import Path
import re
import sys

# Read the container aliases from the architecture contract.
diagram = Path("README.md").read_text(encoding="utf-8")
aliases = re.findall(r"^\s*Container\(([^,]+),", diagram, re.MULTILINE)

# Map each internal alias to the Python module it names.
missing = [f"{alias}.py" for alias in aliases if not Path(f"{alias}.py").exists()]

if missing:
    print("Architecture drift detected.")
    print(f"Missing modules: {', '.join(missing)}")
    sys.exit(1)

print("Architecture matches the diagram.")