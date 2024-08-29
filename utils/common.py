import os


def check_if_downloaded(year: int, month: int, name: str):
    """
    Function that checks if a file is present in the corresponding year and month folder.
    Args:
        year: the year of issuing, extracted from the original filename
        month: the month of issuing, extracted from the original filename
        filename: the original name of the file.
    Returns:
        bool: is the file is present in the directory
    """
    if(year in os.listdir() and month in os.listdir(str(year))):
        return name in os.listdir(str(year)+'/'+str(month))


def create_folder(year: int, month: int, filename: str):
    """
    Function that, given a year, a month and a filename, checks if the year/month folders exist and saves the file accordingly.
    When downloading a new year, the function creates both the year and month folder.
    When downloading a new month, it creates the nested month folder. 
    Then, it saves the file in the new path (/year/month/filename) and appends the filename in the file containing all the filenames of the year.
    Args:
        year: the year of issuing, extracted from the original filename
        month: the month of issuing, extracted from the original filename
        filename: the original name of the file.
    Returns:
        None
    """
    if not(year in os.listdir()):
        os.mkdir(str(year))

    if not(month in os.listdir(str(year))):
        os.mkdir(str(year)+'/'+str(month))

    new_path = str(year)+ '/' +str(month) + '/'+ filename
    os.rename(filename, new_path)


def create_year_file(year: int):
    """
    Function that creates the file containing the list of downloaded files for a specific year.
    Args:
        year: the year of issuing, extracted from the original filename
    Returns:
        None
    """
    if(not os.path.exists(str(year)+'.txt')):
        list_files_year = open(str(year) + ".txt",'w')
        list_files_year.close()

def append_name(year: int, name: str):
    """
    Function that appends the new file name to the file containing the list of the already downloaded files of the year.
    Args:
        year: the year of issuing, extracted from the original filename
        name: the original name of the downloaded file.
    Returns:
        None
    """
    year_file = open(str(year) + ".txt",'a')
    year_file.write(name + '\n')
    year_file.close()


def check_if_written(year: int, name: str):
    """
    Function that checks if a specific file has already been downloaded (therefore, its name is written in the file of the corresponding year)
    Args:
        year: the year of issuing, extracted from the original filename
        name: the original name of the downloaded file.
    """
    year_file = open(str(year) + ".txt", 'r')
    if not(name+'\n') in year_file:
        append_name(year, name)
        return False
    else:
        year_file.close()
    
    return True

