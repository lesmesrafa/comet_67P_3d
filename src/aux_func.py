import pathlib
import urllib.request
import os


def download_file(dl_path, dl_url):
    """
    download_file(DL_PATH, DL_URL)

    This helper function supports one to download files from the Internet and
    stores them in a local directory.

    Parameters
    ----------
    DL_PATH : str
        Download path on the local machine, relative to this function.
    DL_URL : str
        Download url of the requested file.
    """

    
    file_name = dl_url.split('/')[-1]


    pathlib.Path(dl_path).mkdir(parents=True, exist_ok=True)

    # If the file is not present in the download directory -> download it
    if not os.path.isfile(dl_path + file_name):
        urllib.request.urlretrieve(dl_url, dl_path + file_name)
