import requests
def IsThePageExist(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
def read_websites_from_file(file_name):
    with open(file_name, "r") as file:
        websites = file.readlines()
        websites = [x.replace("\n","") for x in websites]
        return websites
def filter_working_websites(websites):
    working_websites = []
    for website in websites:
        if IsThePageExist(website):
            working_websites.append(website)
        else: print("nie ma takiej strony")
    return working_websites
def save_working_websites(working_websites, file_name):
    with open(file_name, "w") as file:
        for website in working_websites:
            file.write(website)

websites = read_websites_from_file("websites.txt")
working_websites = filter_working_websites(websites)
save_working_websites(working_websites, "working_websites.txt")
    
