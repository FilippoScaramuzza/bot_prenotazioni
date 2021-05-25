from webbot import Browser
from time import sleep
import getpass


email = input("E-MAIL: ")
pwd = getpass.getpass("PASSWORD: ")
mat_pome = input("MATTINA o POMERIGGIO? (M o P): ")
date = input("DATA (dd/mm/aaaa): ").replace("/", "")

"""
email = input("E-MAIL: ")
pwd = input("PASSWORD: ")
mat_pome = input("MATTINA(M) o POMERIGGIO(P)?")
date = input("DATA (dd/mm/aaaa): ").replace("/", "")
"""

driver = Browser()
driver.go_to('https://biblioteche.parma.it/SebinaOpac/dashboard/')
driver.click('ACCEDI')
driver.click(id="login-ateneo")
driver.type(email, id="username")
driver.type(pwd, id="password")
driver.click("Accesso")
driver.click("statusbar-select-btn")
driver.click(id="statusbar-select-btn")
driver.click("Appuntamenti")
driver.click("Prendi un nuovo appuntamento")
sleep(1)
driver.click(id="select2-prop-container")
driver.type("Ingegneria")
driver.press(driver.Key.ENTER)
driver.press(driver.Key.ESCAPE)
driver.click("Posto in Sala Studio Grande (" + "MATTINA" if mat_pome == "M" else "POMERIGGIO" + ")")
driver.scrolly(5)
sleep(1)
driver.click(xpath='//*[@id="dashboard"]/div/form[2]/fieldset/label[1]/input')
driver.press(driver.Key.LEFT)
driver.type(date)
sleep(1)
driver.click(xpath='//*[@id="dashboard"]/div/form[2]/fieldset/label[2]/input')
driver.press(driver.Key.LEFT)
driver.type(date)
driver.click("CERCA")

confirmed = False
while not confirmed:
    try:
        sleep(5)
        driver.click("CONTINUA")
        driver.driver.find_element_by_xpath('//*[@id="calendario"]/table/tbody/tr/td[6]/select')
        print("FOUND!")
        confirmed = True
    except:
        driver.click("CERCA")
        print("NOT FOUND")

sleep(1)
driver.click("1")
driver.click("INSERISCI")
