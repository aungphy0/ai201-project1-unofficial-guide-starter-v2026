# Run log — after_advice

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-23 18:48

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What major should I choose if I want to be an AI Engineer | fail | fail | fail |
| When is the best time in a year to apply for internships | fail | fail | fail |
| Which laptop should I buy a laptop with a Windows operating system? | fail | fail | fail |
| What is the meal plan? | fail | fail | fail |
| What is the weather like today? | fail | fail | fail |

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

### What major should I choose if I want to be an AI Engineer — run 1

- Best distance: 0.7036 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_textbook_editions.txt, thread_transfer_credits.txt

```
I don't have enough information about that.
```

### What major should I choose if I want to be an AI Engineer — run 2

- Best distance: 0.7036 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_textbook_editions.txt, thread_transfer_credits.txt

```
I don't have enough information about that.
```

### What major should I choose if I want to be an AI Engineer — run 3

- Best distance: 0.7036 (refused by the gate)
- Sources retrieved: thread_changing_major.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_textbook_editions.txt, thread_transfer_credits.txt

```
I don't have enough information about that.
```

### When is the best time in a year to apply for internships — run 1

- Best distance: 0.3920 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_professor_email.txt

```
Large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. 

Source: thread_internship_timing.txt
```

### When is the best time in a year to apply for internships — run 2

- Best distance: 0.3920 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_professor_email.txt

```
The best time to apply depends on the type of employer: large employers close their applications in October and November for the following summer, while smaller and local places hire in February and March. 

Source: `thread_internship_timing.txt`
```

### When is the best time in a year to apply for internships — run 3

- Best distance: 0.3920 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_professor_email.txt

```
Large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. 

Source: thread_internship_timing.txt
```

### Which laptop should I buy a laptop with a Windows operating system? — run 1

- Best distance: 0.5593 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laptop_specs.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_professor_email.txt

```
I don't have enough information to answer whether you should buy a laptop with a Windows operating system, as the provided documents do not mention operating systems (thread_laptop_specs.txt).
```

### Which laptop should I buy a laptop with a Windows operating system? — run 2

- Best distance: 0.5593 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laptop_specs.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_professor_email.txt

```
I don't have enough information to answer your question.
```

### Which laptop should I buy a laptop with a Windows operating system? — run 3

- Best distance: 0.5593 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laptop_specs.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_professor_email.txt

```
I don't have enough information to answer your question.
```

### What is the meal plan? — run 1

- Best distance: 0.4170 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_meal_plan_tier.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
According to the provided documents, declining balance rolls within the semester (though not between them) and must be spent in December or lost. Additionally, the meal plan has tiers, such as the highest tier (which makes sense only if you eat three meals a day in the halls) and a middle tier, and students in buildings with kitchenettes like Fenwick can go down a tier and cook two or three nights. 

Source: `thread_meal_plan_tier.txt`
```

### What is the meal plan? — run 2

- Best distance: 0.4170 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_meal_plan_tier.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on the provided documents, the highest meal plan tier makes sense only if you eat three meals a day in the halls every single day, and declining balance rolls within the semester but not between them (thread_meal_plan_tier.txt). Additionally, students in buildings with kitchenettes, like Fenwick, can go down a tier and cook two or three nights, while everyone else should get the middle tier (thread_meal_plan_tier.txt).
```

### What is the meal plan? — run 3

- Best distance: 0.4170 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_late_work.txt, thread_meal_plan_tier.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on the provided documents, the meal plan has different tiers:
- A highest tier, which only makes sense if you eat three meals a day in the halls every single day (thread_meal_plan_tier.txt).
- A middle tier, which is recommended for everywhere except Fenwick (thread_meal_plan_tier.txt).
- A lower tier used by people in Fenwick who cook two or three nights because their building has kitchenettes (thread_meal_plan_tier.txt).
- The plan includes a declining balance that rolls within the semester but not between them (thread_meal_plan_tier.txt). 

Source: thread_meal_plan_tier.txt
```

### What is the weather like today? — run 1

- Best distance: 0.6598 (refused by the gate)
- Sources retrieved: thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is the weather like today? — run 2

- Best distance: 0.6598 (refused by the gate)
- Sources retrieved: thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```

### What is the weather like today? — run 3

- Best distance: 0.6598 (refused by the gate)
- Sources retrieved: thread_late_work.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_winter_advice.txt

```
I don't have enough information about that.
```
