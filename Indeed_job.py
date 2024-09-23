import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

def export(results):
    df = pd.DataFrame(results)
    df.to_csv("Job_results.csv", mode="a", index=False, header=True)
def scrape_job():
    job_search="DevOps Engineer"
    base_url = "https://pk.indeed.com/"
    #https://pk.indeed.com/jobs?q=DevOps+Developer&l=&vjk=233c36b6a375b745
    url = base_url+f"jobs?q={job_search}&l=&vjk=233c36b6a375b745"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    job_list = bs.find('ul', {'class':'css-zu9cdh'})
    # print(job_list)
    jobs = job_list.find_all('div', {'class': 'job_seen_beacon'})
    info =[]
    # print(jobs)
    for job in jobs:
        TITLE = job.find('h2', {'class':'jobTitle'})
        title = TITLE.text
        
        link = TITLE.find('a').attrs['data-jk']
        # print(link, title)
        url = f'https://pk.indeed.com/viewjob?cmp=A-Bit-Much-SME-Private-Limited&t=Devops+Engineer&jk=858e369d2568bf2d&xpse=SoBI67I37HxBaqA4Pb0LbzkdCdPP&xfps=76ffd32e-72cd-4d3f-ac6e-3f175db56e07&xkcb=SoCR67M37HfysSgKVb0LbzkdCdPP&vjs=3'
        company_name = job.find('span', {'class':'css-63koeb'}).text
        company_location = job.find('div',{'class': "company_location"}).text
        data = {
            'title': title,
            'company name':company_name,
            'company location':company_location,
            'job url':url
        }
        info.append(data)
    export(info)
        
        # print(title, company_name, company_location, url)
    
if __name__ =="__main__": 
    scrape_job()