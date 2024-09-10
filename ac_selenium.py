from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def switch_to_deepest_iframe(driver):
    while True:
        try:
            iframes = driver.find_elements(By.TAG_NAME, 'iframe')
            if len(iframes) == 0:
                print("No more iframes found")
                break
            print(f"Found {len(iframes)} iframe(s), switching to the first one.")
            driver.switch_to.frame(iframes[0])
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://allstatesugarbowl.org/news/2024/9/9/manning-stars.aspx")
    time.sleep(0.5)
    switch_to_deepest_iframe(driver)
    try:
        colandrea = driver.find_element(By.ID, "1ab96bb1-6eb5-11ef-9287-49c1ce55de26")
        colandrea.click()
        print("clicked")
        time.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")
        return False
    driver.quit()
    return True

if __name__ == '__main__':
    successes = 0
    failures = 0
    start_time = time.time()
    for _ in range(0, 10000):
        try:
            if main():
                successes += 1
            else:
                failures += 1
        except Exception as e:
            print(f"Error: {e}")
            break
        elapsed_time = time.time() - start_time
        print(f"Successes: {successes}")
        print(f"Failures: {failures}")
        print(f"Successes per minute: {successes / elapsed_time * 60}")
        print(f"Total Time: {elapsed_time/60:.2f} minutes")