import json
import pickle
import numpy as np


__furnishing =None
__data_columns =None
__model =None

def get_estimated_price(bathroom,area,floor_number,parking,power_backup,total_rooms,furnishing,available_for,property_age,wheelchair_availablity,pets_allowed,floor_type,place):
    try:
        place_index = __data_columns.index(place.lower())
    except:
        place_index =-1

    try:
        furn_index = __data_columns.index(furnishing.lower())
    except:
        furn_index =-1

    try:
        available_for_index = __data_columns.index(available_for.lower())
    except:
        available_for_index =-1

    try:
        wheelchair_availablity_index = __data_columns.index(wheelchair_availablity.lower())
    except:
        wheelchair_availablity_index =-1

    try:
        pets_allowed_index = __data_columns.index(pets_allowed.lower())
    except:
        pets_allowed_index =-1

    try:
        floor_type_index = __data_columns.index(floor_type.lower())
    except:
        floor_type_index =-1

    try:
        property_age_index = __data_columns.index(property_age.lower())
    except:
        property_age_index =-1



    x = np.zeros(len(__data_columns))

    x[0]=bathroom
    x[1]= area
    x[2]=floor_number
    x[3]=parking
    x[4]=12
    x[5]=power_backup
    x[6]=30000
    x[7]=total_rooms

    if (place_index >= 0):
        x[place_index] = 1

    if(furn_index>=0):
        x[furn_index]=1

    if (available_for_index >= 0):
        x[available_for_index] = 1

    if (property_age_index >= 0):
        x[property_age_index] = 1

    if (floor_type_index >= 0):
        x[floor_type_index] = 1

    if (pets_allowed_index >= 0):
        x[pets_allowed_index] = 1

    if (wheelchair_availablity_index >= 0):
        x[wheelchair_availablity_index] = 1



    return round(__model.predict([x])[0])



def get_furnishing_method():
    return __furnishing


def load_saved_artifacts():
    print("loading saved artifacts.....")
    global __data_columns
    global __furnishing

    with open("./artifacts/columns4.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __furnishing = __data_columns[9:12]
    global  __model
    with open("./artifacts/PF4.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading  artifacts Done")


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_furnishing_method())
    print(get_estimated_price(3,1900,3,3,1,2,"furnished","family only","1 to 5 year old","wheelnotchairavailable","petnotavailable","marble","fort kochi"))
