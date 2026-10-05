# The Unofficial Guide

<!-- Aung Phyo 'advice_threads' -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

     I picked advice_threads. The system answered 5 different questions. 
     Each question got replied with different replies and some replies are 
     not related with the question.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: 5**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `thread_bike_commute.txt#0` — produced by: `chunker.py::fallback_split`

```
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

--- reply 3 (22 votes) ---
Both true. I keep a cheap bike for September to November and walk the rest of the year. Total cost was about $120 for the bike and I don't care what happens to it.

--- reply 4 (5 votes) ---
If you do get one, the campus does free registration and it's the only reason I got mine back after it was taken.


```

**Chunk 2** — source: `thread_first_gen.txt#0` — produced by: `chunker.py::fallback_split`

```
THREAD: Anything specific for first-generation students?

--- reply 1 (33 votes) ---
The advising office has a specific programme and it is genuinely good, but it is opt-in and badly publicised. Ask for it by name.

--- reply 2 (41 votes) ---
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

--- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.


```

**Chunk 3** — source: `thread_laptop_specs.txt#0` — produced by: `chunker.py::fallback_split`

```
THREAD: How much laptop do I actually need for CS courses?

--- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice.

--- reply 2 (18 votes) ---
Adding: the lab machines exist and are better than anything you'll buy. For the heavy assignments people just use those.

--- reply 3 (12 votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.


```

**Chunk 4** — source: `thread_office_hours_etiquette.txt#0` — produced by: `chunker.py::fallback_split`

```
THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.

--- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up.

--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.


```

**Chunk 5** — source: `thread_roommate_conflict.txt#0` — produced by: `chunker.py::fallback_split`

```
THREAD: Roommate situation isn't working. What now?

--- reply 1 (28 votes) ---
Talk to your RA early, and frame it as 'we need help sorting this out' rather than 'move me'. Room changes are possible but the process starts with mediation and skipping that step slows it down.

--- reply 2 (14 votes) ---
Room changes happen at the semester boundary almost always, and mid-semester only in fairly serious cases.

--- reply 3 (33 votes) ---
Write down specifics before the meeting. 'It's not working' is hard to act on; 'guests four nights a week past 2am' is not.



```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

**Answer:**

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  |  |  |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

Evidence file: `results/run_2026-09-23_1859_after_advice.md`, produced by
`run_eval.py::main` (gate evidence from `run_eval.py::check_out_of_scope`).
Corpus `advice_threads`, chunks from `chunker.py::fallback_split`
(800 characters, 120 overlap), top-k 5, cutoff 0.6.

> Note on the file name: this run was labelled `after_advice` because it came
> after I switched from `campus_life` to `advice_threads` and fixed my scorer
> and questions. It is the **before** for my unit 2 improvement: it is the
> first run with my final questions, the right corpus, and the original
> chunker. Earlier files in `results/` used broken questions or the wrong
> corpus, so I don't count them.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Retrieved chunks are 200–800 tokens and carry the answer without excessive unrelated text | 4 of 5 | 0 of 5 | 0 of 5 | 0 of 5 | MISSED |
| 5. Every key claim in the answer is supported by the cited source, nothing invented | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

How each number was counted:

- **1** — the answering thread appears in "Sources retrieved" for all five
  questions in all three runs, and every answer contains the `expects` keyword
  (`scorer.py::judge` returned pass 15/15).
- **3** — one deterministic pass; same number in every column.
- **4** — also deterministic (chunking doesn't change between runs).
  `chunker.py::fallback_split` returns each thread as a single chunk because
  every file is under 800 characters. The five answering chunks are about
  120–195 tokens (thread_internship_timing ≈ 120, thread_laundry_timing ≈ 135,
  thread_laptop_specs ≈ 146, thread_meal_plan_tier ≈ 185,
  thread_pass_fail ≈ 193). None reaches 200.
- **5** — checked by hand: I read each of the 15 answers next to the thread it
  cited.

### Real output (from `results/run_2026-09-23_1859_after_advice.md`)

**Criteria 1, 2 and 5** — `run_eval.py::run_once` → `store.py::search` → `generate.py::answer_from_chunks`

```
Q: How late in the term can you declare the pass/fail option? — run 1
- Best distance: 0.4741 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

You can declare the pass/fail option as late as week eight.

This information comes from `thread_pass_fail.txt` and `thread_first_year_regret.txt`.
```

```
Q: How much RAM do students recommend for a laptop for CS courses? — run 1
- Best distance: 0.1905 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_professor_email.txt

Students recommend 16GB of RAM for a laptop for CS courses.

Source: `thread_laptop_specs.txt`
```

```
Q: When are the dorm laundry rooms least busy? — run 1
- Best distance: 0.3789 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt, thread_study_spots.txt

Laundry is actually free in the dorms on Tuesday and Wednesday mornings in every building.

Source: thread_laundry_timing.txt
```

**Criterion 3** — `run_eval.py::check_out_of_scope`, cutoff 0.6, refused 5 of 5

```
| What is the capital of Mongolia?                            | 0.890 | refused |
| How do I change the oil in a diesel engine?                 | 0.930 | refused |
| Who won the 1994 World Cup?                                 | 0.787 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.828 | refused |
| How do I write a for loop in Rust?                          | 0.871 | refused |
```

**Criterion 4** — `chunker.py::fallback_split`, the chunk that answers the pass/fail question (`thread_pass_fail.txt#0`, ≈193 tokens)

```
THREAD: When should you actually use the pass/fail option?

--- reply 1 (24 votes) ---
For a course outside your major that you're taking because you're curious. That's what it's for and most people never use it.

--- reply 2 (38 votes) ---
The part that isn't advertised: you can declare it as late as week eight. So take the midterm first, then decide.

--- reply 3 (20 votes) ---
Careful with this one if you're applying to graduate programmes. Some want a letter grade for prerequisites and a P doesn't satisfy it.

--- reply 4 (12 votes) ---
Two per year and eight across the degree. I hit the annual limit in second year and regretted spending one on an easy course.
```

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | The answering thread was retrieved for 5 of 5 questions in all three runs, above the 4-of-5 target every time. |
| 2 | Every answer names a source | MET | All 15 answers name at least one `.txt` file; the target was 5 of 5 and it held in every run. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5 refused. The closest one (World Cup, 0.787) is still well above the 0.6 cutoff, and the furthest in-scope question (pass/fail, 0.474) is well below it. |
| 4 | Chunks are 200–800 tokens and carry the answer without excessive unrelated text | MISSED | 0 of 5 answering chunks reach 200 tokens. It also misses on the "unrelated text" half: in the pass/fail chunk above, 3 of the 4 replies are not about the deadline. |
| 5 | Answer is supported by the cited source | MET | I found the supporting sentence for every claim in all 15 answers. Closest call: the laundry answer says laundry is "free", which reads like no cost. The thread uses "free" to mean "machines available", so the claim is supported, but the wording could mislead a reader. I counted it as supported. |

## Diagnoses

**Criterion 4 — stage: chunking.**

`CHUNK_SIZE` is 800 *characters* but my criterion is in *tokens*. Every
`advice_threads` file is under 800 characters (shortest 320, longest 796), so
`fallback_split` never cuts anything: each thread becomes exactly one chunk of
roughly 90–225 tokens. The five threads my questions hit are all under 200.
The size half of the criterion can't be met by tuning `CHUNK_SIZE`, because a
bigger window has nothing more to take from the same file. The only way to get
over 200 tokens would be to merge different threads into one chunk, which
breaks the other half of the same criterion ("without excessive unrelated
information").

The unrelated-text half is also a chunking problem. One thread is several
replies, and each of my questions is answered by one reply (pass/fail → reply
2, internship → reply 1, meal plan → reply 1, laundry → reply 1). Whole-thread
chunks always carry the other replies along. That shows up in retrieval too:
the pass/fail question's best distance is 0.474, the weakest of the five,
because the "week eight" sentence is diluted by three replies about other
things.

No other misses. Criteria 1, 2, 3 and 5 all had headroom (5 of 5 against a
4-of-5 or 5-of-5 target), so those targets were probably set too low for a
corpus this small and clean. If I tightened one, it would be criterion 1: "the
**top-ranked** chunk is from the answering thread" for 5 of 5, instead of "any
of the 5 retrieved chunks".

## The Improvement

**What I changed:** I replaced the body of `chunker.py::split_documents` so it
splits each thread on its `--- reply N ---` markers. Each chunk is one reply,
with the `THREAD:` title line repeated at the top so a short reply like
"Tuesday and Wednesday mornings, every building" still makes sense on its own.
Replies are never cut mid-sentence. The corpus goes from 23 chunks (avg 545
characters) to 75 chunks (avg 202 characters, 132–281).

**Why I picked it:** My criterion 4 diagnosis says the answering reply shares
its chunk with unrelated replies, and that is the half of criterion 4 I can
fix without merging threads. I expect this to make the size half *worse*
(chunks get smaller, not bigger). I'm reporting that rather than hiding it.

### Run Log — After

Evidence file: `results/run_2026-10-04_1938_after.md`, produced by
`run_eval.py::main`. Same corpus, questions, top-k 5 and cutoff 0.6 as before;
the only change is chunks now come from `chunker.py::split_documents`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Retrieved chunks are 200–800 tokens and carry the answer without excessive unrelated text | 4 of 5 | 0 of 5 | 0 of 5 | 0 of 5 | MISSED |
| 5. Every key claim in the answer is supported by the cited source, nothing invented | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

How each number was counted: same method as the Before table. Criterion 4 is
still 0 of 5 on size (each chunk is now one reply, roughly 35–70 tokens), but
on the unrelated-text half it is now 5 of 5: the chunk that answers each
question is the single reply that contains the answer, plus the thread title.

Best distance per question (lower = closer match):

| Question | Before | After |
|---|---|---|
| Internship timing | 0.301 | 0.190 |
| Laptop RAM | 0.191 | 0.156 |
| Meal plan tier | 0.332 | 0.294 |
| Pass/fail deadline | 0.474 | 0.217 |
| Laundry timing | 0.379 | 0.278 |
| Out-of-scope range | 0.787–0.930 | 0.807–0.896 |

### Real output (from `results/run_2026-10-04_1938_after.md`)

```
Q: How late in the term can you declare the pass/fail option? — run 1
- Best distance: 0.2170 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_pass_fail.txt

You can declare the pass/fail option as late as week eight (source: `thread_pass_fail.txt` and `thread_first_year_regret.txt`).
```

```
Q: When are the dorm laundry rooms least busy? — run 2
- Best distance: 0.2784 (passed the gate)
- Sources retrieved: thread_laundry_timing.txt, thread_roommate_conflict.txt

Laundry rooms are least busy on Tuesday and Wednesday mornings in every building, according to **thread_laundry_timing.txt**.
```

```
Out-of-scope, `run_eval.py::check_out_of_scope`, cutoff 0.6 — refused 5 of 5
| What is the capital of Mongolia?                            | 0.893 | refused |
| How do I change the oil in a diesel engine?                 | 0.896 | refused |
| Who won the 1994 World Cup?                                 | 0.893 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.807 | refused |
| How do I write a for loop in Rust?                          | 0.835 | refused |
```

**Did it help?**

Yes for the problem I aimed at, no for the verdicts. Every criterion has the
same verdict as before: 1, 2, 3 and 5 MET, 4 still MISSED. As I predicted, the
size half of criterion 4 got further away (chunks went from ~120–195 tokens to
~35–70).

What did improve is retrieval. The best distance dropped for all five
questions, and the biggest gain was the one my diagnosis pointed at: pass/fail
went from 0.474 to 0.217 once the "week eight" reply stopped sharing a chunk
with three unrelated replies. The gate got safer too. Before, the gap between
my worst in-scope question (0.474) and my closest out-of-scope question
(0.787) was 0.31. Now it is 0.29 to 0.81, a gap of 0.51, so 0.6 sits much more
comfortably in the middle. Fewer unrelated threads come back as well (2–3
source files per question instead of 4–5).

One answer-quality change I didn't expect: before, the laundry answer said
laundry is "free", which could be read as no cost. After, all three runs say
"least busy" or "free (least busy)". With only the one reply and the title in
front of it, the model read "free" the way the thread meant it.

## What's Still Broken

**Criterion 4 (size half).** It is still missed and I stopped there on
purpose. No thread in `advice_threads` is long enough for a 200-token chunk,
so the only way to hit the target is to glue unrelated threads together. That
would make retrieval worse to satisfy a number. The real problem is the
criterion, not the pipeline (see below).

**Scorer limit.** `scorer.py::judge` only checks that a keyword appears. The
laundry answer passes because it contains "Tuesday", but it also says
"free", which a reader could take to mean no cost. A keyword scorer can't catch
that, which is why I checked criterion 5 by hand.

## What I'd Do Differently

I'd rewrite **criterion 4**. I wrote "200–800 tokens" before measuring my
documents, and it mixed up units: the config counts characters and the
criterion counts tokens. The longest thread in the corpus is about 225 tokens,
so the floor was close to impossible from the start. A better version, based on
what I actually saw: "For at least 4 of 5 questions, the chunk containing the
answer holds no more than one reply that is unrelated to the question, and no
reply is cut mid-sentence." That is countable and fits a corpus of short
threads.

I'd also set criteria 1 and 3 higher. Both cleared their targets with room to
spare, so they didn't tell me much.
