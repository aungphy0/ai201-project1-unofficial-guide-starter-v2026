"""
My scorer.

What I decided "correct" means, before running anything:

An answer passes when it contains the `expects` keyword I wrote down in
questions.py at the same time as the question itself. That keyword is the one
fact the answer has to carry — a date, a number, a named tier. If the answer
talks around the subject without landing on that fact, it is not an answer to
the question I asked.

Two things count as an automatic fail:

  - The gate refused. A refusal is the right behaviour for an out-of-scope
    question, but these five are in scope, so a refusal here is a miss.
  - The question has no `expects`. I can't judge correctness against a
    criterion I never wrote, so I'd rather fail loudly than pass silently.

Matching is case-insensitive substring, which is deliberately forgiving about
phrasing and deliberately strict about the fact. It will not catch an answer
that names the right number inside a wrong claim; that's the known limit of
keyword scoring and I note it in the README.
"""


def judge(question: str, expects: str, answer: str, results) -> bool:
    """True when the answer carries the fact I said it had to carry."""
    from gate import REFUSAL

    expects = (expects or "").strip().lower()
    answer = (answer or "").strip()

    if not expects:
        # No criterion was written for this question — can't score it.
        return False

    if answer == REFUSAL:
        # Gate refused an in-scope question.
        return False

    return expects in answer.lower()
