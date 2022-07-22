from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import threading
from ..serializers import *
def try_element(driver,element):
     while(True):
        try:
            ActionChains(driver).move_to_element(element).click().perform()
            break
        except:
            time.sleep(1)

def list_str(lis):
    q=[]
    for i in range(len(lis)):
        q.append(lis[i].text.strip())
    return q


def commentgathering(link,pk):
    numpage=5
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    element=driver.find_element("xpath","//a[@data-hook = 'see-all-reviews-link-foot']")
    try_element(driver,element)
    page_reviews=[]
    i=0
    while i<numpage:
        i=i+1
        content = driver.page_source
        soup = BeautifulSoup(content)
        page_review = list_str(soup.find_all(attrs={"data-hook":"review-body"}))
        for comment in page_review:
            data={"comment":comment,"address":pk}
            serializer = Comment_serial(data=data)
            print(f"HERE {comment} {data}")
            serializer.is_valid(raise_exception=True)
            serializer.save()
        while(True):
            try:
                element=driver.find_element("xpath","//*[text()='Next page']")
                break
            except:
                time.sleep(1)
        try_element(driver,element)


class myThread (threading.Thread):
    def __init__(self, link,pk):
        threading.Thread.__init__(self)
        self.link = link
        self.pk = pk
    def run(self):
        print(f'I am {self.link} {self.pk}')
        commentgathering(self.link,self.pk)
