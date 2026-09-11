import os
import time
from pathlib import Path
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

TRANSCRIPT_URL = "your teams transcript url"
FILE_NAME = "your transcript file name"
SAVE_PATH = Path(rf"the path where you want to save your file eg. C:\Users\username\Downloads") / f"{FILE_NAME}.txt"
driver = webdriver.Chrome(options=options)
driver.get(TRANSCRIPT_URL)

def wait_for_element(criteria: tuple[str, str], timeout=20):
    wait = WebDriverWait(driver=driver, timeout=timeout)
    return wait.until(EC.element_to_be_clickable(criteria))

wait_for_element((By.CSS_SELECTOR, "div[class='ms-List-cell']"))
# time.sleep(3)

entries = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'entry-')]")
entries_dict = {}
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
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, "div[id^='listItem-']").send_keys(Keys.PAGE_DOWN)

        print(entries_dict.keys())
    except Exception as e:
        print(e)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",driver.find_element(By.ID, f"entry-{list(entries_dict.keys())[-1]}"))
        wait_for_element((By.ID, f"entry-{list(entries_dict.keys())[-1]}"))

    # wait_for_element((By.ID, f"{entries[-1].get_attribute("id")}"))
    entries: list[WebElement] = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'entry-')]")
    print(f"current_n_of_entries: {len(entries_dict)}", entries[-1].get_attribute("id"))
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

with open(SAVE_PATH, "w", encoding="utf-8") as file:
    file.write(transcript_string)
