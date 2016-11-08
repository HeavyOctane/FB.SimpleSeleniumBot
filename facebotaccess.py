#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import tkinter as tk
import smtplib
from tkinter import * 
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from tkinter import Tk, Label, Button, StringVar
from gi.repository import Notify


window1 = Tk()
window1.title("LOGIN")
img = PhotoImage(file='favicon.gif')
window1.tk.call('wm','iconphoto', window1._w,img)

def acceder():
	print ("Sent")
	with open(".secure.txt", "w") as text_file:
		print(E1.get(),E2.get(), file=text_file)
		window1.quit()

L1 = Label(window1, text="User")
L1.grid(row=0, column=0)
E1 = Entry(window1, bd =8)
E1.grid(row=0, column=1)
L2 = Label(window1, text="Password")
L2.grid(row=1, column=0)
E2 = Entry(window1, bd =8, show="·")
E2.grid(row=1, column=1)
MyButton1 = Button(window1, text="Login", width=10, command=acceder)
MyButton1.grid(row=3, column=1)
window1.mainloop()

E1u = E1.get()
E2p = E2.get()
# FOR USE WITH FIREFOX DRIVER, IF AVAILABLE
#driver = webdriver.Firefox()
#driver.get("http://www.facebook.com")

# FOR USE WITH CHROME DRIVER, GIVEN THAT SINCE THE LAST UPDATE, FIREFOX HAS BEEN UNUSABLE
driver =  webdriver.Chrome('/home/david/custommodules/chromedriver')
driver.get("http://www.facebook.com")
print ("Opened facebook...")
a = driver.find_element_by_id('email')
a.send_keys(E1u)
print ("Email Id entered...")
b = driver.find_element_by_id('pass')
b.send_keys(E2p)
print ("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()

Notify.init("App Name")
Notify.Notification.new("Login Successful").show()

post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Greetings______Testing using Selenium.")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
#post_it.click()
print ("Posted...")
Notify.init("App Name")
Notify.Notification.new("Posted Successful").show()
