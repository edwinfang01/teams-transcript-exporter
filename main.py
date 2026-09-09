import os
import time
import pyclip
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
options.add_argument(f"--user-data-dir={user_data_dir}")

TRANSCRIPT_URL = "https://unibedom-my.sharepoint.com/:v:/r/personal/a_almonte4_prof_unibe_edu_do/Documents/Grabaciones/Inicio%20de%20Clases%20Ingenier%C3%ADa%20de%20Factores%20Humanos-20260908_191212-Meeting%20Recording.mp4?d=wfef65232a6754c97b24611141356e856&csf=1&web=1&e=aoueXT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D"
driver = webdriver.Chrome(options=options)
driver.get(TRANSCRIPT_URL)

def wait_for_element(criteria: tuple[str, str], timeout=5):
    wait = WebDriverWait(driver=driver, timeout=timeout)
    return wait.until(EC.visibility_of_element_located(criteria))

wait_for_element((By.CSS_SELECTOR, "div[class='ms-List-cell']"))
time.sleep(3)

entries = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'entry-')]")
entries_list = []
entries_dict = {}
n_of_entries = len(entries)
last_entry = driver.find_elements(By.CSS_SELECTOR, "*[class*='lastListItem']")

while len(last_entry) == 0 or ( last_entry and len(entries_dict.keys()) < int(last_entry[0].get_attribute("id").strip("listItem-")) ):
    last_entry = driver.find_elements(By.CSS_SELECTOR, "*[class*='lastListItem']")
    if last_entry:
        print(last_entry[0].get_attribute("id").strip("listItem-"), len(entries_dict.keys()), len(entries_dict.keys()) < int( last_entry[0].get_attribute("id").strip("listItem-") ))
    try:
        entries_dict.update(
            {
                int(entry.get_attribute("id").strip("entry-")):
                    {
                        "speaker": entry.get_attribute("aria-label"),
                        "text": entry.find_element(By.CSS_SELECTOR, "div[id^='sub-entry-']").text,
                        "id": int(entry.get_attribute("id").strip("entry-"))
                    }
                for entry in entries if int(entry.get_attribute("id").strip("entry-")) not in entries_dict.keys()
            }
        )
    except StaleElementReferenceException as e:
        print("error: StaleElementReferenceException")

    # driver.find_element(By.CSS_SELECTOR, "div[id^='listItem-']").send_keys(Keys.PAGE_DOWN)

    try:
        # if len(entries_dict.keys()) < 160:
        #     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
        #                           driver.find_element(By.ID, f"entry-{list(entries_dict.keys())[-10]}"))
        #     wait_for_element((By.ID, f"entry-{list(entries_dict.keys())[-10]}"))
        # else:
        driver.find_element(By.CSS_SELECTOR, "div[id^='listItem-']").send_keys(Keys.PAGE_DOWN)

        print(entries_dict.keys())
    except Exception as e:
        print(e)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",driver.find_element(By.ID, f"entry-{list(entries_dict.keys())[-1]}"))
        wait_for_element((By.ID, f"entry-{list(entries_dict.keys())[-1]}"))

    # wait_for_element((By.ID, f"{entries[-1].get_attribute("id")}"))
    entries: list[WebElement] = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'entry-')]")
    current_n_of_entries = len(entries)
    print(f"current_n_of_entries: {current_n_of_entries}, n_of_entries: {n_of_entries}", entries[-1].get_attribute("id"))
    n_of_entries = current_n_of_entries
    # time.sleep(1)

# unique_entries = list({item["id"]: item for item in entries_list}.values())
unique_entries = entries_dict.values()

# transcript_dict = {
#     entry: {
#         "speaker": entry.get_attribute("aria-label"),
#         "text": entry.find_element(By.CSS_SELECTOR, "div[id^='sub-entry-']")
#     }
#     for entry in entries
# }

transcript_string = ""
previous_speaker = ""
for entry in unique_entries:
    # print(entry['id'])
    if previous_speaker != entry['speaker']:
        transcript_string += "\n" + entry['speaker'] + "\n"
    transcript_string += entry['text']
transcript_string = transcript_string.strip()

pyclip.copy(transcript_string)
# print(transcript_string)
