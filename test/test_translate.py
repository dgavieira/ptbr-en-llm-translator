import os

import pytest
from dotenv import load_dotenv

from inference.translate import Translator

# Load environment variables
load_dotenv()
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")


@pytest.fixture
def translator():
    if not HUGGINGFACE_TOKEN:
        pytest.fail("Hugging Face token is not set in the .env file.")

    model_name = "Helsinki-NLP/opus-mt-ROMANCE-en"
    return Translator(model_name=model_name, token=HUGGINGFACE_TOKEN)


def test_translate_simple_sentence(translator):
    portuguese_sentence = "Olá, como você está hoje?"
    possible_outputs = ["Hello, how are you today?", "Hi, how are you today?"]

    result = translator.translate(portuguese_sentence)

    assert isinstance(result, str), "Translation result should be a string."
    assert any(result.lower() == output.lower() for output in possible_outputs), \
        f"Expected one of {possible_outputs}, but got '{result}'."


def test_translate_empty_string(translator):
    portuguese_sentence = ""
    expected_english = ""  # Adjust to match the translator's updated behavior

    result = translator.translate(portuguese_sentence)

    assert isinstance(result, str), "Translation result should be a string."
    assert result == expected_english, f"Expected '{expected_english}', but got '{result}'."


def test_translate_special_characters(translator):
    portuguese_sentence = "!@#$%^&*()"
    expected_english = "!@#$%^&*()"

    result = translator.translate(portuguese_sentence)

    assert isinstance(result, str), "Translation result should be a string."
    # Strip spaces if the tokenizer adds them unnecessarily
    assert result.replace(" ", "") == expected_english, \
        f"Expected '{expected_english}', but got '{result}'."


def test_translate_long_sentence(translator):
    portuguese_sentence = (
        "Este é um exemplo de uma frase longa que contém muitas palavras para testar o desempenho do tradutor em sentenças extensas."
    )
    result = translator.translate(portuguese_sentence)

    assert isinstance(result, str), "Translation result should be a string."
    assert len(result) > 0, "Translation result should not be empty for a long sentence."


def test_translate_non_portuguese_text(translator):
    non_portuguese_sentence = "This is a test in English."
    result = translator.translate(non_portuguese_sentence)

    assert isinstance(result, str), "Translation result should be a string."
    assert result == non_portuguese_sentence, f"Expected '{non_portuguese_sentence}', but got '{result}'."
