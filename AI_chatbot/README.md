# SupportBot: AI Mental Health Support Chatbot

**SupportBot** is an AI-powered chatbot designed to provide accessible, empathetic, and judgment-free mental health support. Using the **LangChain** framework and **Ollama** for language generation, it helps users take the first step toward addressing mental health challenges while adhering to strict guidelines to ensure safety and appropriateness.

---

## Problem Statement

Millions of people worldwide face mental health challenges but lack consistent access to mental health professionals. Traditional therapy can be expensive, and waiting for help can worsen distress. **TherapistBot** provides immediate, anonymous support to individuals seeking guidance, helping bridge the gap between those in need and professional care.

---

## Solution Overview

**TherapistBot** offers AI-driven mental health support through conversational guidance. The chatbot uses:

- **LangChain** for processing and managing user queries.
- **Ollama** for generating empathetic and helpful responses.
- A **tips and guidelines file** (.txt or .doc) to ensure responses are safe, ethical, and in line with professional advice.

### Key Features

- **Mental health support**: Provides empathetic guidance on emotional well-being and coping strategies.
- **Guideline-based filtering**: Detects and politely refuses harmful or inappropriate queries based on predefined ethical rules.
- **Mood tracking**: Logs and visualizes user mood over a 10-day period using SQLite and Streamlit.
- **Open-source**: Fully open-source to encourage community-driven improvements.

---

## Tech Stack

- **Frontend**: Streamlit – For building the interactive UI and visualizing mood data.
- **Backend**: LangChain – For handling query processing and AI integration.
- **Language Model**: Ollama – Generates empathetic and relevant responses.
- **Data Source**: SQLite3 – Tracks user mood over time, and a **text or .doc file** containing ethical guidelines and therapist tips.

---

## Features & How It Works

### User Flow

- **User Interaction**: Users input questions or concerns related to mental health.
- **Guideline Check**: The system verifies queries against the guidelines file to ensure safety and relevance.
- **Response Generation**: Ollama generates a helpful and empathetic response based on the user input.
- **Query Rejection**: If a query is harmful or inappropriate, the bot politely refuses to answer and explains why.
- **Mood Visualization**: Users can track mood trends over 10 days through the Streamlit dashboard.
