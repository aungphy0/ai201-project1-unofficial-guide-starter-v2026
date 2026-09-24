# Run log — after_advice

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-23 18:57

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| When should I start applying for a summer internship? | pass | pass | pass |
| How much RAM do students recommend for a laptop for CS courses? | pass | pass | pass |
| Which meal plan tier do students recommend for most people? | pass | pass | pass |
| How late in the term can you declare the pass/fail option? | pass | pass | pass |
| When are the dorm laundry rooms least busy? | pass | pass | pass |

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

### When should I start applying for a summer internship? — run 1

- Best distance: 0.3008 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_first_year_regret.txt, thread_internship_timing.txt, thread_pass_fail.txt

```
You should start looking earlier than feels reasonable, as large employers close applications in October and November for the following summer. Smaller and local places hire in February and March. 

Source: thread_internship_timing.txt
```

### When should I start applying for a summer internship? — run 2

- Best distance: 0.3008 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_first_year_regret.txt, thread_internship_timing.txt, thread_pass_fail.txt

```
You should start looking for a summer internship earlier than feels reasonable, as large employers close their applications in October and November for the following summer (thread_internship_timing.txt).
```

### When should I start applying for a summer internship? — run 3

- Best distance: 0.3008 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_first_year_regret.txt, thread_internship_timing.txt, thread_pass_fail.txt

```
You should start looking earlier than feels reasonable, as large employers close their applications in October and November for the following summer (thread_internship_timing.txt). Smaller and local places hire in February and March if you miss the autumn window (thread_internship_timing.txt).
```

### How much RAM do students recommend for a laptop for CS courses? — run 1

- Best distance: 0.1905 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_professor_email.txt

```
Students recommend 16GB of RAM for a laptop for CS courses. 

Source: thread_laptop_specs.txt
```

### How much RAM do students recommend for a laptop for CS courses? — run 2

- Best distance: 0.1905 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_professor_email.txt

```
Students recommend 16GB of RAM for a laptop for CS courses. 

Source: thread_laptop_specs.txt
```

### How much RAM do students recommend for a laptop for CS courses? — run 3

- Best distance: 0.1905 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_professor_email.txt

```
Students recommend 16GB of RAM for a laptop for CS courses. 

Source: thread_laptop_specs.txt
```

### Which meal plan tier do students recommend for most people? — run 1

- Best distance: 0.3320 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_meal_plan_tier.txt, thread_pass_fail.txt, thread_printing.txt, thread_study_spots.txt

```
For most people outside of Fenwick (which has kitchenettes), students recommend the middle tier. 

Source: `thread_meal_plan_tier.txt`
```

### Which meal plan tier do students recommend for most people? — run 2

- Best distance: 0.3320 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_meal_plan_tier.txt, thread_pass_fail.txt, thread_printing.txt, thread_study_spots.txt

```
For most people (everywhere except Fenwick, which has kitchenettes), students recommend the middle tier meal plan. 

Source: thread_meal_plan_tier.txt
```

### Which meal plan tier do students recommend for most people? — run 3

- Best distance: 0.3320 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_meal_plan_tier.txt, thread_pass_fail.txt, thread_printing.txt, thread_study_spots.txt

```
For most people living outside of Fenwick (which has kitchenettes), students recommend getting the middle tier. 

Source: `thread_meal_plan_tier.txt`
```

### How late in the term can you declare the pass/fail option? — run 1

- Best distance: 0.4741 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
You can declare the pass/fail option as late as week eight (*thread_pass_fail.txt* and *thread_first_year_regret.txt*).
```

### How late in the term can you declare the pass/fail option? — run 2

- Best distance: 0.4741 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
You can declare the pass/fail option as late as week eight (*thread_pass_fail.txt* and *thread_first_year_regret.txt*).
```

### How late in the term can you declare the pass/fail option? — run 3

- Best distance: 0.4741 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
You can declare the pass/fail option as late as week eight (`thread_pass_fail.txt` and `thread_first_year_regret.txt`).
```

### When are the dorm laundry rooms least busy? — run 1

- Best distance: 0.3789 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Laundry is actually free in the dorms on Tuesday and Wednesday mornings in every building. 

Source: thread_laundry_timing.txt
```

### When are the dorm laundry rooms least busy? — run 2

- Best distance: 0.3789 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Laundry is actually free in the dorms on Tuesday and Wednesday mornings in every building. 

Source: thread_laundry_timing.txt
```

### When are the dorm laundry rooms least busy? — run 3

- Best distance: 0.3789 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Laundry is actually free (least busy) on Tuesday and Wednesday mornings in every building. 

Source: thread_laundry_timing.txt
```
