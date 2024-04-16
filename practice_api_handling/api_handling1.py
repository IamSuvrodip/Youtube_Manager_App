import requests

def fectch_user_details():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    # convert json file
    data = response.json()

    if data["success"] and "data" in data:
        user_data= data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country

    else:
        raise Exception("Faild to fetch user data")


def main():
    try:
        username, country = fectch_user_details()
        print(f"Username is: {username} \nCountry is: {country}...")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()