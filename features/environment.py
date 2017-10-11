__author__ = 'pioc'

from selenium import webdriver
#from features.steps.browser import Browser
from browser import Browser
from behave import *

def before_all(context):
    print('before all execution')
    context.browser = Browser()

def after_all(context):
    print('finished')
    #context.browser.close()
