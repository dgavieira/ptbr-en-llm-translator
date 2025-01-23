# Translate PT to EN

## Description

This repository provides a Python-based solution for translating sentences from Brazilian Portuguese to English using the Hugging Face `transformers` library and the `Helsinki-NLP/opus-mt-ROMANCE-en` model. The project leverages object-oriented programming principles and includes modularized code for better readability and maintainability.

### Features
- Utilizes the Hugging Face `transformers` library for translation.
- Supports authentication with Hugging Face API tokens.
- Modular design with a dedicated `translator` package.
- Easily configurable via `.env` file.

## Installation

### Prerequisites
- Python 3.8 or higher
- A Hugging Face account with an API token.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/translate-pt-to-en.git
   cd translate-pt-to-en
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Hugging Face API token:
   ```env
   HUGGINGFACE_TOKEN=your_hugging_face_token
   ```

## Usage

### Running the Translator

To translate a sentence from Brazilian Portuguese to English:

1. Open the `main.py` file and modify the `portuguese_sentence` variable with your desired input.
2. Run the script:
   ```bash
   python main.py
   ```

### Example Output
```
Portuguese: Olá, como você está hoje?
English: Hello, how are you today?
```

## Project Structure

```
translator/
├── __init__.py  # Marks the directory as a Python package
├── translate.py  # Contains the Translator class for handling translations
main.py  # Main script to run the translator
requirements.txt  # List of Python dependencies
.env.example  # Example environment file for storing Hugging Face token
```

## Requirements

- `transformers`
- `python-dotenv`
- `sacremoses` (optional but recommended for tokenizer support)

Install these dependencies via the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Contributing

Feel free to open issues or submit pull requests for enhancements or bug fixes. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Developed by Diego Vieira. Connect with me on [LinkedIn](https://www.linkedin.com/in/dgavieira/).
