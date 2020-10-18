from selenium import webdriver
browser=webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
browser.get('https://www.facebook.com/')


user_id=input('Enter User Id of your Fb Account :')  
password=input('Enter the password :')


print(user_id)
print(password)