# SHELF

**Shelf** is a reading-centered language learning platform that combines NLP, grammar discovery, and adaptive memory systems to help learners acquire language directly from texts.

Instead of studying isolated vocabulary lists, learners discover words, grammar patterns, verb forms, pronoun families, and constructions while reading.

## Built With

- React + TypeScript
- FastAPI + Python
- spaCy NLP
- OCR for import (pdf, png, jpg)
- CEFR difficulty estimation
- Adaptive review system

## Current Status

- Spanish support
- English support
- Reader-based vocabulary discovery
- Grammar collectibles
- Pronoun and verb families
- OCR import
- Adaptive review
- CEFR-based difficulty highlighting

---

## Core Idea

Shelf is built around three principles:

1. **Reading** — language is encountered in context.
2. **Discovery** — words and grammar patterns are detected automatically.
3. **Memory** — useful items are stored, reviewed, and tracked over time.

Unknown words, grammar patterns, pronouns, verb forms, and difficulty levels are detected directly from texts.

<img width="1000" height="800" alt="Shelf dictionary view" src="https://github.com/user-attachments/assets/ffa548cc-daa7-42db-a192-2457171623c1" />

<img width="1000" height="800" alt="image" src="https://github.com/user-attachments/assets/62c3f455-c4b6-428f-bd01-e33c68d8c30a" />

---

## Discover Instead of Memorize

Shelf lets learners collect:

- Vocabulary
- Verb families
- Pronoun families
- Grammar rules
- Noun patterns
- Adjective patterns

This makes grammar part of the reading workflow instead of a separate memorization task.

<img width="900" height="750" alt="Shelf grammar view" src="https://github.com/user-attachments/assets/6e3de707-84a0-4e25-8ee1-b0391d1bbd8d" />

---

## Grammar Through Usage

Grammar rules are linked to real examples from texts.

Examples:

- `a / an` → Articles
- `who / whom / whose` → Question words
- `can / could` → Modal verbs
- `with / without` → Prepositions

The goal is to make grammar visible through repeated exposure and usage.

<img width="900" height="750" alt="Shelf shelves view" src="https://github.com/user-attachments/assets/4ff6ffe3-806e-4885-8daf-54928f22d8e3" />

---

## Personal Difficulty Ratings

Shelf uses personal difficulty ratings instead of treating every word as equally hard.

Difficulty combines:

- User rating
- Exposure frequency
- Review history
- Time decay

This creates a more flexible review system than simple flashcard repetition.

---

## Theoretical Inspiration

Shelf is inspired by ideas from cognitive science, language acquisition research, and memory research.

### Usage-Based Language Learning

--> Language is acquired through repeated exposure to meaningful examples rather than isolated memorization.

### Comprehensible Input

--> Learners benefit from exposure to language that is understandable but slightly challenging.

### Retrieval Practice

--> Memory improves when information is actively recalled rather than only reread.

### Spaced Repetition

--> Repeated exposure over time improves long-term retention.

### Lexical Chunking

--> Language is often learned through reusable phrases, patterns, and constructions rather than isolated words.


Shelf does not attempt to implement any single theory directly. Instead, it combines ideas from language learning, memory research, and NLP into a practical reading-based workflow.

---

## Architecture

```text
Text
 ↓
NLP Processing
 ↓
Token Analysis
 ↓
Dictionary Entries
 ↓
Grammar Detection
 ↓
Collectibles
 ↓
Adaptive Review
