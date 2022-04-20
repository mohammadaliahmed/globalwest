import json
import re
import requests
from bs4 import BeautifulSoup
from xmlrpc.client import Boolean
import pandas as pd

import traceback
from woocommerce import API
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# url="https://www.globalwest.net/pontiac-gto-lemans-tempest-1973-1977-front-suspension.html"
# url = "https://www.globalwest.net/riviera-1963-1964-1965-1966-1967-1968-1970-1971-1972-1973-1974-1975-1976-1977-1978-1979-1980-1981-19.html"
# html_content = requests.get(url).text
# soup = BeautifulSoup(html_content, "lxml")
# special_divs = soup.find_all('div', {'class': 'sectinfo'})

# html_content = '''<li class="megatop">Buick <ul style="display: none;"><li><a href="riviera-1963-1964-1965-1966-1967-1968-1970-1971-1972-1973-1974-1975-1976-1977-1978-1979-1980-1981-19.html">Riviera 1963-1984</a></li><li class="mega">Skylark, GS, Special, Grand Sport, Sport Wagon 1964-1972<div class="navbox"><table width="100%"><tbody><tr><td class="tl"></td><td class="b"></td><td class="tr"></td></tr><tr><td class="b"></td><td class="body"><div class="content"><table><tbody><tr><td valign="top"><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-gs-skylark-special-grand-sport-wagon-front-control-arms.html">Front Control Arms, Bushings and Shafts</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-gs-skylark-special-grand-sport-wagon-front-springs-shocks-sway-bar-coilover.html">Front Springs, Shocks, Sway Bar and Coilover</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-gs-skylark-special-grand-sport-wagon-rear-control-arms.html">Rear Control Arms and Frame Supports </a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="skylark-gs-special-grand-sport-sport-wagon-buick-64-65-66-67-68-69-70-71-72-replacement-parts.html">Replacement Parts</a></td></tr></tbody></table></li></ul></td></tr></tbody></table></div></td><td class="b"></td></tr><tr><td class="bl"></td><td class="b"></td><td class="br"></td></tr></tbody></table></div></li><li><a href="1975-80skylark.html">Skylark, Special, 1975-1980</a></li><li class="mega">1973-1977 (Century, Regal, Grand National) <div class="navbox"><table width="100%"><tbody><tr><td class="tl"></td><td class="b"></td><td class="tr"></td></tr><tr><td class="b"></td><td class="body"><div class="content"><table><tbody><tr><td valign="top"><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-front-control-arms-1964-1972.html">Front Control Arms, Bushings and Shafts</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-springs-sway-bar-coilovers-1964-1972.html">Springs, Sway Bars and Coilover Kits</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-rear-control-arms-frame-supports-1964-1972.html">Rear Control Arms and Frame Supports</a></td></tr></tbody></table></li></ul></td></tr></tbody></table></div></td><td class="b"></td></tr><tr><td class="bl"></td><td class="b"></td><td class="br"></td></tr></tbody></table></div></li><li class="mega">1978-1988 (Century, Regal, Grand National) <div class="navbox"><table width="100%"><tbody><tr><td class="tl"></td><td class="b"></td><td class="tr"></td></tr><tr><td class="b"></td><td class="body"><div class="content"><table><tbody><tr><td valign="top"><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-1973-1977-front-control-arms.html">Front Control Arms, Bushings and Shafts</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-1973-1977-springs.html">Springs, Sway Bars and Coilover Kits</a></td></tr></tbody></table></li></ul><ul class="subsubnav"><li><table width="300"><tbody><tr><td><a class="sublink noimg" href="buick-century-regal-grand-national-1973-1977-rear.html">Rear Control Arms and Frame Supports</a></td></tr></tbody></table></li></ul></td></tr></tbody></table></div></td><td class="b"></td></tr><tr><td class="bl"></td><td class="b"></td><td class="br"></td></tr></tbody></table></div></li><li class="last"><a href="1984-87grandnationalturbo.html">Grand National, Turbo 1984-1987</a></li></ul></li>'''
# soup = BeautifulSoup(html_content, "lxml")
# special_divs = soup.find_all('li', {'class': 'megatop'})
# --------------------------------------------------------------------------------------------------------------------------------------------

try:
    data = pd.read_excel(r'3level.xlsx')
    filenameToWrite="buick3.txt"
    df = pd.DataFrame(data, columns=['main', 'child', 'categoryUrl'])
    for row in range(0,3 ):
        # url = "https://www.globalwest.net/" + str(df.loc[row]["id"]) + ".html"
        # wcapi = API(
        #     url="http://localhost/woocommerce/",
        #     consumer_key="ck_3dd172aac6fd001e568c0545932fea720d36e313",
        #     consumer_secret="cs_f94a7b4df7e186f3c4cb70cd3426419943186a5a",
        #     version="wc/v3",
        #     timeout=60
        # )
        wcapi = API(
            url="https://staging3.trexnex.com",

            consumer_key="ck_b3ecde7ddff3bc6c12b72de465c97f18d0618bda",
            consumer_secret="cs_0da51cba71ebc7c805dc053bc67fab27144e1156",
            version="wc/v3",
            timeout=60
        )

        

        firstLevelId = ""
        secondLevelCategoryId = ""
        thirdLevelCategoryId = ""

        categoryName = str(df.loc[row]["child"])
        print(categoryName)

        categoryUrl = "https://www.globalwest.net/"+str(df.loc[row]["categoryUrl"])
##        categoryUrl = str(df.loc[row]["categoryUrl"])

        print(categoryUrl)

        data = {
            "name": str(df.loc[row]["main"])
        }
        abcaaa = wcapi.post("products/categories", data).json()
        try:
            firstLevelId = abcaaa["id"]
        except:
            firstLevelId = abcaaa["data"]["resource_id"]

        data = {
            "name": categoryName,
            "parent": str(firstLevelId)
        }
        abcaaa = wcapi.post("products/categories", data).json()

        try:
            secondLevelCategoryId = abcaaa["id"]
        except:
            secondLevelCategoryId = abcaaa["data"]["resource_id"]
        try:
            print(str(row)+" "+categoryUrl+"\n")
            html_content = requests.get(categoryUrl).text
            soup = BeautifulSoup(html_content, "lxml")
            special_divs2 = soup.find_all('div', {'class': 'sectinfo'})
            for text2 in special_divs2:
                download = text2.find_all('a')
                if len(download) > 0:
                    for text in download:
                        hrefText = (text['href'])
                        categoryName = text.text
                        for text in special_divs2:
                            download = text.find_all('h1')
                            secondLevelCategoryName = download[0].text
                            print("child:  " + secondLevelCategoryName + "    " + categoryName + " " + hrefText)

                            data = {
                                "name": categoryName,
                                "parent": str(secondLevelCategoryId)
                            }
                            abcaaa = wcapi.post("products/categories", data).json()

                            try:
                                thirdLevelCategoryId = abcaaa["id"]
                            except:
                                thirdLevelCategoryId = abcaaa["data"]["resource_id"]

                        page = requests.get(hrefText)
                        soup = BeautifulSoup(page.content, "html.parser")
                        scripts = soup.findAll("script")
                        items = []
                        for script in scripts:
                            data = script.decode_contents()
                            if "new pagingItem" in data:
                                data = data[data.index("window"):]
                                data = data[0: data.index("; var ")]
                                while len(data) > 0:
                                    item = False
                                    try:
                                        c = data[0]
                                        data = data[1:]
                                        item = c + data[0: data.index("window.item")]
                                        data = data[data.index("window.item"):]
                                    except ValueError:
                                        item = data
                                        data = ""
                                    if item is not False:
                                        items.append(item)
                        for item in items:
                            abc = item.split(",")[0]
                            finl = abc.rsplit('(', 1)[1]
                            productSLug = str(finl).replace('"', "")
                            fileOut = open(filenameToWrite, "a")
                            fileOut.write(str(thirdLevelCategoryId) + "," + productSLug + "\n")
                            fileOut.close()
                else:

                    page = requests.get(categoryUrl)
                    soup = BeautifulSoup(page.content, "html.parser")
                    scripts = soup.findAll("script")
                    items = []
                    for script in scripts:
                        data = script.decode_contents()
                        if "new pagingItem" in data:
                            data = data[data.index("window"):]
                            data = data[0: data.index("; var ")]
                            while len(data) > 0:
                                item = False
                                try:
                                    c = data[0]
                                    data = data[1:]
                                    item = c + data[0: data.index("window.item")]
                                    data = data[data.index("window.item"):]
                                except ValueError:
                                    item = data
                                    data = ""
                                if item is not False:
                                    items.append(item)
                    for item in items:
                        abc = item.split(",")[0]
                        finl = abc.rsplit('(', 1)[1]
                        productSLug = str(finl).replace('"', "")
                        fileOut = open(filenameToWrite, "a")
                        fileOut.write(str(secondLevelCategoryId) + "," + productSLug + "\n")
                        fileOut.close()
        except:
            traceback.print_exc()
except:
    traceback.print_exc()
