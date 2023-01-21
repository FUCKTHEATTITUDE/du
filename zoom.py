import time
import warnings
import threading
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec



proxylist = [
    "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
   "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",
]

warnings.filterwarnings('ignore')
fake = [
'David Asir',
'Mohammed UAE',
'Victor Sam',
'SENTHILKUMAR DUBAI',
'Tamilarasan',
'NAWAZ KHALEEL',
'Samimii',
'PEER MOHAMMAD',
'L Krishnakumar',
'Yuvanathan',
'MANJU',
'Muthubabu',
'Christopher Asir Dass',
'KITTY',
'Prabhakar',
'Neranjan',
'Muralidhar',
'S ANANYA',
'Anushka',
'Devi Gayathri',
'Divya shree',
'Imarankhan',
'Jasmine Stella',
'Jayaraman',
'Jhansi *Crypto*',
'KAVITHA R',
'Khanchana',
'Kavya Kumar',
'Malathi',
'Panneer Selvam',
'Sumathi Arun',
'Mayadevi',
'Meeramadavan',
'Navyasundar',
'Nila guru',
'Priyadhrasini',
'Ganesamoorthi',
'Gurugularaman',
'Ramamoorthy',
'Sivabalan',
'Siva subramanian',
'Kumaresan',
'Rojamuthu',
'Sanvikabalu',
'Sathyanarayanan',
'gopalakrishnan',
'Sita Narayanan',
'Williams',
'Veerakumar',
'Zahara beevi',
'Kumaravel',
'Shanthinathan',
'Hariharan',
'AMSAVENI',
'Darshan',
'SK Lakshana ',
'Alagarsamy',
'BABU KV',
'Elangovan',
'Rajan',
'Prashanth',
'Palanisamy',
'poovithan',
'Akashaya',
'Mithilesh ',
'Nithish Sai Ram',
'Ramasubbu',
'Sam Daniel ',
'Arul Edwin Prabhakar ',
'Sridevi S',
'Mohammad Nadeem',
'Gnanam',
'Farhan',
'Rassul Haris',
'Ashok kumar',
'Nagaraj covai',
'Saatvika',
'Krishna Kumar',
'Yuvaraj',
'Varundev',
'Vishnu shastri',
'tharun',
'Sam Paul',
'Venkat subramanian',
'Vivesh Balan',
'Kapilan R',
'Vetrivel',
'Abhishek E',
'Divyesh Narayanan',
'Gokul L',
'Srinanthan',
'Preethi Sundar',
'Kavinraj',
'Subhash',
'Sabarimathan',
'DAYANITHI',
'Essaki Subbiah',
'Pradeep Kumar',
'Pranav Suresh',
'Mosas ',
'Varshan',
'Raj nagul',
'Dinesh Kumar ',
'Tharul Krishna',
'Asvin Karthick',
'kishore',
'Manikandan',
'Sai pranav',
'Sundaresan',
'Ruthran',
'BalajiKumar',
'Harshan',
'Sanjeev',
'Selvaraj',
'R.K.vinoth',
'Tamilprasath',
'Uthayasuriya',
'Veeramani',
'Giriraj',
'Kanmani',
'Meenakumari',
'Kayalabbas',
'Chockalingam',
'Srinivasagam',
'Murugavel',
'Chandrasekaran',
'Petchikumar',
'Haja Modieen',
'Rangasamy',
'Mohandas',
'Subramani',
'Jabber basha',
'Thabasuraj',
'Dhamodharan',
'Madhan',
'Nageswaran',
'Queensly',
'Xavier Sam',
'Vellammal',
'Vellaismy',
'Jacob',
'Thalavai Sundram',
'Chiranjeevi',
'Deviprasad',
'Dhanasingh',
'DHIVAKAR',
'GEMINI',
'Eknath',
'Govardhan',
'Govindaraj',
'Guru Prasad',
'Hemanth',
'Jeeva Arun',
'jawahar',
'Kailash',
'KapilDev',
'Karunakaran',
'Keeethivasan',
'Laxman',
'Kuberan',
'Mithiran',
'Prasanna Kumar',
'Premrajasingh',
'Ramprasad',
'Rahul Saran',
'Rohith',
'Sachin',
'Sai Shankar',
'Koothai',
'Sooraj',
'Yuvan',
'Vishva',
'Uma Rani',
'Vamsikrishna',
'k Sripathi',
'Kaarthika ',
'Kavitha',
'komalavalli',
'Krija Vaithiyanathan',
'Khushboo',
'KULANTHIVEL',
'Ramya',
'Rajeswari',
'RAMANI',
'ranjitha',
'Revathi',
'Rosanna',
'Wajeeha',
'Nagalakshmi',
'NADHIYA',
'Nalini',
'Neelaveni',
'Sudhan Veluchamy',
'Parvathi',
'Padmapriya',
'Panimalar',
'Priyadhrasini',
'Priyanka',
'Pradiksha',
'Boobalan Relanak',
'Tamaraiselvi',
'Mala Shankar',
'Maruthupaniyan',
'Mathumitha',
'Padmavathi']

MUTEX = threading.Lock()


def sync_print(text):
    with MUTEX:
        print(text)



def get_driver(proxy):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    if proxy is not None:
        options.add_argument(f"--proxy-server={proxy}")
    driver = webdriver.Chrome('chromedriver', options=options)
    return driver


def driver_wait(driver, locator, by, secs=1, condition=ec.element_to_be_clickable):
    wait = WebDriverWait(driver=driver, timeout=secs)
    element = wait.until(condition((by, locator)))
    return element


def start(name, proxy, wait_time):
    sync_print(f"{name} started!")
    driver = get_driver(proxy)
    driver.get(f'https://dulink.in/r1uux')
    time.sleep(15)
    btn2 = driver.find_element(By.ID, 'btn3')
    btn2.click()
    time.sleep(20)
    btn3 = driver.find_element(By.ID, 'btn6')
    time.sleep(1)
    btn3.click()
    sync_print(f"{name} sleep for {wait_time} seconds ...")
    time.sleep(wait_time)
    sync_print(f"{name} ended!")


def main():
    wait_time = sec * 60
    workers = []
    for i in range(number):
        try:
            proxy = proxylist[i]
        except IndexError:
            proxy = None
        try:
            proxy = None
        except IndexError:
            break
        wk = threading.Thread(target=start, args=(
            f'[Thread{i}]', proxy, wait_time))
        workers.append(wk)
    for wk in workers:
        wk.start()
    for wk in workers:
        wk.join()


if __name__ == '__main__':
    number = int(input("Enter number of Users: "))
    sec = 20
    main()
