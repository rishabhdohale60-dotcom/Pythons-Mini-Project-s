
import transformers
import nltk
import pandas as pd
import streamlit as st

print("All libraries installed successfully!")


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

text = "Artificial Intelligence is the simulation of human intelligence processes by machines."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)


# AI Notes Summarize + Quiz Generator (Starter Code)

from transformers import pipeline
import random

# 1. Summarizer model (HuggingFace)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example notes text
notes = """
Artificial Intelligence is the simulation of human intelligence processes by machines.
It includes learning, reasoning, and self-correction.
Machine Learning is a subset of AI that focuses on data-driven learning.
Types of ML include supervised, unsupervised, and reinforcement learning.
Applications include spam filtering, recommendation systems, and image recognition.
"""

# 2. Generate summary
summary = summarizer(notes, max_length=60, min_length=30, do_sample=False)
print("📘 Summary:\n", summary[0]['summary_text'])

# 3. Simple Quiz Generator
quiz_questions = [
    ("Which subset of AI focuses on data-driven learning?", "Machine Learning"),
    ("Name two applications of Machine Learning.", "Spam filtering, Recommendation systems"),
    ("True/False: Reinforcement learning is based on rewards and penalties.", "True"),
]

print("\n🎯 Quiz:")
for i, (q, a) in enumerate(quiz_questions, 1):
    print(f"{i}. {q}")

# 4. Random MCQ Example
options = ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Machine Learning"]
question = "Which type of ML uses labeled data?"
answer = "Supervised Learning"

print(f"\nMCQ: {question}")
print("Options:", options)
print("Correct Answer:", answer)


# Simple Quiz Example

question = "Which type of ML uses labeled data?"
options = ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Machine Learning"]
answer = "Supervised Learning"

print("Q:", question)
print("Options:", options)

user_input = input("Your Answer: ")

if user_input.strip() == answer:
    print("✅ Correct!")
else:
    print("❌ Wrong! Correct Answer is:", answer)

user_input = input("Your Answer: ")

if user_input.strip().lower() == answer.lower():
    print("✅ Correct!")
else:
    print("❌ Wrong! Correct Answer is:", answer)

import difflib

answer = "Supervised Learning"
user_input = input("Your Answer: ")

# Case-insensitive + spelling tolerance
similarity = difflib.SequenceMatcher(None, user_input.lower(), answer.lower()).ratio()

if similarity > 0.7:  # 70% match threshold
    print("✅ Correct! (Close enough)")
else:
    print("❌ Wrong! Correct Answer is:", answer)


import difflib

def ask_question(question, options, answer):
    print("Q:", question)
    print("Options:", options)
    user_input = input("Your Answer: ")

    # Case-insensitive + fuzzy matching
    similarity = difflib.SequenceMatcher(None, user_input.lower(), answer.lower()).ratio()

    if similarity > 0.7:  # 70% match threshold
        print("✅ Correct!\n")
        return True
    else:
        print("❌ Wrong! Correct Answer is:", answer, "\n")
        return False

# Example Quiz
questions = [
    ("Which type of ML uses labeled data?", 
     ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Machine Learning"], 
     "Supervised Learning"),
    
    ("True/False: Reinforcement learning is based on rewards and penalties.", 
     ["True", "False"], 
     "True"),
]

score = 0
for q, opts, ans in questions:
    if ask_question(q, opts, ans):
        score += 1

print("🎯 Final Score:", score, "/", len(questions))


import difflib

def check_answer(user_input, correct_answer):
    # Case-insensitive + fuzzy matching
    similarity = difflib.SequenceMatcher(None, user_input.lower(), correct_answer.lower()).ratio()
    if similarity > 0.75:  # 75% match threshold
        return True
    return False

# Example usage
question = "Which type of ML uses labeled data?"
options = ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Machine Learning"]
answer = "Supervised Learning"

print("Q:", question)
print("Options:", options)

user_input = input("Your Answer: ")

if check_answer(user_input, answer):
    print("✅ Correct!")
else:
    print("❌ Wrong! Correct Answer is:", answer)
