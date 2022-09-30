from bs4 import BeautifulSoup
from PIL import Image, UnidentifiedImageError
from tqdm import tqdm
from io import BytesIO
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
from natsort import natsorted
import re 
import os
import time
import requests
import PyPDF2


def get_manga_link(base_url):
    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r"C:\Users\Samael101\.vscode\Python2021\Pandas\geckodriver.exe")

    driver.get(base_url)
    print("Headless Firefox Initialized")

    search_box = driver.find_element_by_xpath("/html/body/div[1]/div/form/input[1]")
    search_box.click()

    search_manga = driver.find_element_by_xpath('//*[@id="search"]')
    search_manga.send_keys("")
    # time.sleep(0.1)

    manga_user_input = input("Please enter manga title to download: \n")
    search_manga.send_keys(manga_user_input)
    # time.sleep(0.1)

    button_search = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/a")
    button_search.click()
    time.sleep(1)

    manga_titles_url = driver.current_url

    html_ver = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html_ver, "lxml")

    table = sel_soup.find_all("div", class_ = "ls5")
    search_result = []
    for i in table:
        result_dict = {}
        result_dict["title"] = i.a["title"]
        result_dict["link"] = base_url + i.a["href"]
        search_result.append(result_dict)
    driver.quit()

    for i,choice in enumerate(search_result):
        print(f'{i} : {choice["title"]}')
    print()
    user = int(input("please choose manga from list: \n "))
    if user in range(len(search_result)):
        search_url = search_result[user]["link"]
        print(f'{search_result[user]["title"]} : {search_result[user]["link"]}')
    
    #--------------------------------------------------------------------#
        
    r = requests.get(search_url)
    soup = BeautifulSoup(r.content, "lxml")

    search_result = soup.find("body").find_all("div",class_="p series")
    search_result
    tr = search_result[0].find_all("tr", attrs={"itemprop": "hasPart"})
    Manga_name = search_result[0].find("b", attrs={"style": "font-size:16px"}).text
    title_array = []
    for i in tr:
        title_info={}
        title_info["title"] =i.a["title"]
        title_info["link"] =base_url + i.a["href"]
        title_array.append(title_info)
    title_array.reverse()
    
    list = [int(item) for item in re.findall("\d+",input("\nenter Selected Chapters separated by comma(,): \n"))]
    selected_chapters = [i for i in range(list[0], list[1]+1)]
  
    #--------------------------------------------------------------------#


    if os.path.exists(Manga_name):
        os.chdir(os.path.join(os.getcwd(),Manga_name))
        print("\n{} folder exists.\nChanging CWD to {}\n".format(Manga_name, os.getcwd()))
    else:
        try:
            os.mkdir(Manga_name)
            os.chdir(os.path.join(os.getcwd(),Manga_name))
            print("\n{} folder created\n".format(Manga_name))
        except:
            pass
    #--------------------------------------------------------------------#

    all_files = [os.path.splitext(i)[0] for i in os.listdir() if i.endswith(".pdf")]
    print("Downloading Selected chapters...\n")

    #--------------------------------------------------------------------#

    for x in (selected_chapters):
        req_chap = requests.get((title_array[x]["link"]))
        chap_soup = BeautifulSoup(req_chap.content, "lxml")
        pages = chap_soup.find_all("div", attrs={"id": "Read"})
        check_title = title_array[x]["title"]

        if check_title not in all_files:

            for page in tqdm(pages[0].find_all("img"),desc = title_array[x]["title"], leave = False):
                try:
                    page_num = page["alt"]
                    page_src = page["data-src"]
                    sheet = requests.get(page_src, "lxml")
                    image = Image.open(BytesIO(sheet.content))
                    image.save(page_num + ".pdf")
                except Exception:
                    print(f" error on chapter : {page_num}")
                    pass

                merger = PyPDF2.PdfFileMerger()
                list_to_delete = natsorted([f for f in os.listdir(os.getcwd()) if "Page" in f])
                for h in list_to_delete:
                    merger.append(h)
                merger.write(title_array[x]["title"] + ".pdf")
                merger.close()
            for h in list_to_delete:
                os.remove(h)
            print("{} Downloaded...".format(title_array[x]["title"]))
        else:
            print("{} already there".format(title_array[x]["title"]))
        
    print("\nAll chapters have been downloaded\n")
    #--------------------------------------------------------------------#

def main():
    base_url = "https://mangafast.net"
    search_url = get_manga_link(base_url)


if __name__ == "__main__":

    os.chdir(r'C:\Users\Samael101\.vscode\Manga Extractor')
    main()
    

    
    

    