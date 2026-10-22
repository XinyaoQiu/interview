"""Print tests for serialized requests and the real 5-second upload delay."""

from concurrent.futures import ThreadPoolExecutor, TimeoutError
from time import monotonic

from camera_log_server import app


app.testing = True


def get(path):
    with app.test_client() as client:
        response = client.get(path)
        return response.status_code, response.get_json()


def upload(logs):
    with app.test_client() as client:
        response = client.post("/send_log", json={"logs": logs})
        return response.status_code, response.get_json()


with ThreadPoolExecutor(max_workers=4) as pool:
    first_user = pool.submit(get, "/get_log")
    first_camera = pool.submit(get, "/poll_command")
    print(first_camera.result(timeout=10))  # (200, {'command': 'get_log'})

    # The second user must wait before publishing another command.
    second_user = pool.submit(get, "/get_log")
    second_camera = pool.submit(get, "/poll_command")
    try:
        second_camera.result(timeout=0.2)
        print("Second command blocked:", False)
    except TimeoutError:
        print("Second command blocked:", True)

    start = monotonic()
    first_upload = pool.submit(upload, ["first request logs"])
    try:
        first_user.result(timeout=0.2)
        print("First user waits for upload:", False)
    except TimeoutError:
        print("First user waits for upload:", True)

    print(first_upload.result(timeout=10))  # (200, {'status': 'ok'})
    print("Upload took at least 5 seconds:", monotonic() - start >= 5)
    print(first_user.result(timeout=10))  # (200, {'logs': ['first request logs']})

    # Only now can the second command be delivered.
    print(second_camera.result(timeout=10))  # (200, {'command': 'get_log'})
    print("Second user still waiting:", not second_user.done())  # True
    print(upload([]))  # (200, {'status': 'ok'})
    print(second_user.result(timeout=10))  # (200, {'logs': []})
