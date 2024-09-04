import requests
import base64
import logging

# Configure logging
logging.basicConfig(
    filename='update_insta.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

crsrfToken = "HFaJGtQwzlEO3wvXByCHK48kWn9nfGpK0l0cPYQSQbsTNVJNV5O0LjPTZSFJH0iW"
sessionId = "vamb2sqaq16i5ssic0bs5hg3cqh8rqpt"
file_path = "/Users/vishnu.aru/apps/rnd/scripts/python/VishnuAru.pdf"  # Update with the path to your file
login_data = {
    "email": "abc@gmail.com",
    "password": "Hey@1234"
}

cookies = {
    "csrftoken": crsrfToken,
    "_ga": "GA1.2.34600236.1725410623",
    "_gid": "GA1.2.1008061378.1725410631",
    "_gat_UA-45611607-3": "1",
    "_ga_0PQL61K7YN": "GS1.1.1725410623.1.0.1725410631.0.0.0",
    "sessionid": sessionId
}

# Construct the cookie header string
cookie_header = "; ".join([f"{key}={value}" for key, value in cookies.items()])

# Define headers for requests
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "cookie": cookie_header,
    "origin": "https://www.instahyre.com",
    "priority": "u=1, i",
    "referer": "https://www.instahyre.com/login/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-csrftoken": crsrfToken
}

# User login request
login_url = "https://www.instahyre.com/api/v1/user_login"

response = requests.post(login_url, headers=headers, json=login_data)

if response.status_code == 201:
    print("Login Successful")
    # print(response.json())
else:
    print(f"Login Failed: {response.status_code}")
    error_message = f"Failed to update candidate. Status Code: {response.status_code}. Response Content: {response.text}"    
    # Log error to file
    logging.error(error_message)

# Update candidate profile
candidate_update_url = "https://www.instahyre.com/api/v1/candidate_jsp/78962"
candidate_update_data = {
    "id": 78962,
    "total_experience": 6,
    "main_skills": [
        "C",
        "C++",
        "Java"
    ],
    "resource_uri": "/api/v1/candidate_jsp/78962"
}

candidate_update_response = requests.put(candidate_update_url, headers=headers, json=candidate_update_data)

if candidate_update_response.status_code == 200:
    print("Candidate Profile Updated Successfully")
else:
    print(f"Candidate Profile Update Failed: {candidate_update_response.status_code}")
    # print(candidate_update_response.text)
    error_message = f"Failed to update candidate. Status Code: {candidate_update_response.status_code}. Response Content: {candidate_update_response.text}"    
    # Log error to file
    logging.error(error_message)

# Update resume
resume_update_url = "https://www.instahyre.com/api/v1/resume/108736"


with open(file_path, "rb") as file:
    file_b64 = base64.b64encode(file.read()).decode('utf-8')

resume_update_data = {
    "calculate_opps": True,
    "candidate": "/api/v1/limited_candidate/78987",
    "resource_uri": "/api/v1/resume/108736",
    "file_b64": file_b64,
    "title": "VishnuAru.pdf"
}

resume_update_response = requests.put(resume_update_url, headers=headers, json=resume_update_data)

if resume_update_response.status_code == 200:
    print("Resume Updated Successfully")
    # print(resume_update_response.json())
else:
    print(f"Resume Update Failed: {resume_update_response.status_code}")
    # print(resume_update_response.text)
    error_message = f"Failed to update candidate. Status Code: {resume_update_response.status_code}. Response Content: {resume_update_response.text}"    
    # Log error to file
    logging.error(error_message)
