# Comparison: Human vs AI Version

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes because (`appointment['patient']`) are self-explanatory | Slightly less — tuple indices like (`a[0]`, `a[1]`) require memorising order |
| Runs successfully? | Yes | Yes |
| Uses only required features? | Yes | Yes |
| Adds assumptions? | No extra assumptions | Assumes `patient_name` is always valid — no check |
| Handles errors? | Yes — raises `ValueError` on empty patient name | No — accepts blank/`None` fields silently |
| Could I explain it? | Yes, you wrote it | Yes, but you'd need to explain *why* it lacks validation |