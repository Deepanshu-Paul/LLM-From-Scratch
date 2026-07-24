# Lab 01 - Character Tokenizer

## Objective

Build a Character Level Tokenizer from scratch to understand how raw text is converted into numerical IDs before entering an LLM.

---

# What is a Tokenizer?

A tokenizer converts human-readable text into machine-readable integer IDs.

Pipeline:

Text
↓
Tokens
↓
Vocabulary
↓
Integer IDs

---

# Character Tokenization

Example:

Input:

Hello

Tokens:

H
e
l
l
o

Each character becomes one token.

---

# Components of a CharacterTokenizer

## Vocabulary

Maps characters to integer IDs.

Example

{
    "<UNK>": 0,
    "H": 1,
    "e": 2,
    "l": 3,
    "o": 4
}

---

## Reverse Vocabulary

Maps IDs back to characters.

{
    0: "<UNK>",
    1: "H",
    2: "e",
    3: "l",
    4: "o"
}

---

# Methods

## fit(text)

Purpose:

Learn the vocabulary.

Algorithm

1. Remove duplicate characters
2. Sort them
3. Add <UNK> at index 0
4. Build:
   - char_to_id
   - id_to_char

---

## encode(text)

Purpose:

Convert text into integer IDs.

Algorithm

For each character

↓

Lookup ID

↓

If not found

↓

Return ID of <UNK>

Example

hello

↓

[2,1,3,3,4]

---

## decode(ids)

Purpose

Convert IDs back into text.

Algorithm

For each ID

↓

Lookup character

↓

Join characters

Example

[2,1,3,3,4]

↓

hello

---

# Unknown Token

Special Token

<UNK>

Purpose

Represents characters not present in the vocabulary.

Without it:

Unknown character

↓

KeyError

With it:

Unknown character

↓

ID = 0

---

# Python Concepts Learned

- Classes
- Object state
- Type hints
- Dictionary comprehensions
- Generator expressions
- enumerate()
- set()
- sorted()
- dict.get()
- join()

---

# Time Complexity

fit()

O(n log n)

(set + sorting)

encode()

O(n)

decode()

O(n)

---

# Design Decisions

Use a class instead of standalone functions.

Use:

char_to_id

and

id_to_char

instead of searching dictionaries repeatedly.

Use

dict.get()

instead of raising KeyError.

Store

UNK_TOKEN

as a class constant.

---

# Advantages

Simple

Easy to understand

Small vocabulary

Good for learning

---

# Limitations

Very long sequences.

Example

"Transformer"

↓

11 tokens

instead of one meaningful word.

Model must learn words from individual characters.

Not used in modern LLMs.

---

# Key Takeaways

✔ First stage of every LLM

✔ Text → IDs

✔ Vocabulary is learned

✔ Unknown tokens require special handling

✔ Tokenization happens before embeddings

# Why wasn't Character Tokenization enough?

Although character tokenization is simple and can represent any word, it has several major limitations.

## 1. Very Long Input Sequences

Example

Transformer

Character Tokens

T r a n s f o r m e r

↓

11 tokens

Longer sequences mean:

- More computation
- More memory
- Slower training
- Harder for the model to learn long-range relationships

---

## 2. Characters Carry Little Meaning

The character

"a"

does not have semantic meaning.

The model has to learn that

m + a + c + h + i + n + e

↓

machine

This makes learning language much harder.

---

## 3. Context Requires Many Tokens

To understand

"machine"

the model must process seven characters.

A WordTokenizer would need only one token.

---

## 4. Inefficient Learning

Instead of learning

machine

the model first has to learn

m

↓

ma

↓

mac

↓

mach

↓

...

↓

machine

This requires significantly more training.

---

# Why did researchers move beyond Character Tokenization?

Researchers wanted:

✓ Shorter sequences

✓ More meaningful tokens

↓

Word Tokenization