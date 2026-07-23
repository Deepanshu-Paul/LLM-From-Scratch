Today you learned several important concepts that go beyond tokenizers:

State vs Behavior
State → self.char_to_id, self.id_to_char
Behavior → fit(), encode(), decode()
Determinism
We use sorted(set(text)) so the same input always produces the same vocabulary.
Python built-ins
Strings are iterable.
set() removes duplicates.
sorted() ensures consistent ordering.
enumerate() gives both index and value.
Dictionary comprehensions create mappings concisely.
Object-Oriented Design
Temporary variables disappear after a method returns.
self stores information that the object needs to remember.