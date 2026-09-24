# Run log — after_advice

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-23 18:12

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What is the first movie in this year? | fail | fail | fail |
| Is that health care system still good? | fail | fail | fail |
| What is a possibility for raining tomorrow? | fail | fail | fail |
| How is the world cup champion? | fail | fail | fail |
| What number is the lucky number? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.890 | refused |
| How do I change the oil in a diesel engine? | 0.930 | refused |
| Who won the 1994 World Cup? | 0.787 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.828 | refused |
| How do I write a for loop in Rust? | 0.871 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What is the first movie in this year? — run 1

- Best distance: 0.7953 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_internship_timing.txt, thread_laptop_specs.txt, thread_meal_plan_tier.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is the first movie in this year? — run 2

- Best distance: 0.7953 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_internship_timing.txt, thread_laptop_specs.txt, thread_meal_plan_tier.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is the first movie in this year? — run 3

- Best distance: 0.7953 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_internship_timing.txt, thread_laptop_specs.txt, thread_meal_plan_tier.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### Is that health care system still good? — run 1

- Best distance: 0.8134 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt

```
I don't have enough information about that.
```

### Is that health care system still good? — run 2

- Best distance: 0.8134 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt

```
I don't have enough information about that.
```

### Is that health care system still good? — run 3

- Best distance: 0.8134 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt

```
I don't have enough information about that.
```

### What is a possibility for raining tomorrow? — run 1

- Best distance: 0.6169 (refused by the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is a possibility for raining tomorrow? — run 2

- Best distance: 0.6169 (refused by the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is a possibility for raining tomorrow? — run 3

- Best distance: 0.6169 (refused by the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_laundry_timing.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### How is the world cup champion? — run 1

- Best distance: 0.8355 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_meal_plan_tier.txt, thread_professor_email.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### How is the world cup champion? — run 2

- Best distance: 0.8355 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_meal_plan_tier.txt, thread_professor_email.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### How is the world cup champion? — run 3

- Best distance: 0.8355 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_meal_plan_tier.txt, thread_professor_email.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What number is the lucky number? — run 1

- Best distance: 0.7788 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_late_work.txt, thread_parking.txt, thread_textbook_editions.txt

```
I don't have enough information about that.
```

### What number is the lucky number? — run 2

- Best distance: 0.7788 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_late_work.txt, thread_parking.txt, thread_textbook_editions.txt

```
I don't have enough information about that.
```

### What number is the lucky number? — run 3

- Best distance: 0.7788 (refused by the gate)
- Sources retrieved: thread_bike_commute.txt, thread_clubs.txt, thread_late_work.txt, thread_parking.txt, thread_textbook_editions.txt

```
I don't have enough information about that.
```
