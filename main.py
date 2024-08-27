import requests
import json
allCurrencies=["USD","AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"]
specialNumber=int(input("请输入要搜索的要素数字\n"))
mode=input("请选择搜索方式：\n1.其他币种汇率按美元汇率换算（较快，准确率较低） 2.查询所有币种汇率（较慢，准确率较高）\n")
leastError=[1000000]*len(str(specialNumber))
bestMatch=[None]*len(str(specialNumber))
print("搜索中...")
if mode=='1':
    url="https://api.exchangerate-api.com/v4/latest/USD"
    response=requests.get(url)
    data=response.json()
    for currency in allCurrencies:
        for name in allCurrencies:
            value=data['rates'][name]/data['rates'][currency]
            r=specialNumber%10
            l=int(specialNumber/10)
            cnt=1
            while l!=0:
                if abs(l*value-r)<leastError[cnt]:
                    leastError[cnt]=abs(l*value-r)
                    bestMatch[cnt]=str(l)+currency+"="+str(l*value)+name
                r=r+l%10*10**cnt
                l=int(l/10)
                cnt=cnt+1
if mode=='2':
    for currency in allCurrencies:
        url="https://api.exchangerate-api.com/v4/latest/"+currency
        session=requests.Session()
        response=session.get(url)
        data=response.json()
        for name,value in data['rates'].items():
            r=specialNumber%10
            l=int(specialNumber/10)
            cnt=1
            while l!=0:
                if abs(l*value-r)<leastError[cnt]:
                    leastError[cnt]=abs(l*value-r)
                    bestMatch[cnt]=str(l)+currency+"="+str(l*value)+name
                r=r+l%10*10**cnt
                l=int(l/10)
                cnt=cnt+1
print("最匹配的汇率换算为：")
for i in range(1,len(str(specialNumber))):
    print(bestMatch[i])