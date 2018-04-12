__author__= 'anjali'
import unittest
from selenium import webdriver

class article(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_article(self):
		driver = webdriver.Firefox()
		driver.get("http://10.129.26.119/communities/")
		driver.get("http://10.129.26.119/community-view/8/")
		driver.get("http://10.129.26.119/community-view/8/#")
		driver.get("http://10.129.26.119/forum/forum/buddhist-and-tibetan-art-9/")
		#driver.find_element_by_xpath("//a[@href='/media/community/a38f8eb8-8c10-433a-b1f7-48187b79169b.jpg']").click();
		elem = driver.find_elements_by_class_name("fancybox-button")
		print (elem)
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		