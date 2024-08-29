import tqdm
import yaml
from utils.common import append_name, check_if_downloaded, check_if_written, create_folder, create_year_file
from utils.scraping import download_file, web_scraping


pages = {
    1906 : list(range(0,7)),
    1907 : list(range(0,6)),
}

def run_downloader(url: str, year: int, download_uri: str, source_type: str):

    for j in tqdm.tqdm(pages[year]):
        content = web_scraping(url, str(year), str(j), "item-img")
        for c in content:
            retrieved_string = str(c)
            if retrieved_string.__contains__(source_type):
                title = retrieved_string.split(source_type)[1].split('" style=')[0]
                name = title.split('manshu-nippo-')[1]
                year = name.split('.')[0]
                month = name.split('.')[1].split('.')[0]
                if(check_if_downloaded(year, month, (name + ".pdf"))):
                    check_if_written(year, name)
                else:
                    new_uri = download_uri + title + '/'+ name +'.pdf'
                    file = download_file(new_uri, name)
                    create_folder(year, month, file.name)
                    append_name(year, name)
            else:
                print("Requested content is not available at this URL.")


if __name__ == "__main__":

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    for year in pages.keys():
        create_year_file(year)
        run_downloader(
            url=config["URL"], 
            year=year, 
            download_uri=config["DOWNLOAD_URI"], 
            source_type=config["SOURCE_TYPE"]
        )