from dynamic_geographic_scoring import *

if __name__ == "__main__":
    geolocated_list = parse_excel_address_columns("EDA_Export_FullFile_20220831.xlsx",
                                                  ["BUYADR1", "BUYCITY", "BUYSTATE"],
                                                  "AkpW075G4UOWN7lJqDMQJ_o6SxDZ8nA1riedUl0tLGH5Irga56-0kkFoCSnNEMBs")
    print(geolocated_list)
    geolocated_list.to_excel("geolocated.xlsx")
