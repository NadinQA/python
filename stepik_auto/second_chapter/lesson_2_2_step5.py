from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 100);")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView(true);
button.click()