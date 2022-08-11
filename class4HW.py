import requests
import names
from selenium import webdriver
#1
git_repo = requests.get("https://api.github.com/users/avielb/repos")
assert len(git_repo.json()) > 5
#2
name_test = 0
for name in range (3):
    name_req = requests.get(f"https://api.agify.io/?name={names.get_first_name()}")
    if not 0 <= name_req.json()["age"] <= 120:
        name_test = 1
assert name_test == 0
#3
universities = requests.get("http://universities.hipolabs.com/search?country=Israel")
assert len(universities.json()) > 5
#4
y_combinator_test = webdriver.Chrome()
y_combinator_test.get("https://www.ycombinator.com/")
assert y_combinator_test.title == "Y Combinator"
#5
docker_hub_test = webdriver.Chrome()
docker_hub_test.get("https://hub.docker.com/")
assert docker_hub_test.title == "Docker Hub Container Image Library | App Containerization"
