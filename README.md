# magic-8-ball-bot---Using-RASA-framework

# 🎱 Magic 8-Ball Chatbot (Rasa Framework)

##  Project Overview

The **Magic 8-Ball Chatbot** is a simple conversational AI built using the **Rasa framework**. It mimics the behavior of a traditional Magic 8-Ball toy by responding to user questions with predefined, randomized answers such as *Yes*, *No*, *Maybe*, or *Ask again later*.

This project was developed **as part of an academic requirement** to understand the fundamentals of chatbot development, Natural Language Understanding (NLU), and dialogue management using Rasa.

---

## Objectives

* To learn the basics of chatbot development using **Rasa**
* To understand **intents, stories, rules, and actions**
* To build a simple question–answer based conversational bot
* To gain hands-on experience with **NLU training data** and **dialogue flow**

---

## Technologies Used

* **Python**
* **Rasa Framework**
* **YAML** (for training data and configuration files)
* **HTML** (basic frontend for interaction)

---

## Project Structure

```
magic-8ball-bot/
├── data/
│   ├── nlu.yml          # Intents and example user messages
│   ├── stories.yml      # Conversation flows
│   └── rules.yml        # Rule-based responses
├── actions/
│   ├── __init__.py
│   └── actions.py       # Custom actions (random 8-ball responses)
├── config.yml           # NLU pipeline and policies
├── domain.yml           # Intents, responses, actions
├── endpoints.yml        # Action server configuration
├── index.html           # Simple UI for chatbot
└── README.md            # Project documentation
```

---

## How the Bot Works

1. The user asks a **yes/no type question**
2. Rasa NLU identifies the intent
3. The dialogue manager selects the appropriate action
4. The bot responds with a **random Magic 8-Ball style answer**

---

## Intents Used

* `greet` – Greeting messages
* `ask_question` – User asks a question
* `goodbye` – Ending the conversation

---

## How to Run the Project

### 1️.Install Rasa

```bash
pip install rasa
```

### 2️.Train the Model

```bash
rasa train
```

### 3️.Run the Action Server

```bash
rasa run actions
```

### 4️.Start the Bot

```bash
rasa shell
```

---

## Academic Relevance

This project fulfills academic requirements by demonstrating:

* Understanding of conversational AI concepts
* Practical usage of the Rasa framework
* Implementation of rule-based and intent-driven conversations


