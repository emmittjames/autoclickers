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

def click_on_ac(driver):
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    time.sleep(1)
    switch_to_deepest_iframe(driver)
    try:
        colandrea = driver.find_element(By.ID, "1ab96bb1-6eb5-11ef-9287-49c1ce55de26")
        colandrea.click()
        print("clicked")
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    successes = 0
    failures = 0
    start_time = time.time()

    driver.get("https://allstatesugarbowl.org/news/2024/9/9/manning-stars.aspx")
    time.sleep(1)
    for _ in range(0, 1000):
        if click_on_ac(driver):
            successes += 1
        else:
            failures += 1
        print(f"Successes: {successes}, Failures: {failures}")
        print(f"Successes per minute: {successes / ((time.time() - start_time) / 60)}")
        print(f"Elapsed time: {(time.time() - start_time) / 60} minutes")

    driver.quit()
    return True

if __name__ == '__main__':
    main()