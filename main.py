import pymysql
import requests
import time
import datetime
from bs4 import BeautifulSoup

def deter_incre(cur_rate):
    if "+" in cur_rate:
        return "+"
    else:
        return "-"

def insert_db(table_name, scrap_time, price, _fluc_rate, _fluc_price):
    try:
        # create sql
        sql = "insert into %s " \
              "(saved_date, price, fluc_rate, fluc_price) " \
              "value ('%s', '%s', '%s','%s') " % (table_name, scrap_time, price, _fluc_rate, _fluc_price)

        # execute sql
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print("ERROR : insert ",table_name)


if __name__ == '__main__':
    conn = pymysql.connect(host="127.0.0.1",
                            port=3306,
                            user="",
                            password="",
                            db="stock",
                            charset="utf8")

    cursor = conn.cursor()

    response = requests.get("https://finance.naver.com/sise/")
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    while(1):
        scrap_time = datetime.datetime.now()
        if scrap_time.minute % 5 == 0:
            stock_time = soup.select("#time3")[0].text
            if "장중" in stock_time:
                kospi_price = soup.select("#KOSPI_now")[0].text
                kosdaq_price = soup.select("#KOSDAQ_now")[0].text
                kospi200_price = soup.select("#KPI200_now")[0].text

                kospi_fluc = soup.select("#KOSPI_change")[0].text.split("%")[0].split(" ")
                kosdaq_fluc = soup.select("#KOSDAQ_change")[0].text.split("%")[0].split(" ")
                kospi200_fluc = soup.select("#KPI200_change")[0].text.split("%")[0].split(" ")

                kospi_fluc_price = deter_incre(kospi_fluc[1]) + kospi_fluc[0].replace("\n","")
                kosdaq_fluc_price = deter_incre(kosdaq_fluc[1]) + kosdaq_fluc[0].replace("\n","")
                kospi200_fluc_price = deter_incre(kospi200_fluc[1]) + kospi200_fluc[0].replace("\n","")

                insert_db("KOSPI", scrap_time, kospi_price, kospi_fluc[1], kospi_fluc_price)
                insert_db("KOSDAQ", scrap_time, kosdaq_price, kosdaq_fluc[1], kosdaq_fluc_price)
                insert_db("KOSPI200", scrap_time, kospi200_price, kospi200_fluc[1], kospi200_fluc_price)
            time.sleep(60)