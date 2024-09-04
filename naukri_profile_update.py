import requests
import random
import datetime
import logging


# Configure logging
logging.basicConfig(
    filename='update_nauk_profile.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# log_file = '/Users/vishnu.aru/apps/rnd/scripts/python/update_profile.log'

USER_NAME = "abc@gmail.com"
PASS = "Hey@1234"
PROFILE_ID = "8336d8bece6b87e8216532adb1974f84915606f69e528a9ef79fd6c296adc7b6"
NO_YR_EXP = 5
NO_MONTH_EXP = 6
RESUME_PATH = "/Users/vishnu.aru/apps/rnd/scripts/python/VishnuAru.pdf"
FILE_NAME = "VishnuAru.pdf"
RESUME_ID = PROFILE_ID

# with open(log_file, 'a') as f:
#     f.write(f'Cron job executed at: {datetime.datetime.now()}\n')

# Step 1: Perform login to get the nauk_at token
login_url = "https://www.naukri.com/central-login-services/v1/login"
login_headers = {
    "accept": "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "appid": "103",
    "cache-control": "no-cache",
    "clientid": "d3skt0p",
    "content-type": "application/json",
    "origin": "https://www.naukri.com",
    "priority": "u=1, i",
    "referer": "https://www.naukri.com/",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "systemid": "jobseeker"
}

login_data = {
    "username": USER_NAME,
    "password": PASS
}

login_response = requests.post(login_url, headers=login_headers, json=login_data)

# Extract cookies as a dictionary
cookies = login_response.cookies.get_dict()
print("Logged in successfully!")

# Extract specific cookies
unid = cookies.get("MYNAUKRI[UNID]")
nkwap = cookies.get("NKWAP")
nauk_at = cookies.get("nauk_at")
nauk_rt = cookies.get("nauk_rt")
nauk_sid = cookies.get("nauk_sid")

# print("unid:", unid)
# print("nkwap:", nkwap)
# print("nauk_at:", nauk_at)
# print("nauk_rt:", nauk_rt)
# print("nauk_sid:", nauk_sid)

# Construct the Cookie header
cookie_header = (
    f"MYNAUKRI[UNID]={unid}; "
    f"NKWAP={nkwap}; "
    f"nauk_at={nauk_at}; "
    f"nauk_rt={nauk_rt}; "
    f"nauk_sid={nauk_sid}"
)

# Function to determine experience_month randomly
def get_random_experience_month():
    return random.choice([NO_MONTH_EXP, NO_MONTH_EXP+1])

if nauk_at:
    # Step 2: Use the nauk_at token in the authorization header of the next request
    profile_url = "https://www.naukri.com/cloudgateway-mynaukri/resman-aggregator-services/v1/users/self/fullprofiles"
    profile_headers = {
        "Cookie": cookie_header,
        "accept": "application/json",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "appid": "103",
        "cache-control": "no-cache",
        "clientid": "d3skt0p",
        "content-type": "application/json",
        "origin": "https://www.naukri.com",
        "referer": "https://www.naukri.com/",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "systemid": "jobseeker",
        "x-http-method-override": "PUT",
        "authorization": f"Bearer {nauk_at}",
    }

    # Update profile payload
    update_payload = {
        "profile": {
            "experience": {
                "year": NO_YR_EXP,
                "month":  get_random_experience_month()
            }
        },
        "profileId": PROFILE_ID
    }

    try:
        profile_response = requests.post(profile_url, headers=profile_headers, json=update_payload)

        if profile_response.status_code == 200:
            print("Profile updated successfully!")
            # print(profile_response.json())
        else:
            print(f"Failed to update profile. Status code: {profile_response.status_code}")
            print(f"Response: {profile_response.text}")
            error_message = f"Failed to update profile. Status Code: {profile_response.status_code}. Response Content: {profile_response.text}"    
            # Log error to file
            logging.error(error_message)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
else:
    print("Failed to retrieve nauk_at token from login response.")


def upload_file_and_update_resume(file_path, file_name, form_key, file_key, upload_callback, resume_id, bearer_token):
    # First CURL request to upload the file
    file_upload_url = 'https://filevalidation.naukri.com/file'
    file_upload_headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'appid': '105',
        'origin': 'https://www.naukri.com',
        'priority': 'u=1, i',
        'referer': 'https://www.naukri.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'systemid': 'fileupload',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        "Cookie": cookie_header
    }
    
    file_upload_data = {
        'formKey': form_key,
        'fileName': file_name,
        'uploadCallback': upload_callback,
        'fileKey': file_key
    }


    file_upload_files = {
        'file': (file_name, open(file_path, 'rb'))
    }

    # Sending the file upload request
    response_upload = requests.post(file_upload_url, headers=file_upload_headers, data=file_upload_data, files=file_upload_files)
    
    if response_upload.status_code == 200:
        print("File uploaded successfully!")
    else:
        print(f"Failed to upload the file: {response_upload.status_code} - {response_upload.text}")
        error_message = f"Failed to upload the file. Status Code: {response_upload.status_code}. Response Content: {response_upload.text}"    
        # Log error to file
        logging.error(error_message)
        return
    

    update_resume_url = f'https://www.naukri.com/cloudgateway-mynaukri/resman-aggregator-services/v0/users/self/profiles/{resume_id}/advResume'
    update_resume_headers = {
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'appid': '105',
        'authorization': f'Bearer {bearer_token}',
        'content-type': 'application/json',
        'Cookie': cookie_header,
        'x-http-method-override': 'PUT',
        'x-requested-with': 'XMLHttpRequest',
        'appid': '105',
        'systemid': '105',
    }

    file_update_data= {
        "textCV": {
            "formKey": form_key,
            "fileKey": file_key,
            "textCvContent": ''
        }
    }

    # Sending the update resume request
    response_update = requests.post(update_resume_url, headers=update_resume_headers, json=file_update_data)

    if response_update.status_code == 200:
        print("Resume updated successfully!")
    else:
        print(f"Failed to update the resume: {response_update.status_code} - {response_update.text}")
        error_message = f"Failed to update the resume. Status Code: {response_update.status_code}. Response Content: {response_update.text}"    
        logging.error(error_message)



# Example usage
upload_file_and_update_resume(
    file_path = RESUME_PATH,
    file_name = FILE_NAME,
    form_key="F51f8e7e54e205",
    file_key="UINS8kbTUvgWsR",
    upload_callback="true",
    resume_id= RESUME_ID,
    bearer_token= nauk_at
)