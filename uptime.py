import requests
import argparse
import time
TOKEN = BOTTOKEN
CHAT_ID =CHAT_ID
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id":CHAT_ID,"text":message}
    try:
        requests.post(url,data=data)
    except Exception as e:
        print(f"{message} not send ",e)
def uptime(url,interval):
    while True:
        try:
            response = requests.get(url,timeout=5)
            if response.status_code != 200:
                send_telegram_message(f"{url} is down with status code {response.status_code} at {time.ctime()}")
        except:
                send_telegram_message(f"{url} is down  at {time.ctime()}")
        time.sleep(int(interval)*60)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor a website with telegram alerts")
    parser.add_argument("url",help = "Specify the url")
    parser.add_argument("-i",default=1,help = "specify the interval to check the website in minutes")
    args=parser.parse_args()
    send_telegram_message(f"Bot set to monitor {args.url}")
    url = f"https://{args.url}"
    uptime(url,args.i)