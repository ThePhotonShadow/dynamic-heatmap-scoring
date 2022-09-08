import pandas
import geopandas
import geopy
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter


def parse_excel_address_columns(filepath: str, column_names: list, api_key: str):
    """Takes an Excel file with one or more address columns and returns a data_frame with a latitude and longitude
    for each entry. Requires a Bing geocoding api key"""
    data_frame = pandas.read_excel(filepath)

    if len(column_names) > 1:
        data_frame["complete_address"] = ""
        for column_name in column_names:
            data_frame["complete_address"] = data_frame["complete_address"] + data_frame[column_name]
    else:
        data_frame.rename(columns={column_names[0]: "complete_address"})

    locator = geopy.Bing(api_key=api_key)
    data_frame['point'] = data_frame["complete_address"].apply(locator.geocode)\
        .apply(lambda loc: tuple(loc.point) if loc else None)
    data_frame[['latitude', 'longitude', 'altitude']] = pd.DataFrame(
        data_frame["point"].tolist(),
        index=data_frame.index
    )

    return data_frame

def score_point(latitude: float, longitude: float, ):
    """Returns a suitability value score for a geographic point weighted by the euclidian distance
    and number of units at sale locations"""
    """To-do: Probably too expensive to do API calls for driving distance rather than 
    straight-line distances"""


def score():
    pass