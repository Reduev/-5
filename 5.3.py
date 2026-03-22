import random
import json
import string

user_data = {
    "name": f"{random.choice(['John', 'Alice', 'Bob', 'Mary', 'Charlie'])} {random.choice(['Doe', 'Smith', 'Johnson', 'Brown', 'Davis'])}",
    "age": random.randint(18, 80),
    "email": f"{random.choice(['john', 'alice', 'bob', 'mary', 'charlie'])}.{random.choice(['doe', 'smith', 'johnson', 'brown', 'davis'])}@example.com",
    "password": ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
}

with open('user_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(user_data, json_file, ensure_ascii=False, indent=4)

with open('user_data.json', 'r', encoding='utf-8') as json_file:
    loaded_user_data = json.load(json_file)
    print(json.dumps(loaded_user_data, indent=4, ensure_ascii=False))