from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def test_browser(browser_name):
    grid_url = "http://admin:admin@localhost:31444/wd/hub"

    if browser_name == 'chrome':
        options = ChromeOptions()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
    elif browser_name == 'edge':
        options = EdgeOptions()
    else:
        raise ValueError("Unsupported browser: " + browser_name)

    driver = webdriver.Remote(command_executor=grid_url, options=options)

    try:
        driver.get("https://www.google.com")
        print(f"Page title in {browser_name} is:", driver.title)
        assert "Google" in driver.title

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    for browser in ['firefox']:
        test_browser(browser)
