
import requests, pprint
from bs4 import BeautifulSoup

static_URLs = {"monster": "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia",
               "pythonjobs": "http://pythonjobs.github.io/",
               "indeed": "https://au.indeed.com/jobs?q=software+engineer&l=Australia"
               }


### Things to do
###-----------------
### Make it applicable to static websites (Done!)
### Customize search query
### Make it applicable to dynamic websites
### Make it applicable to hidden websites
### Build commandline app




def listJobs(URL_dict, job_title = None, location= None):

    for name, URL in URL_dict.items():

        print("\n","--------Jobs Listings for {name}--------".format(name=name),"\n")
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if name == "monster":
            id = "ResultsContainer"
            tag_list = "section"
            result_class = "card-content"

            tag_title = "h2"
            tag_company = "div"
            tag_location = "div"
            title_class = "title"
            company_class = "company"
            location_class = "location"

            title_index= 0
            location_index = 0
            company_index = 0

        elif name == "pythonjobs":
            id ="content"
            tag_list = "div"
            result_class = "job"

            tag_title = "h1"
            tag_company = "span"
            tag_location = "span"
            title_class = None
            company_class = "info"
            location_class = "info"

            title_index= 0
            location_index = 0
            company_index = 3

        elif name == "indeed":
            id = "resultsCol"

            tag_list = "div"
            result_class = "jobsearch-SerpJobCard"

            tag_title = "div"
            title_class = "title"

            tag_company = "span"
            company_class = "company"

            tag_location = "span"
            location_class = "location accessible-contrast-color-location"

            title_index = 0
            location_index = 0
            company_index = 0

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


def linksForKeyword(URL_dict, search: str):

    if type(search) is not str:
        raise TypeError("You should input a string of text argument")

    for name, URL in URL_dict.items():

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if name == "monster":
            print("\n", "--------Links for {name}--------".format(name=name), "\n")
            id = "ResultsContainer"
            h = "h2"
            element = "a"
            attribute = "href"

        else:
            continue

        results = soup.find(id=id)

        python_jobs = results.find_all(h, string=lambda text: search in text.lower())

        for p_job in python_jobs:
            link = p_job.find(element)[attribute]
            print(p_job.text.strip())
            print("Apply here: {}\n".format(link))


    print("--------End of Search--------")

listJobs(static_URLs)
