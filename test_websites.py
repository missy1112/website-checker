from selenium import webdriver
import time

# Read URLs
with open("urls.txt", "r") as file:
    urls = file.readlines()

driver = webdriver.Chrome()

results = []

for url in urls:
    url = url.strip()
    print(f"Testing: {url}")

    try:
        driver.get(url)
        time.sleep(3)

        if driver.title:
            print(f"PASS: {url}")
            results.append((url, "PASS"))
        else:
            print(f"FAIL: {url}")
            results.append((url, "FAIL"))

    except Exception as e:
        print(f"ERROR: {url}")
        results.append((url, "ERROR"))

driver.quit()

print("\nRESULTS:")
for r in results:
    print(r)
