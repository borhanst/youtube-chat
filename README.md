# YouTube Video Chat Application

An interactive application that allows users to chat with YouTube video content using AI. The application transcribes YouTube videos and enables users to ask questions about the video content using a conversational interface.

## Features

- YouTube video transcript extraction with multi-language support
- Translation capabilities for video transcripts
- Interactive chat interface to ask questions about video content
- AI-powered responses using Google's Generative AI
- Vector database storage for efficient transcript searching
- Streamlit-based user interface

## Prerequisites

- Python 3.11+
- Google API credentials (for Generative AI)
- Internet connection for YouTube access
- uv package manager (for fast dependency management)

> Note: This project uses [uv](https://docs.astral.sh/uv/), a extremely fast Python package manager written in Rust that's 10-100x faster than pip for dependency management. It provides universal lockfile support and efficient caching.

## Installation

1. Install uv (Choose one method):
   ```bash
   # For macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Or install via pip
   pip install uv
   ```

2. Clone the repository

3. Create and activate virtual environment with uv:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix-like systems
   # or
   .venv\Scripts\activate     # On Windows
   ```

4. Install dependencies using uv (since project includes uv.lock):
   ```bash
   uv sync
   ```

5. Create a `.env` file with your Google API credentials

## Project Structure

- `main.py` - Main application file with Streamlit interface
- `embedding.py` - Handles vector embeddings and database operations
- `utils.py` - Utility functions for transcript extraction and LLM responses
- `country.json` - Language configuration file
- `chroma_db/` - Vector database storage directory

## Usage

1. Start the application:
```bash
uv run streamlit run main.py
```

2. Enter a YouTube URL in the sidebar
3. Select transcript language(s) and translation language
4. Submit to load the video and transcript
5. Use the chat interface to ask questions about the video content

## Technical Details

- Uses `langchain` for LLM operations
- Implements ChromaDB for vector storage
- Utilizes Google's Generative AI for embeddings and responses
- Supports multiple language transcripts through YouTube's API
- Implements efficient document chunking for better context management

## Environment Variables

Required environment variables:
- `GOOGLE_API_KEY` - Your Google API key for Generative AI access

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.