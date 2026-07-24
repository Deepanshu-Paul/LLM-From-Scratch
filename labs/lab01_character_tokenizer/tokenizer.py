class CharacterTokenizer:
    """
    A simple character-level tokenizer.

    This tokenizer learns a vocabulary of unique characters
    and provides methods to encode text into integer IDs
    and decode IDs back into text.
    """
    UNK_TOKEN = "<UNK>"

    def __init__(self):
        self.char_to_id: dict[str, int] = {}
        self.id_to_char: dict[int, str] = {}

    def fit(self, text:str):
        """
        Learn the vocabulary from the given text.

        Args:
            text (str): The input text to learn the vocabulary from.
        """
        unique_chars = [self.UNK_TOKEN] + sorted(set(text))
        self.char_to_id = {ch: i for i, ch in enumerate(unique_chars)}
        self.id_to_char = {i: ch for i, ch in enumerate(unique_chars)}

    def encode(self, text:str) -> list[int]:
        """
        Encode the given text into a list of integer IDs.

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of integer IDs corresponding to the characters.
        """
        return [self.char_to_id.get(ch, self.char_to_id[self.UNK_TOKEN]) for ch in text]
    #[self.char_to_id[ch] for ch in text]
    
    def decode(self, ids:list[int]) -> str:
        """
        Decode a list of integer IDs back into text.

        Args:
            ids (list[int]): A list of integer IDs to decode.

        Returns:
            str: The decoded text.
        """
        return ''.join(self.id_to_char.get(i, self.UNK_TOKEN) for i in ids)
