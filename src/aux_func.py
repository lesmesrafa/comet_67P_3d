import pathlib
import urllib.request
import os
import polars as pl
from PyQt5.QtWidgets import QWidget, QHBoxLayout


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

        

def obj2df(data_dir: str,  col_names: list[str]) -> pl.DataFrame:
    """
    Converts a whitespace-separated values file to a Polars DataFrame.

    This function reads a file from the specified directory, processes each line to remove
    unnecessary whitespaces and newline characters, converts numeric values to floats, and
    finally compiles the cleaned data into a Polars DataFrame with specified column names.

    Parameters:
    - data_dir (str): The path to the data file that needs to be processed. The file should
      contain whitespace-separated values with each line representing a record.
    - col_names (list[str]): A list of column names for the resulting DataFrame. The number
      of column names provided should match the number of fields in each line of the file.

    Returns:
    - pl.DataFrame: A Polars DataFrame containing the processed data from the file. Each column
      in the DataFrame corresponds to one of the specified column names.

    Note:
    - The first element of each line in the file is treated as a non-numeric value and is not
      converted to float. All subsequent elements are converted to floats.
    - It is assumed that the last element of each cleaned list may have a newline character
      which is stripped during processing.
    - The function uses Polars (imported as `pl`) for creating the DataFrame. Ensure Polars
      is installed and imported correctly in your environment.
    """
    file_lines = []
    with open(data_dir, "r") as file:
        
        for line in file: 
            line = line.split(" ")    
            cleaned_list = [item for item in line if item != '']

            if cleaned_list[-1].endswith('\n'):
                cleaned_list[-1] = cleaned_list[-1].rstrip('\n')

            cleaned_list = [elem if idx == 0 else float(elem) for idx, elem in enumerate(cleaned_list)]
            file_lines.append(cleaned_list)


    return pl.DataFrame(file_lines, schema = col_names)


class MainViewPanel(QWidget):
    """
    MainViewPanel is a custom QWidget that integrates a plotting figure
    using the specified backend for visualizations, and sets up the layout
    and appearance of the main view panel.

    This class creates a figure using the backend specified by
    `vv.backends.backend_pyqt5.Figure`, places it within a horizontal layout,
    and sets the window title. It's designed to serve as the main panel for
    displaying visualizations in a PyQt5 application, specifically tailored
    for showing Rosetta-related data.

    Attributes:
    - fig: A figure object created using the visualization backend, which is
      intended to hold the plots or visualizations.
    - sizer: A QHBoxLayout instance used to manage the layout of widgets in the
      panel, specifically arranging the figure widget within the panel.

    Parameters:
    - *args: Variable length argument list passed to the QWidget constructor.
             This allows for customization and flexibility in initializing the
             QWidget base class.

    Note:
    - The class is dependent on the `vv.backends.backend_pyqt5` module for
      creating the figure, which should be part of the visualization library
      you're using. Ensure this backend is correctly installed and available.
    - The `show()` method is called at the end of the initialization to
      automatically display the widget upon creation. This behavior can be
      adjusted if deferred display is preferred.
    """
    def __init__(self, *args) -> None: 
        QWidget.__init__(self, *args)
        selfr.fig = vv.backends.backend_pyqt5.Figure(self)
        self.sizer = QHBoxLayout(self)
        self.sizer.addWidget(self.fig._widget)
        self.setLayout(self.sizer)
        self.setWindowTitle("Rosetta")
        self.show()