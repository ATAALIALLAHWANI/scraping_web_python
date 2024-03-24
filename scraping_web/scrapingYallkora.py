import requests
from bs4 import BeautifulSoup
import lxml
import csv

def all_main():
    date = "1/12/2023"
    path = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#days")

    def main(path) :
        src = path.content

        soup = BeautifulSoup(src , "lxml")
        matches_details = []
        matches_all = soup.find_all("div", {'class':'matchCard'})


        def get_match_info(matches_all):
            titel_champ = []
            for i in range(len(matches_all)):
                titel_champ.append(matches_all[i].find("h2").text.strip())

             #get match on the champ
            for   i in range(len(matches_all)):
                allMatch_inchamp = matches_all[i].find_all('li')
                for i in range(len(allMatch_inchamp)):
                    teme_a = allMatch_inchamp[i].find('div', {'class': 'teamA'}).text.strip()
                    teme_b = allMatch_inchamp[i].find('div', {'class': 'teamB'}).text.strip()
                    # get result
                    match_res = allMatch_inchamp[i].find('div', {'class': 'MResult'} ).find_all('span',{'class','score'})
                    score = f"{match_res[0].text.strip()} - {match_res[1].text.strip()}"

                    matches_details.append({"نوع البطولة " : titel_champ[i] , "teama":teme_a , "teamb":teme_b , "score":score})






        get_match_info(matches_all)
        header = matches_details[0].keys()
        print(header)
        with open('D:\scraping web/aa.csv' , 'w') as output_file:
            write_header = csv.DictWriter(output_file , header)
            write_header.writeheader()
            write_header.writerows(matches_details)


            print("dooon")







    main(path)