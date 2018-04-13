__author__= 'anjali'
import unittest
from selenium import webdriver



class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user="liken"
		pwd= "coolguyss"
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.find_element_by_xpath('//a[@href="/login/?next=/"]').click()
		print ("driver.current_url>>>>>>"+driver.current_url)
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a[@href="/communities/"]').click()
		print ("driver.current_url>>>>>>"+driver.current_url)
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		print ("driver.current_url>>>>>>"+driver.current_url)
		driver.find_element_by_xpath('//a[@href="/group-view/1/"]').click()
		print ("driver.current_url>>>>>>"+driver.current_url)
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		print ("driver.current_url>>>>>>"+driver.current_url)
		

	def tearDown(self):
	    self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		