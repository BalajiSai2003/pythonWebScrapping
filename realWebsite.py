from bs4 import BeautifulSoup
import requests
import time
print("put some skills that your are not familiar with")
unfamiliar_skill=input(">")
print(f"Filtering out {unfamiliar_skill}")
def find_jobs(fileName):
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    # print(html_text)
    soup=BeautifulSoup(html_text,"lxml")
    jobsAvail= soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
    s=""
    for jobs in jobsAvail:
        publish_date = jobs.find("span", class_="sim-posted").span.text
        if publish_date=="Posted today" or publish_date=="Posted few days ago"  :
            company_name = jobs.find("h3", class_="joblist-comp-name").text.replace(" ", "").rstrip().lstrip()
            skills = jobs.find('span', class_="srp-skills").text.replace(" ", "").rstrip().lstrip()
            more_info=jobs.header.h2.a["href"]
            if unfamiliar_skill not in skills or unfamiliar_skill=="":
                s=s+f'''
Company Name: {company_name}
skills: {skills}
More Info: {more_info}
                '''
                print(f"file saved: {fileName}")
    with open(f"posts\{fileName}.txt", 'w') as fi:
        fi.write(s)
        fi.close()

if __name__=="__main__":
    i=1
    while True:
        find_jobs(str(i))
        time_wait=10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)
        i=i+1
