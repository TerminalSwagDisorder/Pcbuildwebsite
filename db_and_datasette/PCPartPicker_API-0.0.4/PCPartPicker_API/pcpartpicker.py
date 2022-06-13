from json import loads as jsonloads
from ._pages_data import lookup
from bs4 import BeautifulSoup
from requests import get

base_url = "https://pcpartpicker.com"

def set_region(region):
    global base_url
    if region in ["au", "be", "ca", "de", "es", "fr", "in", "ie", "it", "nz", "uk", "us"]:
        base_url = "https://" + ((region + ".") if region != "us" else "") + "pcpartpicker.com"
    else:
        raise ValueError("region not supported")

class lists(object):
    """
    For scraping product lists such as
    https://pcpartpicker.com/products/cpu-cooler/
    """

    @staticmethod
    def _get_page(part_type, page_num, return_max_pagenum=False):
        if part_type not in lookup:
            raise ValueError("part_type invalid")
        r = get(base_url + "/products/" + part_type + "/fetch?page=" + str(page_num))
        parsed = jsonloads(r.content.decode("utf-8"))
        if return_max_pagenum:
            return parsed["result"]["paging_data"]["page_blocks"][-1]["page"]
        return BeautifulSoup(parsed["result"]["html"], "html.parser")
    
    @staticmethod
    def total_pages(part_type):
        """
        returns the total number of pages for $part_type
        """
        return lists._get_page(part_type, 1, True)

    @staticmethod
    def get_list(part_type, page_num=0):
        """
        returns results for $page_num
        if $page_num left to default, get all pages
        """
        if page_num == 0:
            start_page_num, end_page_num = 1, lists.total_pages(part_type)
        else:
            start_page_num, end_page_num = page_num, page_num

        parsed_html = []
        for page_num in range(start_page_num, end_page_num+1):
            soup = lists._get_page(part_type, page_num)
            for row in soup.find_all("tr"):
                row_elements = {}
                for count, value in enumerate(row):
                    text = value.get_text().strip()

                    if count in lookup[part_type]:
                        row_elements[lookup[part_type][count]] = text
                    elif count == 1:
                        row_elements["name"] = text
                    elif count == len(row)-2:
                        row_elements["price"] = text
                    elif count == len(row)-3:
                        row_elements["ratings"] = text.replace("(", "").replace(")", "")
                    else:
                        try:
                            if value.a["class"] == ["btn-mds", "pp_add_part"]:
                                row_elements["id"] = value.a["href"].replace("#", "")
                        except TypeError:
                            pass  # Not <a> tag
                        except KeyError:
                            pass  # No class

                parsed_html.append(row_elements)
        return parsed_html
