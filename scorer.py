def judge(questions: str, expects: str, ansewer: str, results: str) -> bool:

 if not expects:
   return False

 return expects.strip().lower() in (ansewer or "".lower)


