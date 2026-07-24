from tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer()

tokenizer.fit("hello")

encoded = tokenizer.encode("hello")
print(encoded)

decoded = tokenizer.decode(encoded)
print(decoded)