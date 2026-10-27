# Python - Async Comprehension

## Description
This project builds on `asyncio` with asynchronous generators and asynchronous comprehensions. It creates an async generator that yields random numbers, collects its values with an async comprehension, and measures how running several of these comprehensions in parallel affects the total runtime.

All scripts are written for **Python 3.8+**, use type annotations, and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Write an asynchronous generator with `async def` and `yield`.
* Consume an async generator with an async comprehension (`[i async for i in ...]`).
* Run several coroutines in parallel with `asyncio.gather`.
* Measure the total runtime of concurrent work with `time.perf_counter`.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Typing:** All functions are type-annotated and documented with docstrings.
* **Imports:** Modules whose names start with a digit are loaded with `__import__("<module>")`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-async_generator.py` | Async generator | `async_generator()` loops 10 times, waits 1 second asynchronously each time, and yields a random float between 0 and 10. |
| `1-async_comprehension.py` | Async comprehension | `async_comprehension()` collects the 10 values of `async_generator` into a list with an async comprehension. |
| `2-measure_runtime.py` | Run time for four parallel comprehensions | `measure_runtime()` runs `async_comprehension` four times with `asyncio.gather` and returns the total elapsed time (about 10 seconds, not 40). |

---

## 🚀 Execution & PEP 8 Testing

```bash
cat > main.py <<'EOF'
#!/usr/bin/env python3
import asyncio
measure_runtime = __import__('2-measure_runtime').measure_runtime

print(asyncio.run(measure_runtime()))
EOF
python3 main.py
```

```bash
pycodestyle 0-async_generator.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
