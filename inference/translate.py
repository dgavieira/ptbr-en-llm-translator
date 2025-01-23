# translator/translate.py
from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self, model_name: str, token: str):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name, token=token)
        self.model = MarianMTModel.from_pretrained(model_name, token=token)

    def translate(self, sentence: str) -> str:
        """
        Translates a sentence from the source language to the target language.

        Args:
            sentence (str): The sentence to be translated.

        Returns:
            str: The translated sentence.
        """
        inputs = self.tokenizer(sentence, return_tensors="pt", truncation=True)
        translated = self.model.generate(**inputs)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)
