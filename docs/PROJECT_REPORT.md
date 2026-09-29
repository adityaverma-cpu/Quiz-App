# Quiz Application Using Python Tkinter
## Project Report

### 1. Project Title
**Quiz Application Using Python Tkinter**

### 2. Abstract
Quiz Application is a beginner-friendly desktop quiz system developed in Python using the Tkinter graphical user interface toolkit. The application presents multiple-choice questions from a JSON question bank and allows the user to select a category and difficulty before starting a quiz.

The current question bank contains 40 questions distributed across General Knowledge, Python, Science, and Mathematics. A quiz randomly selects 10 questions from the questions that match the chosen filters. Each question provides four choices and a 15-second timer. The timer automatically advances the quiz when time expires.

The application stores questions separately in JSON, validates the question-bank structure before use, supports Previous and Next navigation, calculates the final score and percentage, and reports correct, wrong, and unanswered questions. The project also includes automated unit tests for question loading, filtering, scoring, and invalid-data handling.

### 3. Introduction
The purpose of the project is to provide a simple interactive quiz environment that demonstrates practical Python programming concepts through a graphical desktop application.

Instead of presenting quiz questions only through a command-line interface, the project uses Tkinter widgets such as labels, buttons, option menus, radio buttons, frames, and message boxes. This makes the application suitable for demonstrating event-driven programming and basic GUI design.

### 4. Problem Statement
A basic quiz system needs to manage a question bank, present questions clearly, accept answers, enforce a time limit, calculate results, and handle invalid or incomplete question data.

The project solves this problem by separating the question data into a JSON file and implementing reusable functions for loading, validating, filtering, and scoring questions. The Tkinter application manages the interactive quiz workflow.

### 5. Objectives
1. Develop a desktop quiz application using Python.
2. Create a user-friendly Tkinter graphical interface.
3. Maintain a separate JSON question bank.
4. Provide category and difficulty filtering.
5. Randomly select 10 questions for each quiz.
6. Provide four multiple-choice options for every question.
7. Give the user 15 seconds per question.
8. Automatically advance when the timer reaches zero.
9. Support Previous and Next navigation.
10. Calculate score and percentage.
11. Display correct, wrong, and unanswered statistics.
12. Validate question-bank data before use.
13. Handle insufficient questions for selected filters.
14. Provide automated unit tests for important core functions.
15. Keep the implementation dependent only on Python's standard library.

### 6. Scope
The implemented scope includes:
- Graphical quiz interface
- 40-question JSON question bank
- Four categories
- Easy and Medium questions in the current data
- Category filtering
- Difficulty filtering
- Random selection of 10 questions
- Four choices per question
- 15-second timer
- Automatic timer-based advancement
- Previous and Next navigation
- Quiz submission
- Score calculation
- Percentage calculation
- Correct/wrong/unanswered statistics
- Try Again and Exit controls
- JSON validation
- Unit testing
- Documentation

The project does not currently implement online accounts, cloud storage, multiplayer functionality, a database, a web server, or a network-based leaderboard.

### 7. Target Users
The application is suitable for:
- Students learning Python
- Beginners learning Tkinter
- Users who want a small desktop quiz application
- Learners practicing multiple-choice questions
- Students demonstrating event-driven GUI programming

### 8. Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application programming |
| Tkinter | Desktop graphical user interface |
| JSON | Question-bank storage |
| pathlib | File-path handling |
| random | Random question selection |
| unittest | Automated testing |
| Standard Library | Core implementation |

No third-party Python packages are required.

### 9. Project Structure
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

### 10. Functional Requirements
The application provides the following major functional requirements:

**FR1 — Question Loading:** Load questions from the JSON question bank.

**FR2 — Validation:** Verify that the question bank is a non-empty list and that each question contains the required fields, exactly four options, and an answer that belongs to the options.

**FR3 — Filtering:** Filter questions by category and difficulty.

**FR4 — Quiz Generation:** Randomly select 10 questions from the filtered question set.

**FR5 — Answer Selection:** Allow one answer to be selected for each question.

**FR6 — Timer:** Provide 15 seconds for each question and automatically advance when time expires.

**FR7 — Navigation:** Allow movement between questions using Previous and Next.

**FR8 — Submission:** Submit the quiz manually or automatically after the final timed question.

**FR9 — Result Calculation:** Calculate score, percentage, correct answers, wrong answers, and unanswered questions.

**FR10 — Restart/Exit:** Allow the user to start another quiz or close the application.

### 11. Non-Functional Requirements
The project also demonstrates the following non-functional requirements:

- **Usability:** The interface provides clear labels, controls, question numbering, and visible timing.
- **Reliability:** Invalid question-bank structures are rejected before the quiz is started.
- **Maintainability:** Question data is separated from application code in JSON.
- **Performance:** The application operates locally with a small question bank and no network requests.
- **Resource Efficiency:** It uses the Python standard library and local JSON data.
- **Error Handling:** File, JSON, and validation errors are handled when loading the question bank.

### 12. Question Bank
The question bank is stored in:
`data/questions.json`

The current data contains **40 questions**.

Distribution by category:
- General Knowledge — 10
- Python — 10
- Science — 10
- Mathematics — 10

The current difficulty distribution is:
- Easy — 26
- Medium — 14

The available difficulty selector also includes Hard, but the current question data does not contain Hard questions. This is consistent with the application's current data and allows future expansion.

Each question record contains:
- question
- options
- answer
- category
- difficulty

### 13. Question Validation
The `load_questions()` function loads the JSON file and validates its structure.

The validation checks that:
1. The loaded data is a list.
2. The list is not empty.
3. Every item is a dictionary containing the required fields.
4. Every question contains exactly four options.
5. The stored answer is one of the available options.

If validation fails, a `ValueError` is raised. The GUI catches file, JSON, and validation errors and displays an error message.

### 14. Category and Difficulty Filtering
The `filter_questions()` function returns questions matching the selected category and difficulty.

The value **All** acts as a wildcard:
- Category = All means every category is accepted.
- Difficulty = All means every difficulty is accepted.

Both filters can be used together. This allows the user to create a focused quiz such as Python + Easy or Science + Medium.

### 15. Random Quiz Generation
When the user clicks **START QUIZ**, the application first filters the available questions.

At least 10 matching questions are required. If fewer than 10 questions match the selected filters, the application displays a warning and asks the user to choose broader filters.

When enough questions are available, `random.sample()` selects 10 distinct questions for the quiz.

This makes repeated quizzes less predictable while preserving the fixed quiz size.

### 16. Graphical User Interface
The Tkinter interface contains three main user-facing stages:

**Start Screen**
- Application title
- Category selector
- Difficulty selector
- Quiz information
- Start button

**Question Screen**
- Question number
- Progress indicator
- Category label
- Question text
- Four radio-button choices
- Timer
- Previous/Next or Submit controls

**Result Screen**
- Quiz completion message
- Score
- Percentage
- Correct count
- Wrong count
- Unanswered count
- Try Again button
- Exit button

### 17. Timer System
Every question has a 15-second time limit.

The timer is managed with Tkinter's `after()` mechanism. The application updates the visible timer once per second.

The timer:
1. Starts when a quiz begins.
2. Resets when moving to another question.
3. Stops when the quiz is submitted or the screen returns to the start page.
4. Automatically advances when the remaining time reaches zero.

The last timed question automatically submits the quiz.

### 18. Answer Storage and Navigation
The application stores selected answers in a dictionary named `selected_answers`.

The question index is used as the dictionary key, while the selected option text is stored as the value.

When the user moves to another question, the current answer is saved. Returning to a previous question restores the stored selection.

This allows users to navigate through the quiz without losing answers that have already been selected.

### 19. Scoring and Results
The `calculate_score()` function compares each selected answer with the corresponding correct answer.

The final result calculates:
- Score out of 10
- Percentage
- Correct answers
- Wrong answers
- Unanswered questions

The result screen also displays a feedback message based on percentage:
- 80% or higher: Excellent work!
- 50% to below 80%: Good effort! Keep practicing.
- Below 50%: Keep learning and try again!

These messages are presentation feedback and are not part of the scoring algorithm.

### 20. Submission Handling
The user can submit the quiz after reaching the final question.

If there are unanswered questions and the submission is manual, the application asks the user whether to submit anyway.

If the user chooses not to submit, the quiz continues and the timer is restarted.

When the final question is reached automatically because of the timer, the application submits the quiz without showing the manual unanswered-question confirmation.

### 21. Data Structures
The project demonstrates several useful Python data structures:

- **Lists:** store the complete question collection, options, selected quiz questions, categories, and difficulties.
- **Dictionaries:** represent individual question records and selected answers.
- **Sets:** generate unique category names from the question bank.
- **Strings:** represent question text, options, categories, difficulty levels, and answers.

### 22. Program Architecture
The application is organized around reusable functions and a main `QuizApp` class.

**Data Layer**
- `data/questions.json`

**Core Functions**
- `load_questions()`
- `filter_questions()`
- `calculate_score()`

**GUI/Application Layer**
- `QuizApp`
- start screen
- question display
- navigation
- timer
- submission
- result display

**Testing Layer**
- `tests/test_quiz_application.py`

This structure keeps question processing functions independently testable while the class manages the Tkinter interface and application state.

### 23. Program Flow
```text
START
  |
  v
Load JSON Question Bank
  |
  v
Validate Questions
  |
  v
Display Start Screen
  |
  v
Select Category + Difficulty
  |
  v
Filter Questions
  |
  +---- Less than 10? ---- YES ----> Show Warning
  |                                      |
  |                                      v
  |                                Select Again
  |
  NO
  |
  v
Randomly Select 10 Questions
  |
  v
Display Question + 15s Timer
  |
  v
Save Answer
  |
  +---- More Questions? ---- YES ----> Next Question
  |                                      |
  |                                      v
  |                                 Reset Timer
  |
  NO
  |
  v
Calculate Score
  |
  v
Display Result
  |
  +---- Try Again? ---- YES ----> Start Screen
  |
  NO
  |
  v
END
```

### 24. Error Handling
The project handles several important error conditions.

**Question-file errors**
- Missing/unreadable files are caught during application initialization.
- Invalid JSON is caught.
- Invalid question structures raise validation errors.

**Insufficient filtered questions**
- If fewer than 10 questions match the selected filters, the application shows a warning instead of starting an incomplete quiz.

**Incomplete manual submission**
- The application asks for confirmation before submitting when unanswered questions remain.

**Timer cleanup**
- Existing Tkinter timer callbacks are cancelled when appropriate to avoid unwanted timer activity after leaving the quiz screen.

### 25. Testing
The project includes:
`tests/test_quiz_application.py`

The test suite uses Python's `unittest` framework and covers six tests:

1. Loading questions from a temporary JSON file.
2. Filtering by category.
3. Filtering by difficulty.
4. Filtering by both category and difficulty.
5. Correct score calculation.
6. Rejection of an invalid question file.

The test suite was executed against the project during report preparation.

**Result: 6 tests passed successfully.**

The tests focus on core data-processing functions and do not launch the Tkinter GUI.

### 26. Advantages
- Clean graphical interface
- Beginner-friendly design
- Separate JSON question bank
- Four subject categories
- Category and difficulty filtering
- Randomized 10-question quizzes
- Time-limited questions
- Previous/Next navigation
- Automatic timer advancement
- Score and percentage calculation
- Correct/wrong/unanswered statistics
- Input and data validation
- Automated unit tests
- No third-party dependencies
- Easy to expand with additional questions

### 27. Limitations
- Desktop application only
- Single-user local application
- No login or user profiles
- No database
- No online leaderboard
- No multiplayer mode
- No cloud synchronization
- Current question bank contains Easy and Medium questions but no Hard questions
- Quiz size is currently fixed at 10 questions
- Results are not permanently stored

### 28. Future Scope
Possible future improvements include:
- Adding more questions and additional categories
- Adding a complete Hard question set
- Allowing users to choose quiz length
- Adding a question editor
- Saving player history and high scores
- Adding user profiles
- Adding a database for persistent results
- Adding an online leaderboard
- Adding sound effects and visual animations
- Adding image-based questions
- Adding a review screen showing correct answers
- Exporting quiz results
- Creating a web version

These are possible extensions and are not part of the current implementation.

### 29. Conclusion
Quiz Application provides a complete beginner-level desktop quiz solution using Python and Tkinter. It combines a structured JSON question bank with filtering, random question selection, timed interaction, navigation, scoring, result reporting, validation, and automated testing.

The project demonstrates practical Python concepts including functions, classes, lists, dictionaries, sets, file handling, JSON processing, randomization, exception handling, event-driven programming, and unit testing. The implementation remains simple enough for a first-semester project while providing a polished graphical user experience.

### 30. Run Instructions
1. Install Python 3.9 or newer.
2. Open a terminal in the project folder.
3. Run:
   `python quiz_application.py`
4. On Windows, `py quiz_application.py` can also be used if required.
5. To run the tests:
   `python -m unittest discover -s tests -v`

Tkinter is normally included with standard Python installations. No third-party package installation is required.
