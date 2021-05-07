# Imports
import random
import string
from time import sleep
from selenium import webdriver

# slash count, chromedriver local and link input
slash_count = 0
driver_local = "chromedriver.exe"

# Loop
while True:
    # prints how many times you slashed
    slash_count += 1
    print(f"Voce ja ajudou {slash_count} vezes!!")

    # creates random email
    email_len = random.randrange(9, 15)
    random_email = "".join(random.choice(string.ascii_letters) for i in range(email_len))
    random_email += "@gmail.com"
    print(f"email random: {random_email}")

    # creates random pass
    random_pass = "".join(random.choice(string.ascii_letters) for x in range(email_len))
    print(f"senha random: {random_pass}")

    # set chrome to mobile mode
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19"}
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=driver_local,
                              options=chrome_options)

    # enters on aliexpress create account site
    driver.get("https://login.aliexpress.com/")

    # creates an account
    butao = driver.find_element_by_class_name("next-tabs-tab-inner")
    butao.click()
    email = driver.find_element_by_class_name("email")
    email.send_keys(random_email)
    sleep(1)
    senha = driver.find_element_by_class_name("password")
    senha.send_keys(random_pass)
    criar_conta = driver.find_element_by_class_name("submit")
    criar_conta.click()
    sleep(4)

    # slashes the price
    driver.get(f"https://a.aliexpress.com/_mK9dMpb")
    sleep(1.5)
    ajudar = driver.find_element_by_class_name("main-action--btnWrap--3H21BlP")
    ajudar.click()
    sleep(2)

    # closes the tab
    driver.quit()
