import requests
import json

def download_questions(n_batches=50, questions_per_batch=10):
    all_questions = []
    for i in range(n_batches):
        url = f"https://opentdb.com/api.php?amount={questions_per_batch}&category=9&type=boolean"
        response = requests.get(url)
        data = response.json()
        if "results" in data:
            all_questions.extend(data["results"])
    with open('questions_pool.json', 'w') as f:
        json.dump(all_questions, f)
    print(f"Saved {len(all_questions)} questions.")

download_questions()