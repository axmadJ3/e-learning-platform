import requests


username = ''
password = ''


base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'
available_courses = []


while url is not None:
    print(f'Loading courses from {url}')
    r = requests.get(url)
    response = r.json()
    url = response['next']
    courses = response['results']
    available_courses += [course['title'] for course in courses]

print(f'Available courses: {", ".join(available_courses)}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/',
        # replace the username and password variables with existing user or load from env
        auth=(username, password)
    )
    if r.status_code == 200:
        print(f'Succssesfully enroled in {course_title}')
