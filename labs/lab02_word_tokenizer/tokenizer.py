class WordTokenizer:

    """
    A simple word-level tokenizer.

    This tokenizer learns a vocabulary of unique words
    and provides methods to encode text into integer IDs
    and decode IDs back into text.
    """

    UNK_TOKEN = "<UNK>"

    def __init__(self):
        self.word_to_id: dict[str, int] = {}
        self.id_to_word: dict[int, str] = {}

    def tokenize(self, text):
        """
        Split the input text into words based on whitespace.
        """
        return text.split()

    def fit(self, text:str):
        """
        Learn the vocabulary from the given text.

        Args:
            text (str): The input text to learn the vocabulary from.
        """
        words = self.tokenize(text)
        unique_words = [self.UNK_TOKEN] + sorted(set(words))
        self.word_to_id = {word: i for i, word in enumerate(unique_words)}
        self.id_to_word = {i: word for i, word in enumerate(unique_words)}

    def encode(self, text:str) -> list[int]:
        """
        Encode the given text into a list of integer IDs.

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of integer IDs corresponding to the words.
        """
        words = self.tokenize(text)
        return [self.word_to_id.get(word, self.word_to_id[self.UNK_TOKEN]) for word in words]

    def decode(self, ids:list[int]) -> str:
        """
        Decode a list of integer IDs back into text.

        Args:
            ids (list[int]): A list of integer IDs to decode.

        Returns:
            str: The decoded text.
        """
        return ' '.join(self.id_to_word.get(i, self.UNK_TOKEN) for i in ids)
    