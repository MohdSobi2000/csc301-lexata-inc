import os
import sys
from pathlib import Path
PROJECT_PATH = Path(os.getcwd()).parent
print(PROJECT_PATH)
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "application", "backend"
)
sys.path.append(SOURCE_PATH)