# Lab 02 - Word Tokenizer

## Objective

Build a Word Level Tokenizer and understand why character tokenization is insufficient for language modeling.

---

# Word Tokenization

Instead of characters

Hello World

↓

Hello
World

Each word becomes one token.

---

# Pipeline

Text

↓

Split into words

↓

Vocabulary

↓

Integer IDs

---

# Components

Vocabulary

word_to_id

Reverse Vocabulary

id_to_word

Unknown Token

<UNK>

---

# tokenize(text)

Purpose

Split raw text into words.

Current implementation

text.split()

Example

"I love AI"

↓

["I", "love", "AI"]

---

# fit(text)

Algorithm

1. Tokenize text
2. Remove duplicates
3. Sort vocabulary
4. Add <UNK>
5. Build mappings

---

# encode(text)

Algorithm

Text

↓

Tokenize

↓

Lookup IDs

↓

Unknown words

↓

<UNK>

---

# decode(ids)

Algorithm

IDs

↓

Lookup words

↓

Join using spaces

Example

[2,3,1]

↓

"I love AI"

---

# Unknown Words

Training

I love AI

Inference

I love Generative AI

↓

Generative

↓

<UNK>

Output

[2,3,0,1]

---

# Python Concepts

Reuse existing architecture.

Separate tokenization into its own method.

Single Responsibility Principle.

---

# Why tokenize() is a separate method?

Instead of

fit()

↓

split()

and

encode()

↓

split()

Create

tokenize()

Now

fit()

and

encode()

reuse it.

Future improvements only modify one function.

---

# Advantages

Meaningful tokens.

Much shorter sequences.

Model learns semantic words directly.

---

# Limitations
# Why wasn't Word Tokenization enough?

Word tokenization solves many problems of CharacterTokenizer, but introduces new ones.

---

## 1. Huge Vocabulary

Every unique word becomes a token.

Example

run

running

runner

runs

ran

All become different entries.

Vocabulary grows into millions of words.

Large vocabularies require:

- More memory
- Larger embedding matrices
- More computation

---

## 2. Unknown Words (OOV - Out Of Vocabulary)

Training Vocabulary

I
love
AI

Inference

I love Generative AI

↓

Generative

↓

<UNK>

The model completely loses information.

---

## 3. No Understanding of Word Structure

Example

unbelievable

Word Tokenizer

↓

<UNK>

The tokenizer does not know that

un
believe
able

are meaningful pieces.

---

## 4. Poor Handling of Morphology

Words like

play

playing

played

player

are treated as completely unrelated.

The tokenizer cannot recognize they share the same root.

---

## 5. Punctuation Problems

Hello

Hello!

Hello?

Hello,

All become different tokens.

Vocabulary grows unnecessarily.

---

## 6. Multi-Language Problems

Languages like Chinese and Japanese do not separate words using spaces.

Whitespace tokenization fails completely.

---

## 7. Vocabulary Never Stops Growing

New words appear every day.

Examples

ChatGPT

DeepSeek

Llama

Gemma

The tokenizer would need retraining whenever new vocabulary appears.

---

# Why did researchers move beyond Word Tokenization?

Researchers wanted:

✓ Smaller vocabulary

✓ Better handling of unknown words

✓ Shorter sequences

✓ Ability to understand word structure

↓

Subword Tokenization

↓

Byte Pair Encoding (BPE)
---

# Character vs Word Tokenizer

Character

Pros

Small vocabulary

Handles unseen words

Cons

Very long sequences

Poor semantic meaning

---

Word

Pros

Short sequences

Meaningful tokens

Cons

Huge vocabulary

Many unknown words

Poor handling of punctuation

---

# Historical Insight

Character Tokenizer

↓

Too many tokens

Word Tokenizer

↓

Too many unknown words

Need something in between

↓

Subword Tokenization

↓

Byte Pair Encoding (BPE)

---

# Key Takeaways

✔ Word is the token.

✔ tokenize() converts text into words.

✔ Architecture is almost identical to CharacterTokenizer.

✔ Only the definition of "token" changes.

✔ Word tokenizers still have major limitations.

✔ These limitations motivated BPE.
