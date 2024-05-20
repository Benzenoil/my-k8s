from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def test_browser():
    grid_url = "http://admin:admin@localhost:31444/wd/hub"

    options = FirefoxOptions()
    driver = webdriver.Remote(command_executor=grid_url, options=options)

    try:
        driver.get("https://www.google.com")
        print(f"Page title is:", driver.title)
        assert "Google" in driver.title
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_browser()
