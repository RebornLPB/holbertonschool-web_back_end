# Python - Async

## Description
This project introduces asynchronous programming in Python with `asyncio`. It starts from a basic coroutine that waits a random time, then runs many coroutines concurrently, measures the resulting runtime, and finally wraps coroutines into `asyncio.Task` objects.

All scripts are written for **Python 3.8+**, use type annotations, and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Write coroutines with `async def` and suspend them with `await`.
* Run several coroutines concurrently and collect results as they finish with `asyncio.as_completed`.
* Measure the runtime of concurrent code with `time.perf_counter` and `asyncio.run`.
* Create `asyncio.Task` objects with `asyncio.create_task`.
* Annotate coroutines with return types (`float`, `List[float]`, `asyncio.Task`).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Typing:** All functions are type-annotated and documented with docstrings.
* **Imports:** Modules whose names start with a digit are loaded with `__import__("<module>")`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-basic_async_syntax.py` | The basics of async | `wait_random(max_delay=10)` waits for a random delay between 0 and `max_delay` seconds and returns it. |
| `1-concurrent_coroutines.py` | Multiple coroutines at the same time | `wait_n(n, max_delay=10)` spawns `n` `wait_random` coroutines and returns their delays in completion order. |
| `2-measure_runtime.py` | Measure the runtime | `measure_time(n, max_delay=10)` runs `wait_n` and returns the average elapsed time per coroutine. |
| `3-tasks.py` | Tasks | `task_wait_random(max_delay=10)` wraps `wait_random` into an `asyncio.Task`. |
| `4-tasks.py` | Tasks, again | `task_wait_n(n, max_delay=10)` is `wait_n` rewritten on top of `task_wait_random`. |

---

## 🚀 Execution & PEP 8 Testing

Each module is a library; test it from a small driver script:

```bash
cat > main.py <<'EOF'
#!/usr/bin/env python3
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
EOF
python3 main.py
```

```bash
pycodestyle 0-basic_async_syntax.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
