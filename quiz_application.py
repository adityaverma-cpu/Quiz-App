import json
import random
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_FILE = BASE_DIR / "data" / "questions.json"

BG = "#f4f7fb"
CARD = "#ffffff"
PRIMARY = "#2563eb"
PRIMARY_DARK = "#1d4ed8"
TEXT = "#172033"
MUTED = "#64748b"
SUCCESS = "#15803d"
DANGER = "#dc2626"


def load_questions(path=QUESTIONS_FILE):
    """Load and validate the question bank from JSON."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not data:
        raise ValueError("Question bank must contain at least one question.")

    required = {"question", "options", "answer", "category", "difficulty"}
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Invalid question format at question {index}.")
        if len(item["options"]) != 4:
            raise ValueError(f"Question {index} must have exactly four options.")
        if item["answer"] not in item["options"]:
            raise ValueError(f"Answer is not one of the options in question {index}.")
    return data


def filter_questions(questions, category="All", difficulty="All"):
    result = [
        q for q in questions
        if (category == "All" or q["category"] == category)
        and (difficulty == "All" or q["difficulty"] == difficulty)
    ]
    return result


def calculate_score(questions, selected_answers):
    return sum(
        selected_answers.get(index) == question["answer"]
        for index, question in enumerate(questions)
    )


class QuizApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("900x650")
        self.root.minsize(760, 560)
        self.root.configure(bg=BG)

        try:
            self.questions = load_questions()
        except (OSError, ValueError, json.JSONDecodeError) as error:
            messagebox.showerror("Quiz Error", f"Could not load questions:\n{error}")
            self.root.destroy()
            return

        self.categories = ["All"] + sorted({q["category"] for q in self.questions})
        self.difficulties = ["All", "Easy", "Medium", "Hard"]

        self.quiz_questions = []
        self.current_index = 0
        self.selected_answers = {}
        self.time_left = 0
        self.timer_job = None

        self.show_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, width=16):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            font=("Segoe UI", 11, "bold"),
            bg=PRIMARY,
            fg="white",
            activebackground=PRIMARY_DARK,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=8,
        )

    def show_start_screen(self):
        self.stop_timer()
        self.clear_screen()

        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=40, pady=35)

        card = tk.Frame(outer, bg=CARD, bd=0, highlightthickness=1,
                        highlightbackground="#dbe3ef")
        card.pack(fill="both", expand=True)

        tk.Label(
            card, text="QUIZ APPLICATION",
            font=("Segoe UI", 28, "bold"), fg=TEXT, bg=CARD
        ).pack(pady=(55, 8))

        tk.Label(
            card, text="Test your knowledge. Track your score. Improve your skills.",
            font=("Segoe UI", 12), fg=MUTED, bg=CARD
        ).pack(pady=(0, 30))

        settings = tk.Frame(card, bg=CARD)
        settings.pack(pady=5)

        tk.Label(settings, text="Category", font=("Segoe UI", 11, "bold"),
                 fg=TEXT, bg=CARD).grid(row=0, column=0, padx=12, pady=8)
        self.category_var = tk.StringVar(value="All")
        category_menu = tk.OptionMenu(settings, self.category_var, *self.categories)
        category_menu.config(font=("Segoe UI", 10), width=18, bg="#eef2ff", relief="flat")
        category_menu.grid(row=0, column=1, padx=12, pady=8)

        tk.Label(settings, text="Difficulty", font=("Segoe UI", 11, "bold"),
                 fg=TEXT, bg=CARD).grid(row=1, column=0, padx=12, pady=8)
        self.difficulty_var = tk.StringVar(value="All")
        difficulty_menu = tk.OptionMenu(settings, self.difficulty_var, *self.difficulties)
        difficulty_menu.config(font=("Segoe UI", 10), width=18, bg="#eef2ff", relief="flat")
        difficulty_menu.grid(row=1, column=1, padx=12, pady=8)

        tk.Label(
            card,
            text="10 questions • 15 seconds per question • 4 choices",
            font=("Segoe UI", 10), fg=MUTED, bg=CARD
        ).pack(pady=18)

        self.make_button(card, "START QUIZ", self.start_quiz, 20).pack(pady=12)

        tk.Label(
            card,
            text="Tip: Choose a category and difficulty, then answer as many as you can.",
            font=("Segoe UI", 9), fg=MUTED, bg=CARD
        ).pack(pady=15)

    def start_quiz(self):
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()
        available = filter_questions(self.questions, category, difficulty)

        if len(available) < 10:
            messagebox.showwarning(
                "Not Enough Questions",
                f"Only {len(available)} question(s) match your filters.\n"
                "Please choose a broader category or difficulty."
            )
            return

        self.quiz_questions = random.sample(available, 10)
        self.current_index = 0
        self.selected_answers = {}
        self.show_question()
        self.start_timer()

    def show_question(self):
        self.clear_screen()

        question = self.quiz_questions[self.current_index]
        total = len(self.quiz_questions)

        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=35, pady=(22, 5))

        tk.Label(
            header,
            text=f"Question {self.current_index + 1} of {total}",
            font=("Segoe UI", 14, "bold"), fg=TEXT, bg=BG
        ).pack(side="left")

        self.timer_label = tk.Label(
            header, text="", font=("Segoe UI", 14, "bold"), fg=PRIMARY, bg=BG
        )
        self.timer_label.pack(side="right")

        progress = tk.Frame(self.root, bg="#dbe3ef", height=8)
        progress.pack(fill="x", padx=35, pady=(5, 20))
        progress.update_idletasks()
        fill_width = max(1, int((self.current_index + 1) / total * 100))
        self.progress_label = tk.Label(
            progress, text=f"{fill_width}%", font=("Segoe UI", 7),
            fg="#ffffff", bg=PRIMARY, width=max(1, fill_width // 4)
        )
        self.progress_label.pack(side="left", fill="y")

        card = tk.Frame(self.root, bg=CARD, highlightthickness=1,
                        highlightbackground="#dbe3ef")
        card.pack(fill="both", expand=True, padx=35, pady=(0, 20))

        tk.Label(
            card, text=question["category"].upper(),
            font=("Segoe UI", 9, "bold"), fg=PRIMARY, bg=CARD
        ).pack(anchor="w", padx=30, pady=(25, 4))

        tk.Label(
            card, text=question["question"],
            font=("Segoe UI", 17, "bold"), fg=TEXT, bg=CARD,
            wraplength=780, justify="left"
        ).pack(anchor="w", padx=30, pady=(0, 22))

        options_frame = tk.Frame(card, bg=CARD)
        options_frame.pack(fill="x", padx=30)

        self.answer_var = tk.StringVar(value=self.selected_answers.get(self.current_index, ""))

        for option in question["options"]:
            radio = tk.Radiobutton(
                options_frame,
                text=option,
                variable=self.answer_var,
                value=option,
                font=("Segoe UI", 11),
                fg=TEXT,
                bg="#f8fafc",
                activebackground="#eef2ff",
                selectcolor="#dbeafe",
                anchor="w",
                padx=15,
                pady=11,
                relief="flat",
                cursor="hand2",
                wraplength=700,
                justify="left",
            )
            radio.pack(fill="x", pady=5)

        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=35, pady=(0, 22))

        if self.current_index > 0:
            self.make_button(footer, "← Previous", self.previous_question, 14).pack(side="left")

        if self.current_index < total - 1:
            self.make_button(footer, "Next →", self.next_question, 14).pack(side="right")
        else:
            self.make_button(footer, "SUBMIT QUIZ", self.submit_quiz, 16).pack(side="right")

    def save_current_answer(self):
        answer = self.answer_var.get()
        if answer:
            self.selected_answers[self.current_index] = answer

    def next_question(self):
        self.save_current_answer()
        if self.current_index < len(self.quiz_questions) - 1:
            self.current_index += 1
            self.reset_timer()
            self.show_question()

    def previous_question(self):
        self.save_current_answer()
        if self.current_index > 0:
            self.current_index -= 1
            self.reset_timer()
            self.show_question()

    def start_timer(self):
        self.stop_timer()
        self.time_left = 15
        self.update_timer()

    def reset_timer(self):
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        if not self.root.winfo_exists():
            return

        if hasattr(self, "timer_label") and self.timer_label.winfo_exists():
            self.timer_label.config(
                text=f"Time: {self.time_left}s",
                fg=DANGER if self.time_left <= 5 else PRIMARY
            )

        if self.time_left <= 0:
            self.auto_advance()
            return

        self.time_left -= 1
        self.timer_job = self.root.after(1000, self.update_timer)

    def auto_advance(self):
        self.save_current_answer()
        if self.current_index < len(self.quiz_questions) - 1:
            self.current_index += 1
            self.show_question()
            self.start_timer()
        else:
            self.submit_quiz(auto=True)

    def stop_timer(self):
        if self.timer_job is not None:
            try:
                self.root.after_cancel(self.timer_job)
            except tk.TclError:
                pass
            self.timer_job = None

    def submit_quiz(self, auto=False):
        self.stop_timer()
        self.save_current_answer()

        unanswered = len(self.quiz_questions) - len(self.selected_answers)
        if unanswered and not auto:
            proceed = messagebox.askyesno(
                "Submit Quiz",
                f"You have {unanswered} unanswered question(s).\n"
                "Do you want to submit anyway?"
            )
            if not proceed:
                self.start_timer()
                return

        score = calculate_score(self.quiz_questions, self.selected_answers)
        self.show_result(score)

    def show_result(self, score):
        self.clear_screen()
        total = len(self.quiz_questions)
        percentage = score / total * 100

        if percentage >= 80:
            message = "Excellent work!"
            message_color = SUCCESS
        elif percentage >= 50:
            message = "Good effort! Keep practicing."
            message_color = PRIMARY
        else:
            message = "Keep learning and try again!"
            message_color = DANGER

        card = tk.Frame(self.root, bg=CARD, highlightthickness=1,
                        highlightbackground="#dbe3ef")
        card.pack(fill="both", expand=True, padx=55, pady=45)

        tk.Label(card, text="QUIZ COMPLETE", font=("Segoe UI", 26, "bold"),
                 fg=TEXT, bg=CARD).pack(pady=(45, 10))

        tk.Label(card, text=message, font=("Segoe UI", 15, "bold"),
                 fg=message_color, bg=CARD).pack(pady=8)

        tk.Label(card, text=f"{score} / {total}",
                 font=("Segoe UI", 42, "bold"), fg=PRIMARY, bg=CARD).pack(pady=12)

        tk.Label(card, text=f"Percentage: {percentage:.1f}%",
                 font=("Segoe UI", 14), fg=TEXT, bg=CARD).pack(pady=4)

        correct = sum(
            self.selected_answers.get(i) == q["answer"]
            for i, q in enumerate(self.quiz_questions)
        )
        unanswered = total - len(self.selected_answers)
        wrong = total - correct - unanswered

        stats = tk.Frame(card, bg=CARD)
        stats.pack(pady=25)
        for label, value, color in (
            ("Correct", correct, SUCCESS),
            ("Wrong", wrong, DANGER),
            ("Unanswered", unanswered, MUTED),
        ):
            box = tk.Frame(stats, bg="#f8fafc", padx=25, pady=12)
            box.pack(side="left", padx=6)
            tk.Label(box, text=str(value), font=("Segoe UI", 18, "bold"),
                     fg=color, bg="#f8fafc").pack()
            tk.Label(box, text=label, font=("Segoe UI", 9),
                     fg=MUTED, bg="#f8fafc").pack()

        self.make_button(card, "TRY AGAIN", self.show_start_screen, 18).pack(pady=10)
        self.make_button(card, "EXIT", self.root.destroy, 18).pack(pady=5)


def main():
    root = tk.Tk()
    QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
