# Scrap stock info from naver : KOSPI, KOSDAQ, KOSPI200

Scrap KOSPI, KOSDAQ, KOSPI200 info from [naver finance](https://finance.naver.com/sise/)
<p align="center">
    <img src="https://user-images.githubusercontent.com/20381868/76387967-567fe080-63ab-11ea-800e-660f788fc145.png" />
</p>

## Result
**curl -X GET 127.0.0.1:5000/api/v1/stock/index**
```angular2html
{
    "msg": "OK",
    "data": {
        "last_updated": "2020-03-17 12:12:13",
        "KOSPI": {
            "price": "1,675.38",
            "fluc_price": "-39.48",
            "fluc_rate": "-2.30",
            "individual": "+2,802",
            "foreign": "-3,912",
            "institutional": "+933"
        },
        "KOSDAQ": {
            "price": "505.88",
            "fluc_price": "+1.37",
            "fluc_rate": "+0.27",
            "individual": "-2,406",
            "foreign": "+1,800",
            "institutional": "+594"
        },
        "KOSPI200": {
            "price": "227.66",
            "fluc_price": "-5.31",
            "fluc_rate": "-2.28",
            "individual": "+2,802",
            "foreign": "-3,912",
            "institutional": "+982"
        }
    },
    "ret_code": 0
}


```
## How to use
 1. Run ```./venv.sh``` 
 2. Run ```python3 main.py```
 
## Environment
- Python 3.7


