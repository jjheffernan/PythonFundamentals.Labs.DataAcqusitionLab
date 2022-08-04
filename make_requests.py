# import urllib.request
from urllib import request

# using urllib make rest calls to NOAA's API and save the results to json files

# once executed, there should be 39 files.
# JSON objects named 'locations_x.json' numbered 0-38

# Be careful not to overexhaust the allotted calls due to bugs

# URL for calls
url_string = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'


# get URL from input or from file
def call_url(url_string: str):
    # opened specified URL
    # noaa_url = url_string
    request.urlopen(url=url_string)
    # store the url as object


# store json files from specified url
def load_page():
    # load HTML body into list of json objects
    web_data = []  # list of json objects within body


def main():
    # call everything here. This will be accessible via CLI
    # call_url # DO NOT UNCOMMENT UNLESS NO BUGS
    pass


if __name__ == "__main__":
    # CLI call `python3 make_requests.py`
    main()
