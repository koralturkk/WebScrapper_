
class Website():

    def __init__(self,URL: str,name:str, id: str = None, tag_list: str = None, result_class: str = None, tag_title: str = None,
                 tag_company: str = None, tag_location: str = None, title_class: str = None, href: str= None,
                 company_class: str = None, location_class: str = None, tag_link:str = None, title_index: int = 0, location_index: int = 0,
                 company_index: int = 0):

        self.URL = URL
        self.name = name
        self.id = id
        self.tag_list = tag_list
        self.result_class = result_class

        self.tag_title = tag_title
        self.tag_company = tag_company
        self.tag_location = tag_location
        self.title_class = title_class
        self.company_class = company_class
        self.location_class = location_class

        self.title_index = title_index
        self.location_index = location_index
        self.company_index = company_index
        self.href = href
        self.tag_link = tag_link


