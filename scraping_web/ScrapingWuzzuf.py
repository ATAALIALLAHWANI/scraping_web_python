import csv
import itertools

import form as form
import requests
from bs4 import BeautifulSoup




def extraction ():
    job_titles = []
    name_companys = []
    locations_name = []
    job_skillss = []
    for i in range(2):
        path = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={i}")
        src = path.content
        soup = BeautifulSoup(src, "lxml")

        job_title = soup.find_all('h2', {'class': 'css-m604qf'})
        name_company = soup.find_all("a", {"class": "css-17s97q8"})
        location_name = soup.find_all("span", {"class": "css-5wys0k"})
        job_skills = soup.find_all("div", {"class": "css-y4udm8"})
        # get the text form date form for loop

        for i in range(len(job_title)):
            job_titles.append(job_title[i].text.strip())
            name_companys.append(name_company[i].text.strip())
            locations_name.append(location_name[i].text.strip())
            job_skillss.append(job_skills[i].text.strip())

    jobInf = [job_titles, name_companys, locations_name, job_skillss]

    return job_titles



    # creat csv file
    # jobInf = [job_titles , name_companys , locations_name , job_skillss]
    # exported = itertools.zip_longest(*jobInf)
    # with open('D:\scraping web/wuzzuf.csv' , 'w') as output_file:
    #     wr = csv.writer( output_file )
    #     wr.writerow(["job_titale", "company_name" , "location" , "job_skills"])
    #     wr.writerows(exported)













