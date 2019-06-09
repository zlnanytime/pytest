import requests
import bs4
from multiprocessing import Pool
import json
import time

url_root='https://blog.csdn.net/yxp20092010/article/details/51174871'

def geturl(num):
    return url_root + str(num);
def geturls(num):
    return map(geturl,)