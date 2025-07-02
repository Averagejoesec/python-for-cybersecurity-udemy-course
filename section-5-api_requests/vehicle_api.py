import requests as r
import json


def vehicle_search():
    print("Search for vehicle details.")

    make = input('Enter a make for the vehicle (honda/mazda/nissan/toyota/etc..)\n')
    model_year = int(input('Enter a year for the model (YYYY)\n'))
    vehicle_type = input('Enter a vehicle type (car/truck/moto/etc...)\n')

    return make, model_year, vehicle_type


def main():

    make, model_year, vehicle_type = vehicle_search()

    try:
        response = r.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{make}/modelyear/{model_year}/vehicleType/{vehicle_type}?format=json')
        results = response.json()['Results']
        if results == []:
            print("No vehicles found, please search again")
            main()
    except:
        print('Please enter valid attributes for vehicle search.')
        main()

    for v in results:
        make_id = v['Make_ID']
        make_name = v['Make_Name']
        model_id = v['Model_ID']
        model_name = v['Model_Name']
        type = v['VehicleTypeName']
        print(f"Make ID: {make_id}, Make name: {make_name}, Model ID: {model_id}, Model name: {model_name}, Type: {type}")


if __name__ == "__main__":
    main()