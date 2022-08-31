from dynamic_geographic_scoring import *

if __name__ == "__main__":
    geolocated_list = parse_excel_address_columns("EDA_Export_FullFile_20220831.xlsx",
                                                  ["BUYADR1", "BUYADR2", "BUYCITY", "BUYSTATE"],
                                                  "INPUT_YOUR_API_KEY")
    print(geolocated_list)
    geolocated_list.to_excel("geolocated.xlsx")
