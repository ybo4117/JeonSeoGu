from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import time



# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def population(request):
    options = wd.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    driver = wd.Chrome(r'C:\Project\JeonSeoGu\chromedriver.exe', options=options)
    driver.implicitly_wait(3)

    driver.get('https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3&conn_path=I2')
    driver.find_element_by_css_selector('li#tabClassText_1.menu_off').click()
    driver.find_element_by_css_selector('input#classLvlAllChk1_1').click()
    driver.find_element_by_css_selector('input#classChkLi1_1_47').click()
    driver.find_element_by_css_selector('input#classChkLi1_1_27').click()
    driver.find_element_by_xpath('//ul[@id="classList1_1"]/li[16]/a').click()
    driver.find_element_by_css_selector('input#classChk1_2').click()
    driver.find_element_by_xpath('//ul[@id="classList1_1"]/li[4]/a').click()
    time.sleep(1)
    driver.find_element_by_css_selector('input#classChk1_2').click()
    driver.find_element_by_css_selector('img#searchImg1').click()

    #address = driver.page_source

    time.sleep(2)
    #parse = bs(address, 'html.parser')
    THead1 = driver.find_elements_by_css_selector('table#mainTableT > thead > tr > th.colHead-first')
    THead1h = []
    TBody1 = driver.find_elements_by_css_selector('table#mainTable > tbody > tr > td')
    TBody1h = []

    #th_list = parse.select('#mainTableT thead tr th')
    for th1 in THead1:
        THead1h.append(th1.text)

    for tb1 in TBody1:
        TBody1h.append(tb1.text)
   

    crawling_list ={
                    'THead1h':THead1h[:3],
                    'TBody1h1':TBody1h[:10],
                    'TBody1h2':TBody1h[10:20],
                    'TBody1h3':TBody1h[20:30],
                    'TBody1h4':TBody1h[30:40],
                    'TBody1h5':TBody1h[40:50],
                    'TBody1h6':TBody1h[50:60],
                    'TBody1h7':TBody1h[60:70],
                    'TBody1h8':TBody1h[70:80],
                    'TBody1h9':TBody1h[80:90],
                    'TBody1h10':TBody1h[90:100],
                    'TBody1h11':TBody1h[100:110],
                    'TBody1h12':TBody1h[110:120],
                    'TBody1h13':TBody1h[120:130],
                    'TBody1h14':TBody1h[130:140],
                    'TBody1h15':TBody1h[140:150],
                    'TBody1h16':TBody1h[150:160],
                    'TBody1h17':TBody1h[160:170],
                    'TBody1h18':TBody1h[170:180],
                    'TBody1h19':TBody1h[180:190],
                    'TBody1h20':TBody1h[190:200],
                    'TBody1h21':TBody1h[200:210],
                    'TBody1h22':TBody1h[210:220],
                    'TBody1h23':TBody1h[220:230],
                    'TBody1h24':TBody1h[230:240],
                    'TBody1h25':TBody1h[240:250],
                    'TBody1h26':TBody1h[250:260],
                    'TBody1h27':TBody1h[260:270],
                    'TBody1h28':TBody1h[270:280],
                    'TBody1h29':TBody1h[280:290],
                    'TBody1h30':TBody1h[290:300],
                    'TBody1h31':TBody1h[300:310],
                    'TBody1h32':TBody1h[310:320],
                    'TBody1h33':TBody1h[320:330],
                    'TBody1h34':TBody1h[330:340],
                    'TBody1h35':TBody1h[340:350],

                    }

    return render(request, 'population.html', crawling_list)

def work(request):
    options = wd.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    driver = wd.Chrome(r'C:\Project\JeonSeoGu\chromedriver.exe', options=options)
    driver.implicitly_wait(3)

    driver.get('https://kosis.kr/statHtml/statHtml.do?orgId=383&tblId=DT_38301_2013_N1021&vw_cd=MT_ZTITLE&list_id=383_38301_004&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE')
    driver.find_element_by_css_selector('li#tabClassText_1.menu_off').click()
    driver.find_element_by_css_selector('input#classLvlAllChk1_1').click()
    driver.find_element_by_css_selector('input#classChkLi1_1_101').click()
    driver.find_element_by_css_selector('input#classChkLi1_1_100').click()
    #driver.find_element_by_css_selector('li#tabTimeText.menu_off').click()
    #driver.find_element_by_xpath('//h2[@class="top"]/select[@class="box"]/option[@value="201901"]').click()
    driver.find_element_by_css_selector('img#searchImg1').click()

    time.sleep(2)

    THead1 = driver.find_elements_by_css_selector('table#mainTableT > thead > tr > th')
    THead1h = []
    TBody1 = driver.find_elements_by_css_selector('table#mainTable > tbody > tr > td')
    TBody1h = []

    for th1 in THead1:
        THead1h.append(th1.text)

    for tb1 in TBody1:
        TBody1h.append(tb1.text)

    crawling_list ={
                    'THead1h1':THead1h[1:2],
                    'THead1h2':THead1h[2:3],
                    'TBody1hT1':TBody1h[:1],
                    'TBody1hT2':TBody1h[9:10],
                    'TBody1h1':TBody1h[1:5],
                    'TBody1h2':TBody1h[10:14],
                    'TBody1h3':TBody1h[5:9],
                    'TBody1h4':TBody1h[14:18],
                    }
    return render(request, 'work.html', crawling_list)

def corona(request):
    address = 'http://www.gb.go.kr/Main/open_contents/section/wel/page.do?mnu_uid=5857&LARGE_CODE=360&MEDIUM_CODE=90&SMALL_CODE=10&mnu_order=2'
    res = requests.get(address)
    res.encoding = 'utf-8'

    result = res.text
    parse = bs(result, 'html.parser')

    THead = []
    TBody = []
    TBody2 = []
    TBody3 =[]
    dt_list = parse.select('#content .city_corona dt')
    dd_list = parse.select('#content .city_corona dd strong')
    dd_list2 = parse.select('#content .city_corona dd span')
    tb2_list = parse.select('#content .tbl_st1 tbody td')

 
    for dt in dt_list:
        THead.append(dt.get_text())

    for dd in dd_list:
        TBody.append(dd.get_text())


    for d2 in dd_list2:
        TBody2.append(d2.get_text())

    for tb2 in tb2_list:
        TBody3.append(tb2.get_text())


    crawling_list ={
                    'THead':THead[:12],
                    'TBody':TBody[:12],
                    'TBody2':TBody2[:12],
                    'THead_2':THead[12:],
                    'TBody_2':TBody[12:],
                    'TBody2_2':TBody2[12:],
                    'TBody3':TBody3[:11],
                    'TBody3_2':TBody3[11:],
                    }

    return render(request, 'corona.html', crawling_list)

def news(request):
    address = 'http://www.gb.go.kr/Main/open_contents/section/wel/page.do?mnu_uid=5865&LARGE_CODE=360&MEDIUM_CODE=90&SMALL_CODE=90&mnu_order=2'
    res = requests.get(address)
    res.encoding = 'utf-8'

    result = res.text
    parse = bs(result, 'html.parser')
    table_list = parse.select('#content .bodlist_wrap .b_subject a')
    page = []
    for tb in table_list:
        tb = str(tb)
        pg =tb[:9]+"http://www.gb.go.kr/Main/open_contents/section/wel"+tb[10:]
        page.append(pg)
        
    table = { 'table': page }
    return render(request, 'news.html', table)