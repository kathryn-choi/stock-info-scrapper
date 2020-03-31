import requests
import datetime
from bs4 import BeautifulSoup
from flask import Flask, request
import json
from selenium import webdriver
import re

app = Flask(__name__)

def deter_incre(cur_rate):
    if "+" in cur_rate:
        return "+"
    else:
        return "-"

@app.route("/api/v1/stock/index")
def scrap_info():
    response = requests.get("https://finance.naver.com/sise/")
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    stock_info = dict()
    stock_info["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    kospi_info = dict()
    kospi_info["price"] = soup.select("#KOSPI_now")[0].text
    kospi_fluc = soup.select("#KOSPI_change")[0].text.split("%")[0].split(" ")
    kospi_info["fluc_price"] = deter_incre(kospi_fluc[1]) + kospi_fluc[0].replace("\n","")
    kospi_info["fluc_rate"] = kospi_fluc[1]
    kospi_info["individual"] = soup.select("#tab_sel3_deal_trend > li.c2 > span.val > em")[0].text
    kospi_info["foreign"] = soup.select("#tab_sel3_deal_trend > li.c3 > span.val > em")[0].text
    kospi_info["institutional"] = soup.select("#tab_sel1_deal_trend > li.c4 > a > span.val> em")[0].text
    stock_info["KOSPI"] = kospi_info

    kosdaq_info = dict()
    kosdaq_info["price"] = soup.select("#KOSDAQ_now")[0].text
    kosdaq_fluc = soup.select("#KOSDAQ_change")[0].text.split("%")[0].split(" ")
    kosdaq_info["fluc_price"] = deter_incre(kosdaq_fluc[1]) + kosdaq_fluc[0].replace("\n","")
    kosdaq_info["fluc_rate"] = kosdaq_fluc[1]
    kosdaq_info["individual"] = soup.select("#tab_sel2_deal_trend > li.c2 > a > span.val > em")[0].text
    kosdaq_info["foreign"] = soup.select("#tab_sel2_deal_trend > li.c3 > a > span.val > em")[0].text
    kosdaq_info["institutional"] = soup.select("#tab_sel2_deal_trend > li.c4 > a > span.val > em")[0].text
    stock_info["KOSDAQ"] = kosdaq_info

    kospi200_info = dict()
    kospi200_info["price"] = soup.select("#KPI200_now")[0].text
    kospi200_fluc = soup.select("#KPI200_change")[0].text.split("%")[0].split(" ")
    kospi200_info["fluc_price"] = deter_incre(kospi200_fluc[1]) + kospi200_fluc[0].replace("\n","")
    kospi200_info["fluc_rate"] = kospi200_fluc[1]
    kospi200_info["individual"] = soup.select("#tab_sel3_deal_trend > li.c2 > span.val > em")[0].text
    kospi200_info["foreign"] = soup.select("#tab_sel3_deal_trend > li.c3 > span.val > em")[0].text
    kospi200_info["institutional"] = soup.select("#tab_sel3_deal_trend > li.c4 > span.val > em")[0].text
    stock_info["KOSPI200"] = kospi200_info

    result = dict()
    result["msg"] = "OK"
    result["data"] = stock_info
    result["ret_code"] = 0
    return json.dumps(result, indent=4)


@app.route("/api/v1/info")
def code_based_scrap():
    code = request.args.get('code')
    url = "https://finance.daum.net/quotes/A"+code+"#analysis/main"
    finance_table = "https://wisefn.finance.daum.net/v1/company/cF1001.aspx?cmp_cd="+code+"&amp;finGubun=MAIN"

    stock_info = dict()

    driver = webdriver.Chrome("/Users/Kathryn/downloads/chromedriver")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name = soup.select("#favorite")[0].text
    stock_info["name"] = re.findall("[가-힣]+", name)[0]
    pbr = soup.select("#boxDashboard > div > div > span.txtB > dl > dd:nth-child(10) > p")[0].text
    stock_info["pbr"] = pbr.split("(")[0].split("/")[1]
    driver.close()

    driver = webdriver.Chrome("/Users/Kathryn/downloads/chromedriver")
    driver.get(finance_table)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name_list = soup.select("#cTB26 > tbody > tr.row1 > th")
    table_content = soup.select("#cTB26 > tbody > tr.row10 > td > span")
    driver.close()

    liability_info = dict()
    for i in range(len(name_list)):
        key = name_list[i].text.split("(")[0]
        if i < 4:
            liability_info[key + "y"] = table_content[i].text
        else:
            liability_info[key + "p"] = table_content[i].text

    stock_info["liability"] = liability_info
    result = dict()
    result["msg"] = "OK"
    result["data"] = stock_info
    result["ret_code"] = 0
    return json.dumps(result, indent=4,ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)