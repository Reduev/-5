import random
from pathlib import Path

directory = Path("/home/user/random_files")

directory.mkdir(parents=True, exist_ok=True)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

created_files = []

for _ in range(10):
    filename = ''.join(random.choice(chars) for _ in range(8)) + ".txt"

    file_path = directory / filename

    file_path.touch()
    created_files.append(file_path)

for file_path in created_files:
    print(file_path.absolute())