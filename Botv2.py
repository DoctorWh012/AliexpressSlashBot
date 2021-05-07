# Imports
import random
import string
from time import sleep
from selenium import webdriver


class Bot:
    def __init__(self):
        self.slash_count = 0
        self.driver_local = "chromedriver.exe"
        self.link_aliexpress = input(str("Link da ajuda: "))

    def bot_Start(self):
        try:
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
            self.driver = webdriver.Chrome(executable_path=self.driver_local,
                                           options=chrome_options)

            # enters on aliexpress create account site
            self.driver.get(
                "https://m.pt.aliexpress.com/login.html?return_url=https%3A%2F%2Fcampaign.aliexpress.com%2Fwow%2Fgcp%2Fslash_it%2Fitembackflow%3FinvitationCode%3DcmdTdkVVaEQ5akc4cFc2RHFBZ3ZVMUtDYzBmZ25xREdNS0xkcy80M3AwNVN2QU8yR2FsRWVBPT0%26percent%3D85.08%26aid%3D3672732325025281%26mid%3D3073668978025281%26srcSns%3Dsns_Copy%26spreadType%3Dinvite%26bizType%3Dslash%26social_params%3D20171963281%26spreadCode%3DcmdTdkVVaEQ5akc4cFc2RHFBZ3ZVMUtDYzBmZ25xREdNS0xkcy80M3AwNVN2QU8yR2FsRWVBPT0%26itemId%3D1005002484068166%26aff_fcid%3D02686fe8906145ee8b786261ab55937a-1620408961375-01950-_mK9dMpb%26tt%3DMG%26aff_fsk%3D_mK9dMpb%26aff_platform%3Ddefault%26sk%3D_mK9dMpb%26aff_trace_key%3D02686fe8906145ee8b786261ab55937a-1620408961375-01950-_mK9dMpb%26shareId%3D20171963281%26businessType%3Dslash%26platform%3DAE%26terminal_id%3D63b3654d8aeb41c4847d38352108c231")

            # creates an account
            butao = self.driver.find_element_by_class_name("next-tabs-tab-inner")
            butao.click()

            email = self.driver.find_element_by_class_name("email")
            email.send_keys(random_email)
            sleep(1)

            senha = self.driver.find_element_by_class_name("password")
            senha.send_keys(random_pass)

            criar_conta = self.driver.find_element_by_class_name("submit")
            criar_conta.click()
            sleep(4)

            # slashes the price
            self.driver.get(f"{self.link_aliexpress}")
            sleep(1.5)
            ajudar = self.driver.find_element_by_class_name("main-action--btnWrap--3H21BlP")
            ajudar.click()
            sleep(2)

            self.slash_count += 1
            print(f"Voce ja ajudou {self.slash_count} vezes!!!")

            # closes the tab
            self.driver.quit()
        except:
            self.driver.quit()


if __name__ == "__main__":
    bot = Bot()
    while True:
        bot.bot_Start()
