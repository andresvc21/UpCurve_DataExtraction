#Andres Villegas Ceballos and DevOps Team
#Team 4
#Colegiate Council
#January 2021

import urllib3
import requests
from bs4 import BeautifulSoup as bs
import webbrowser
import glob
import os
import shutil
import time
import pdfplumber
import pandas as pd
import keyboard
from urllib.parse import urlparse
import urllib.request
from urllib.request import urlopen as urlopen
from urllib import request
from urllib.request import urlretrieve
import re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

def check_validity(my_url):
    """Check the validity of the URL in university land site

    If the URL is worng print Invalid URL and exit the code
    :param my_url:
    :return:
    """

    try:
        requests.get(my_url)
        print("Valid URL")
    except IOError:
        print ("Invalid URL, This URL will not be considered for the study ")
        flag=1
        return (flag)

    # print(check_validity.__doc__)

def download_file(download_url):
    """Function to download each one of the files using chrome as browser, in that way it's possible to avoid the Captcha from university Lands
    :param download_url:
    """
    webbrowser.get('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" %s').open(download_url)


def move_file(target_dir):
    """Move the files from Download to the path defined by the user
    :param target_dir:
    """

    #Lets try to change the directory of set Chrome's download folder programmatically

    chromeOptions = webdriver.ChromeOptions()
    download_path=get_download_path()
    print(download_path)
    prefs = {"download.default_directory": download_path}
    chromeOptions.add_experimental_option("prefs", prefs)

    list_of_files = glob.glob(download_path+'\\*.pdf')  # * means all if need specific format then *.csv
    list_of_files.sort(key=os.path.getmtime) #parse files by generation time
    # print("\n".join(list_of_files))
    latest_file=list_of_files[-1]
    shutil.move(os.path.join(download_path, latest_file), target_dir)

    # print(target_dir.__doc__)

def get_download_path():
    """Returns the default downloads path for linux or windows
    :return:
    """

    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def dowload_html(my_url, path):
    """Dowload source code from the web site using the Mask for Chrome
    :param my_url: URL from the Universit land site
    :param path: path defined by the user
    :return: return the source code
    """

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36','Cookie':'__utmz=252366797.1609882756.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); BNIS_x-bni-jas=xY4mu5GDGbsTSa_rOCev0dJj4vlU53o5qog7VclNGWw=; x-bni-ci=A_Ps40H_X0wlUfBD8pmhvAJ4cRJqPf-YQtGRO7pz1A-9zWnimA-Vo-RPoLWe8qfDbrDY2rprx3jg9FKPd3FsDU4tDJv1wRjRiHV-4VZZjzI=; __RequestVerificationToken=4d9yt3IiNwvZ5R7pBkXwevMIO6q2XPwlBk8xulynG2laJymM7r5Y3yWLFwrXM9ZdApsVHMif3-gHeWs7ZXRnP_uRPI6r6-rXTQ5ww1Jr6LU1; __utma=252366797.781299337.1609882756.1611945077.1611949028.15; __utmc=252366797'}
    r = requests.get(my_url, headers=headers)
    page_source = r.text
    # page_source = page_source.split('\n')
    print(page_source)
    return(page_source)

    print(download_html.__doc__)

def get_pdfs(my_url, path, well):
    """Function to get PDF from [my_url]
    :param my_url: URL from the Universit land site
    :param path: path defined by the user
    :param well: API number
    :return: the file number and the target directory
    """


    links = []
    # html=dowload_html(my_url, path) #To use it with the web

    # response = urllib.request.urlopen(my_url)
    # webContent = response.read()
    #
    # f = open(str(well)+'.html', 'wb')
    # f.write(webContent)
    # f.close

    html=open("test.html", "r")

    # html=open(str(well)+'.html', "r")

    # html=open("well_test.html", "r")

    # html = urlopen(my_url).read()
    # print(html)
    # html_page = bs(html, features="lxml")
    # reponse= request.urlopen(my_url)
    # reponse=html
    # contents = reponse.read().decode('utf-8')

    html_page = bs(html, features="html.parser")

    # og_url = html_page.find("meta", property="og:url")
    # base=urlparse(my_url)

    print(html_page)

    typ=[]

    for link in html_page.findAll('a'):
        # print(link)
        if '/WellDocument' in link['href']:
            links.append(link.get('href'))
        single_links=list(dict.fromkeys(links))
    print(single_links)

    i=0
    while i < len(single_links):
        single_links[i]='http://www.universitylands.utsystem.edu/'+single_links[i]
        i+=1
    print(single_links)

    #FUTURE WORK: In university lands there are titles more specific for each document, import that titlle

    filenumber=len(single_links)
    target_dir = os.path.join(path, str(well))
    print(target_dir)

    try:
        os.mkdir(target_dir)
    except FileExistsError :
        print("You already downloaded well "+str(well)+" please eliminate this well from the list") #TODO! pass to the next one error managment
        os._exit(0)

    for link in single_links:
        print(link)
        download_file(link)

    time.sleep(15)

    return (filenumber, target_dir)



        # try:
        #     count += 1
        #     print(count)
        #     urllib.urlretrieve(link, "st-intro.pdf")
        #     # filename=Path('metadata.pdf')
        #     # response = urllib.request.get(link)
        #     # print(response)
        #     # filename.write(response.content)
        # except:
        #     print(" \n \n Unable to Download A File \n")

    # print(get_pdfs.__doc__)

def Get_text_from_image(pdf_path):
    """Function using wi and pytesseract to convert the scan image in the PDF to text.

    Please ensure that you have the right paths to both programs. If not go to
    https://pypi.org/project/pytesseract/ and https://poppler.freedesktop.org/

    and follow the instructions!
    :return:
    :param pdf_path:
    :return: """

    pdf=wi(filename=pdf_path,resolution=300)
    pdfImg=pdf.convert('jpeg')
    imgBlobs=[]
    extracted_text=[]
    for img in pdfImg.sequence:
        page=wi(image=img)
        imgBlobs.append(page.make_blob('jpeg'))
    for imgBlob in imgBlobs:
        im=Image.open(io.BytesIO(imgBlob))
        text=pytesseract.image_to_string(im,lang='eng')
        extracted_text.append(text)

    return (extracted_text)

def pdf_image_to_text(target_file):
    """This function is call by well_name_function and llok for the name
    
    PLease ensure that tesseract is installed in your computer, if needed change the path to the .exe in this function
    :param target_file: 
    :return: 
    """  #TODO! change this to do it more geneic

    target_file = 'Test_5.pdf'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pdf = wi(filename=target_file, resolution=300)
    pdfImg = pdf.convert('jpeg')
    extracted_text=Get_text_from_image(target_file)
    with open('image_text_file.txt', 'w') as f:
        for item in extracted_text:
            f.write("%s\n" % item)
        f.close
    a_file = open("image_text_file.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    print(list_of_lists)
    well_name = []

    #From here to do it more generci
    if list_of_lists[302] != []:
        well_name.append(list_of_lists[302][0])
    else:
        print("Name not found")
        os.exit

    if list_of_lists[344] != []:
        well_name.append(list_of_lists[344][0])

    return(well_name)

#*****************Specific function for the operator PIONEER NATURAL RES*********************** TODO!
#However the function could also work easy for other operator because the document used is the RailRoad Comission of Texas App. Permit
def well_name_function(path, well):
    """Function to search the Well Name property inside the PDF documents
    :param path:
    :return:
    """
    #TODO! Intermediate function to separate files
    path=path+str(well)
    #In this case I know the name of the file but a function to look for texas rail road?
    # target_file = os.path.join(path, 'UNIVERSITY 3-310PU 9H_4246140595_APPROVED W1_5.19.17_474921.pdf')
    # print(target_file)
    # target_file= os.path.join(path, 'UNIVERSITY 3-310PU 9H_4246140595_APPROVED W1_5.19.17_474921.pdf')
    # target_file=['Test_1.pdf', 'Test_2.pdf','Test_3.pdf','Test_4.pdf', 'Test_5.pdf']
    target_file = ['Test_1.pdf', 'Test_2.pdf']


    well_name=[]
    lenght=len(target_file)
    i=1

    #LOOP pdf to text and data extraction
    while i < lenght+1:
        print(target_file[i-1])

        with pdfplumber.open(target_file[i-1]) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
        print(text)

        text_file = open("Output"+str(i)+".txt", "w")

        #IMAGE FILE
        try:
            text_file.write(text)
        except TypeError as err:
            print(target_file[i-1]+' is a image file,  using the function for images')
            results_image=pdf_image_to_text(target_file[i-1])
            print(results_image)
            l=0
            while l<len(results_image):
                well_name.append(results_image[l])
                l+=1


        text_file.close()

        a_file = open("Output"+str(i)+".txt", "r")

        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            # print(line_list)

            list_of_lists.append(line_list)

        a_file.close()

        try:
            matches = list_of_lists.index(['Reservoir'])
            j = 1

            # LOOP Tunning for the specific FORMAT
            while j < 10:

                try:
                    list_of_lists[matches + j][0] == 0
                    # print(list_of_lists[matches+j])
                    # print(list_of_lists[matches+j][2])
                    well_name.append(list_of_lists[matches + j][2])
                except OSError as err:
                    print("OS error: {0}".format(err))
                    break
                except IndexError as err:
                    pass
                    break
                except ValueError:
                    print("Value ERROR.")
                    break

                j += 1

            i += 1


        except ValueError as err:
              break
        #     well_name.append('*****ERROR: IMAGE FILE, please use the image function*****')

        # print(matches)

    k = 1
    #LOOP to delete temporary text files
    while k < lenght + 1:
        print(k)
        os.remove("Output"+str(k)+".txt")
        k += 1
    #
    return (well_name, len(well_name))


def stages_function(well):
    """
    In charge of finde the number of stages and create the data frame to return
    :param well: well in the loop from the user
    :return: data frame with number of stages
    """

    data = pd.read_csv("E:/Personal/ASME/TEST/Info_To_HEEDS.csv")
    stages=data.loc[data["API"] == well, "Stage"]
    API = data.loc[data["API"] == well, "API"]
    # print(stages)
    # print(API)
    return API, stages

def breakdownpressure_function(well):
    """
    In charge of finde the breakdown pressure for each one of the sages
    :param well: well in the loop from the user
    :return: data frame with data for breakdownpressure in [psi]
    """

    data = pd.read_csv("E:/Personal/ASME/TEST/Info_To_HEEDS.csv")
    breakdownpressure=data.loc[data["API"] == well, "Breakdown Pressure (psi)"]
    # print(breakdownpressure)
    return breakdownpressure


def main():

#Main Function

    wellsAPI=[]

    while True:
        try:
            well = int(input("Please enter your well API without slash, if you dont want to enter more API's use 0: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if well==0:
            break
        else:
            wellsAPI.append(well)

    while True:
        try:
            user_input = input("Enter the path to save the files, HINT! Copy the path directly from the explorer window: ")
            assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
            print("Hooray! the path is valid!")
        except AssertionError:
            print("I did not find the file at, " + str(user_input))
            continue
        except TypeError:
            print("Try to re-write the path" )
            continue
        else:
            break

    path=user_input

    # path='E:/Personal/ASME/TEST' #In case we want to skeep the while True of input path

    # wellsAPI=[4246140595] #try
    # wellsAPI=[4238338578, 4246139451]
    # wellsAPI=[4246140595, 4200343438, 4200348163, 4200348169, 4200343666]
    # wellsAPI=[4238338578, 4238338577, 4238338576, 4238338553, 4238338550, 4246139452, 4246139451, 4246139445, 4246139444]
    list_API=[]



    for well in wellsAPI:
        idx=wellsAPI.index(well)
        my_url='http://www.universitylands.utsystem.edu/API/%d'% (well)
        print(my_url)
        flag=check_validity(my_url)
        if flag==1:
            wellsAPI.remove(idx)

        filenumber, target_dir=get_pdfs(my_url, path, well)

        for x in range(filenumber):
            move_file(target_dir)

        # #Frac Summary Table TODO! check with the actual files
        # well_name, length=well_name_function(path, well)
        # print('WELL NAME: '+ str(well_name))

    # i=0
    # while i<length:
    #     list_API.append(well)
    #     i+=1


    # print(well_name)
    # print(list_API)
    # df = pd.DataFrame({"API":list_API, 'WELL NAME':well_name})
    # print(df)

    appended_data = []

    for well in wellsAPI:

        API, stages =stages_function(well)
        breakdownpressure =breakdownpressure_function(well)

        frames = {'API':API, 'Stages':stages, 'Break Down Pressure [psi]':breakdownpressure}

        result = pd.DataFrame(frames)
        print(result)

        appended_data.append(result)

    appended_data = pd.concat(appended_data)
    print(appended_data)
    appended_data.to_csv(r'E:\Personal\ASME\TEST/export_dataframe.csv', index=False)


if __name__ == "__main__":
    main()