from selenium import webdriver
import random,time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()



#The easiest way to hide the browser is to install PhantomJS.
#driver = webdriver.PhantomJS()

url = "https://www.facebook.com/profile.php?id=100009281652810"
user_email = 'user'
user_pass = 'pass'
waitTime = 10


class fbReportUserProfile:

	def __init__(self, driver,url,email,password):
		self.driver = driver
		self.url = url
		self.email = email
		self.password = password

	def navigate(self,url):
		self.driver.get(url)

	def login(self,email,password,driver):
		try:
			emailelement = self.driver.find_element_by_name('email')
			passwordelement = self.driver.find_element_by_name('pass')
			emailelement.send_keys(self.email)
			passwordelement.send_keys(self.password)

			#logging in to the facebook using Selenium
			emailelement.send_keys(Keys.RETURN)

		except Exception as inst:
			print type(inst)     # the exception instance
			print inst.args      # arguments stored in .args
			print inst 
			print "Please check your credential again."

'''
	def browserWaitUntilForConditon(self,driver,time):
		try:
			element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, "events_birthday_view")))
		except:
			print "Couldn't find birthday page, Please check the url"
			driver.quit()
'''

#Navigating to the url
fbReportUserProfile = fbReportUserProfile(driver,url,user_email,user_pass)
fbReportUserProfile.navigate(url)

# Logging in facebook by using email and password
fbReportUserProfile.login(user_email,user_pass,driver)
#facebookBirthdayWishes.browserWaitUntilForConditon(driver,waitTime)

time.sleep(10)
driver.find_element_by_xpath("//*[@id=\"u_0_10\"]/i").click()
driver.find_element_by_xpath("//*[@id=\"u_0_y\"]/div/ul/li[2]/a/span/span").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"nfxQuestionNamedaccount\"]/label[1]").click()
driver.find_element_by_xpath("//*[@id=\"nfx_dialog_continue\"]").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"nfxQuestionNamedfake\"]/label[1]").click()
driver.find_element_by_xpath("//*[@id=\"nfx_dialog_continue\"]").click()

time.sleep(2)
elemFound = driver.find_element_by_xpath("//a[@href='#'][@rel='async-post']")
ActionChains(driver).click(elemFound).perform()





