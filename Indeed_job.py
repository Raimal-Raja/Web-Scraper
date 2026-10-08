import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from urllib.parse import urlencode

def export(results):
    df = pd.DataFrame(results)
    if not results:
        return
    output = Path("Job_results.csv")
    df.to_csv(output, mode="a", index=False,
              header=not output.exists() or output.stat().st_size == 0)
def scrape_job():
    job_search="DevOps Engineer"
    base_url = "https://pk.indeed.com/"
    #https://pk.indeed.com/jobs?q=DevOps+Developer&l=&vjk=233c36b6a375b745
    url = base_url + "jobs?" + urlencode({"q": job_search, "l": ""})
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, timeout=30)
    response.raise_for_status()
    bs = BeautifulSoup(response.text, "html.parser")
    job_list = bs.find('ul', {'class':'css-zu9cdh'})
    if job_list is None:
        raise RuntimeError("No job list found. The page may be blocked or its markup may have changed.")
    # print(job_list)
    jobs = job_list.find_all('div', {'class': 'job_seen_beacon'})
    info =[]
    # print(jobs)
    for job in jobs:
        TITLE = job.find('h2', {'class':'jobTitle'})
        if TITLE is None or TITLE.find('a') is None:
            continue
        title = TITLE.get_text(strip=True)
        
        link = TITLE.find('a').get('data-jk')
        if not link:
            continue
        # print(link, title)
        url = base_url + "viewjob?" + urlencode({"jk": link})
        company = job.find('span', {'class':'css-63koeb'})
        location = job.find('div', {'class': "company_location"})
        company_name = company.get_text(strip=True) if company else ""
        company_location = location.get_text(strip=True) if location else ""
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
