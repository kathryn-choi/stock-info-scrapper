import requests
import datetime
from bs4 import BeautifulSoup
from flask import Flask
import json

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
    stock_info["time"] = datetime.datetime.now()

    kospi_info = dict()
    kospi_info["price"] = soup.select("#KOSPI_now")[0].text
    kospi_fluc = soup.select("#KOSPI_change")[0].text.split("%")[0].split(" ")
    kospi_info["fluc_price"] = deter_incre(kospi_fluc[1]) + kospi_fluc[0].replace("\n","")
    kospi_info["fluc_rate"] = kospi_fluc[1]
    stock_info["KOSPI"] = kospi_info

    kosdaq_info = dict()
    kosdaq_info["price"] = soup.select("#KOSDAQ_now")[0].text
    kosdaq_fluc = soup.select("#KOSDAQ_change")[0].text.split("%")[0].split(" ")
    kosdaq_info["fluc_price"] = deter_incre(kosdaq_fluc[1]) + kosdaq_fluc[0].replace("\n","")
    kosdaq_info["fluc_rate"] = kosdaq_fluc[1]
    stock_info["KOSDAQ"] = kosdaq_info

    kospi200_info = dict()
    kospi200_info["price"] = soup.select("#KPI200_now")[0].text
    kospi200_fluc = soup.select("#KPI200_change")[0].text.split("%")[0].split(" ")
    kospi200_info["fluc_price"] = deter_incre(kospi200_fluc[1]) + kospi200_fluc[0].replace("\n","")
    kospi200_info["fluc_rate"] = kospi200_fluc[1]
    stock_info["KOSPI200"] = kospi200_info

    return json.dumps(stock_info, indent=4, default=str)

if __name__ == '__main__':
    app.run(debug=True)