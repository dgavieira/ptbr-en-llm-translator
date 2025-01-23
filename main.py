# main.py
import os

from dotenv import load_dotenv

from inference.translate import Translator


def main():
    # Load environment variables
    load_dotenv()
    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

    if not huggingface_token:
        raise ValueError("Hugging Face token is not set in the .env file.")

    model_name = "Helsinki-NLP/opus-mt-ROMANCE-en"
    translator = Translator(model_name=model_name, token=huggingface_token)

    # Example usage
    portuguese_sentence = "Olá, como você está hoje?"
    english_translation = translator.translate(portuguese_sentence)

    print("Portuguese:", portuguese_sentence)
    print("English:", english_translation)


if __name__ == "__main__":
    main()
