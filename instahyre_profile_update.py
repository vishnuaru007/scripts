import requests
import base64
import logging

# Configure logging
logging.basicConfig(
    filename='update_insta.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def fetch_csrf_token(url):
    # Start a session
    session = requests.Session()

    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
    }

    # Send a GET request to the login page with headers
    response = session.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the cookies from the response
        cookies = session.cookies

        # Look for the 'csrftoken' in the cookies
        csrf_token = cookies.get('csrftoken')

        if csrf_token:
            return csrf_token
        else:
            print("CSRF Token not found.")
            return None
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

# URL of the website's login page
url = "https://www.instahyre.com/login/"

# Fetch and return the CSRF token
token = fetch_csrf_token(url)

if token:
    print(f"Fetched CSRF Token: {token}")
else:
    error_message = "Failed to retrieve CSRF Token."
    logging.error(error_message)


crsrfToken = token

sessionId = ''
file_path = "/Users/vishnu.aru/apps/rnd/scripts/python/VishnuAru.pdf"  # Update with the path to your file
login_data = {
    "email": "abc@gmail.com",
    "password": "Hey@1234"
}

cookies = {
    "csrftoken": crsrfToken,
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
    set_cookie_header = response.headers.get('Set-Cookie')
    if set_cookie_header:
        cookies = set_cookie_header.split(',')
        for cookie in cookies:
            if 'sessionid=' in cookie:
                session_id = cookie.strip().split('sessionid=')[1].split(';')[0]
                # break
            if 'csrftoken=' in cookie:
                crsrfToken = cookie.strip().split('csrftoken=')[1].split(';')[0]

        if session_id:
            # print(f"Session ID found : {session_id}")
            # print(f"csrftoken ID found : {crsrfToken}")
            sessionId = session_id.strip()
        else:
            logging.error("Session ID not found in Set-Cookie header.")
    else:
        logging.error("Set-Cookie header not found in the response.")
else:
    print(f"Login Failed: {response.status_code}")
    error_message = f"Login Failed:. Status Code: {response.status_code}. Response Content: {response.text}"    
    logging.error(error_message)

cookies = {
    "csrftoken": crsrfToken,
    "sessionid": sessionId
}
cookie_header = "; ".join([f"{key}={value}" for key, value in cookies.items()])

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
