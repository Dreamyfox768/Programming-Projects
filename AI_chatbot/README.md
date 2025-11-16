# TherapistBot: AI Mental Health Support Chatbot

**SupportBot** is an AI-powered chatbot designed to provide accessible, empathetic, and ethical mental health advice. Using the **Langchain** framework and **Ollama** for language generation, it answers common mental health-related questions while adhering to strict guidelines to ensure safety and appropriateness.

---

## Problem Statement

Millions of people worldwide face mental health challenges but lack consistent access to mental health professionals. Traditional therapy can be expensive, and waiting for professional help can cause further distress. **TherapistBot** offers immediate, anonymous support to individuals seeking advice on mental well-being, helping to bridge the gap between people and therapists.

---

## Solution Overview

**TherapistBot** provides mental health advice using conversational AI. The chatbot utilizes:

- **Langchain** for handling and processing user queries.
- **Ollama** for generating relevant responses to user inputs.
- A **tips and guidelines file** (.txt or .doc) to help the bot respond based on ethical guidelines, ensuring safety and avoiding harmful queries.

### Key Features

- **Mental health support**: Provides empathetic and relevant advice on various mental health topics.
- **Guideline-based filtering**: Filters out harmful or malicious queries and refuses them politely based on predefined rules.
- **Open-source**: The project is fully open-source, allowing for community-driven improvements.

---

## Tech Stack

- **Frontend**: [Streamlit] – For building the interactive user interface.
- **Backend**: [Langchain] – For handling query processing and data retrieval.
- **Language Model**: [Ollama] – A language model for generating empathetic responses.
- **Data Source**: [SQLite3] and A **text or .doc file** containing therapist tips, tricks, and ethical guidelines for safe conversation.

---

## Features & How It Works

### User Flow

1. **User Interaction**: The user enters a question or a query related to mental health.
2. **Guideline Check**: The system checks the query against a pre-built knowledge base (the .txt/.doc file) containing therapist guidelines and advice.
3. **Response Generation**: The chatbot generates an answer using the **Ollama** language model, ensuring that the response is helpful and empathetic.
4. **Query Rejection**: If the query is deemed out-of-scope (e.g., harmful or inappropriate), the chatbot politely refuses to answer, explaining the reason.



