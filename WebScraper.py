
import requests, pprint
from bs4 import BeautifulSoup

from Website import Website

### Things to do
###-----------------
### Make it applicable to static websites (Done!)
### Customize search query
### Make it applicable to dynamic websites
### Make it applicable to hidden websites
### Build commandline app



monster_website = Website(URL="https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia",
                          name="Monster", id="ResultsContainer",tag_list="section", result_class="card-content",
                          tag_title="h2", tag_company="div", tag_location="div", title_class="title", company_class="company", tag_link="a",href="href",
                          location_class="location",title_index=0, location_index=0,company_index=0)

pythonjobs_website = Website(URL="http://pythonjobs.github.io/",
                          name="Pythonjobs", id="content",tag_list="div", result_class="job",
                          tag_title="h1", tag_company="span", tag_location="span", title_class=None, company_class="info", tag_link="a", href="href",
                          location_class="info",title_index=0, location_index=0,company_index=3)

indeed_website = Website(URL="https://au.indeed.com/jobs?q=software+engineer&l=Australia",
                          name="Indeed", id="resultsCol",tag_list="div", result_class="jobsearch-SerpJobCard",
                          tag_title="div", tag_company="span", tag_location="span", title_class="title", company_class="company", tag_link="a",href="href",
                          location_class="location accessible-contrast-color-location",title_index=0, location_index=0,company_index=0)

website_list = [monster_website,pythonjobs_website,indeed_website]



def listJobs(website_list, job_title = None, location= None):

    for website in website_list:
        page = requests.get(website.URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if website is not None:
            print("\n", "--------Jobs Listings for {name}--------".format(name=website.name), "\n")

            id = website.id
            tag_list = website.tag_list
            result_class = website.result_class

            tag_title = website.tag_title
            tag_company = website.tag_company
            tag_location = website.tag_location
            title_class = website.title_class
            company_class = website.company_class
            location_class = website.location_class

            title_index= website.title_index
            location_index = website.location_index
            company_index = website.company_index

        else:
            continue

        results = soup.find(id=id)
        job_elems = results.find_all(tag_list, class_=result_class)


        if results is None or job_elems is None:
            raise ValueError("Missing or Unmatching Values -> Check for updates on websites")

        for job_elem in job_elems:


            title_elem = job_elem.find_all(tag_title, class_=title_class)
            company_elem = job_elem.find_all(tag_company, class_=company_class)
            location_elem = job_elem.find_all(tag_location, class_=location_class)

            if len(title_elem) > 0:
                print(title_elem[title_index].text.strip())

            if len(company_elem) > 0:
                print(company_elem[company_index].text.strip())

            if len(location_elem) > 0:
                print(location_elem[location_index].text.strip())

            print("")


def linksForKeyword(website_list, search: str):

    if type(search) is not str:
        raise TypeError("You should input a string of text argument")

    for website in website_list:

        page = requests.get(website.URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if website is not None:

            print("\n", "--------Links for {name}--------".format(name=website.name), "\n")

            id = website.id
            tag_title = website.tag_title
            tag_link = website.tag_link
            href = website.href
        else:
            continue

        results = soup.find(id=id)

        jobs = results.find_all(tag_title, string=lambda text: search in text.lower() if text is not None else "")

        for p_job in jobs:
            link = p_job.find(tag_link)[href]
            print(p_job.text.strip())

            if website.name == "Pythonjobs":
                print("Apply here: http://pythonjobs.github.io{}\n".format(link))
            elif website.name == "Indeed":
                print("Apply here: https://au.indeed.com/{}\n".format(link))
            else:
                print("Apply here: {}\n".format(link))


    print("--------End of Search--------")




listJobs(website_list)

linksForKeyword(website_list, "developer")