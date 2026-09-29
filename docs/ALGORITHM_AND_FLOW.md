# Algorithm and Flow

## Algorithm

1. Start the program.
2. Load questions from `data/questions.json`.
3. Validate the question data.
4. Display the start screen.
5. Let the user choose a category and difficulty.
6. Filter the available questions.
7. Check that at least 10 questions are available.
8. Randomly select 10 questions.
9. Display the first question and start a 15-second timer.
10. Store the selected answer.
11. Allow the user to move to the next or previous question.
12. If the timer reaches zero, automatically move to the next question.
13. After the last question, submit the quiz.
14. Compare selected answers with the correct answers.
15. Calculate score and percentage.
16. Display correct, wrong, and unanswered counts.
17. Allow the user to try again or exit.
18. End.

## Flowchart

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
