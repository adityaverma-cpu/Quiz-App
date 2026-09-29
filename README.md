# Quiz Application

This is a simple quiz app made with Python Tkinter. You select a category and difficulty and answer 10 questions. At the end you can see your score.

## Features

- 40 questions
- 4 categories: General Knowledge, Python, Science, Mathematics
- Easy and Medium difficulty (Hard will be added later)
- 10 random questions, 4 options for each
- 15 seconds timer for each question
- Previous and Next buttons
- Shows score, percentage, correct, wrong and unanswered questions
- Try Again and Exit buttons
- Questions are stored in a JSON file
- Unit tests included

## Requirements

- Python 3.9 or above
- Tkinter

## How to Run

```bash
python quiz_application.py
```

On Windows you can also use:

```bash
py quiz_application.py
```

## How to Use

1. Choose category and difficulty (or All).
2. Click START QUIZ.
3. Select an answer for each question.
4. Use Next and Previous to move between questions.
5. Submit to see your score.

## Files

```text
Quiz Application/
├── quiz_application.py
├── README.md
├── statement.md
├── RUN_PROJECT.txt
├── requirements.txt
├── .gitignore
├── data/
│   └── questions.json
├── docs/
│   ├── PROJECT_REPORT.md
│   └── ALGORITHM_AND_FLOW.md
└── tests/
    ├── __init__.py
    └── test_quiz_application.py
```
