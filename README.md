# Scrap stock info from naver : KOSPI, KOSDAQ, KOSPI200

Scrap KOSPI, KOSDAQ, KOSPI200 from [naver finance](https://finance.naver.com/sise/)
<p align="center">
    <img src="https://user-images.githubusercontent.com/20381868/76387967-567fe080-63ab-11ea-800e-660f788fc145.png" />
</p>

## Result
**curl -X GET 127.0.0.1:5000/api/v1/stock/index**
```angular2html
{
    "time": "2020-03-12 14:57:41.802796",
    "KOSPI": {
        "price": "1,830.92",
        "fluc_price": "-77.35",
        "fluc_rate": "-4.05"
    },
    "KOSDAQ": {
        "price": "566.86",
        "fluc_price": "-28.75",
        "fluc_rate": "-4.83"
    },
    "KOSPI200": {
        "price": "247.13",
        "fluc_price": "-9.88",
        "fluc_rate": "-3.84"
    }
}

```
## How to use
 1. Run ```./venv.sh``` 
 2. Run ```python3 main.py```
 
## Environment
- Python 3.7


