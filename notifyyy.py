import notify2
import requests
from bs4 import BeautifulSoup

def coronavirus_detail():
    res = requests.get("https://www.worldometers.info/coronavirus/country/india/")

    soup = BeautifulSoup(res.text, 'html.parser')

    numbers = soup.select('.maincounter-number')

    Total_case = int(str(numbers[0]).split('\n')[1].split(' ')[1].split('>')[-1].replace(',', ''))
    #print (Total_case)
    Death =  int(str(numbers[1]).split('<span>')[1].split("<")[0].replace(',',''))
    #print (Death)
    recovery = int(str(numbers[2]).split('<span>')[1].split("<")[0].replace(',',''))
    #print (recovery)

    return [Total_case, Death, recovery]

def get_notify(t,d,r):
    notify2.init('fullyinform')
    n = notify2.Notification("Crona cases in India",
                            f"Total: {t}\nRecovered: {r}\nActive : {t-r-d}\nDeath: {d}  ",
                            "notification-message-im"   # Icon name
                        )
    n.show()


if __name__ == "__main__":
    t,d,r = coronavirus_detail()
    get_notify(t,d,r)


