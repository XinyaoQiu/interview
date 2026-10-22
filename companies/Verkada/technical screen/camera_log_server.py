"""
Problem: Camera Log API Server

Implement three APIs using two shared blocking queues:
- poll_command: wait for a command from the user.
- get_log: enqueue a command, then wait for the camera's logs.
- send_log: simulate a 5-second delay, then enqueue the logs.

Assumptions to confirm with the interviewer:
- There is one camera. Concurrent HTTP requests are allowed, but get_log
  processes one complete request at a time using a lock.
- The camera sends exactly one complete log batch per command, possibly empty.
- JSON bodies are valid. Built-in blocking queues are allowed.
- Polling uses long polling; the camera calls again after handling a command.
- Use one process with multiple threads. The camera eventually responds.
- Timeouts, retries, authentication, and persistence are outside this version.

Hold request_lock from command submission until logs arrive. Other get_log
calls wait for the lock, so only one request can consume the shared log queue.
Neither poll_command nor send_log acquires this lock: they must be able to
run while get_log is waiting. No request IDs or per-request queues are needed.

Run tests: python camera_log_server_test.py
Run server: flask --app camera_log_server run --with-threads
Dependency: Flask
"""

from queue import Queue
from threading import Lock
from time import sleep

from flask import Flask, request


app = Flask(__name__)
command_queue = Queue()
log_queue = Queue()
request_lock = Lock()


@app.get("/poll_command")
def poll_command():
    return command_queue.get()


@app.get("/get_log")
def get_log():
    with request_lock:
        command_queue.put({"command": "get_log"})
        return {"logs": log_queue.get()}


@app.post("/send_log")
def send_log():
    logs = request.get_json()["logs"]
    sleep(5)  # Simulate a delay before delivering the logs.
    log_queue.put(logs)
    return {"status": "ok"}
