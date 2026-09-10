import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR / ".env")


# API
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


# Models
WHISPER_MODEL_SIZE = os.getenv(
    "WHISPER_MODEL_SIZE",
    "base"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

CLAUDE_MODEL = os.getenv(
    "CLAUDE_MODEL",
    "claude-sonnet-4-6"
)


# Vector database
CHROMA_DIR = os.getenv(
    "CHROMA_DIR",
    "./chroma_db"
)


# Chunking
CHUNK_CHAR_SIZE = int(
    os.getenv("CHUNK_CHAR_SIZE", "900")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "150")
)


# Retrieval
TOP_K = int(
    os.getenv("TOP_K", "5")
)