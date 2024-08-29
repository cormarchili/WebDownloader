import requests

from bs4 import BeautifulSoup


def download_file(url: str, file_name: str):
    """
    Function that downloads and saves the file, which is then moved to its folder.
    Args:
        url: resource URL
        file_name: output filename of the document.
    Returns:
        BufferedWriter: pointer to the output file
    """
    r = requests.get(url)
    file = open(file_name + ".pdf",'wb')
    file.write(r.content)
    file.close()
    return file


def web_scraping(url: str, year: int, page: int, class_type: str):
    """
    Extract the necessary content type from the webpage.
    Args:
        url: the webpage URL
        year: the year of issuing, extracted from the original filename
        page: the corresponding page number for a specific year
        class_type: type of web content downloaded
    Returns:
        bs4.element.ResultSet: the page content
    """
    
    new_url = url + str(year)+'&sort=date&page=' + str(page)
    req = requests.get(new_url)
    soup = BeautifulSoup(req.content, 'html.parser')

    return soup.find_all(class_ = class_type)