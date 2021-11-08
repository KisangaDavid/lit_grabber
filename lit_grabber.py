import requests
from bs4 import BeautifulSoup


START_URL = "" # Enter the url for the chapter you want to start from
END_URL = "" # Enter the url for the chapter you want to end on (exclusive)
cur_url = START_URL

while cur_url != END_URL:
    page = requests.get(cur_url)
    soup = BeautifulSoup(page.content, "html.parser")
    summary = soup.find_all("div", class_ = "summary-text readable highlightable-content non-paywall")
    non_paywall_analysis = soup.find_all("div", class_ = "analysis-text highlightable-content non-paywall")
    paywall_analysis = soup.find_all("div", class_ = "analysis-text highlightable-content paywall")
    analysis =  (non_paywall_analysis + paywall_analysis)
    chapter = cur_url.split("/")[-1]
    print(f"{chapter} \n")
    for index, sum_passage in enumerate(summary):
        print(f"Summary: {sum_passage.text} \n Analysis: {analysis[index].text}")
    next = soup.find(class_ = "prev-next-links text-right pull-right next")
    cur_url = "https://www.litcharts.com" + next['href']
