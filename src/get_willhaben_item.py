import requests
import os
import sys
import random
import time
from bs4 import BeautifulSoup
from PIL import Image
from colorama import Fore
from math import ceil


def get_willhaben_item(self, url):
    def get_items_to_list(self, url):

        site_number = 1

        while True:
            result_page = requests.get(url + f"&page={str(site_number)}")
            second_soup = BeautifulSoup(result_page.content, 'html.parser')

            must_in = "/iad/kaufen-und-verkaufen/d/"
            must_not_in = "counterId="

            for x in second_soup.find_all('a', href=True):
                    if x.text and must_in in x['href'] and must_not_in not in x['href'] and x['href'] not in self.links_with_product:
                        self.links_with_product.append(x['href'])

                    if len(self.links_with_product) >= self.quantity:
                        break
            if len(self.links_with_product) >= self.quantity:
                break
            site_number += 1

    def get_item_list(self, url):
        search_page = requests.get(url)
        soup = BeautifulSoup(search_page.content, 'html.parser')
        count = int(str(soup.find(id="search-count")).strip(
            """<span class="search-count" id="search-count"> </span>""").replace(".", ""))

        if count == 0:
            print(Fore.GREEN + "No products were found according to the specified criteria." + Fore.CYAN)
            return ""
        else:
            print(
                Fore.GREEN + f"-------------------------------------\nThere were {count} products found.\n-------------------------------------" + Fore.CYAN)

            while True:
                self.quantity = self.int_input(Fore.CYAN + "How many products do you want to grab?\n")

                if self.quantity < 1:
                    print(Fore.RED + "Quantity must be at least 1\n" + Fore.CYAN)

                elif self.quantity > count:
                    print(Fore.RED + f"According to the specified criteria, a maximum of {count}  products can be grabbed." + Fore.CYAN)

                elif 0 < self.quantity < 101:
                    print(Fore.GREEN + "Grabbing products..." + Fore.CYAN)

                    if not os.path.exists('Results'):
                        os.makedirs('Results')

                    get_items_to_list(self, url)

                    return self.links_with_product

                elif self.quantity > 100:
                    print(Fore.GREEN + "Grabbing products..." + Fore.CYAN)

                    if not os.path.exists('Results'):
                        os.makedirs('Results')

                    get_items_to_list(self, url)

                    return self.links_with_product
                else:
                    break

    self.links_with_product = get_item_list(self, url)

    if self.links_with_product != "":
        for x in range(self.quantity):
            pdkte = random.choice(self.links_with_product)
            self.links_with_product.remove(pdkte)

            name_adding = 0

            product_page = requests.get("https://www.willhaben.at" + pdkte)

            soup_pd = BeautifulSoup(product_page.content, 'html.parser')

            for heading in soup_pd.find_all("title"):
                heading_item = heading.text.strip("- willhaben")

            for code in soup_pd.find_all("span", {"id": "advert-info-whCode"}):
                wh_code = code.text.replace(":", "")

            for desc in soup_pd.find_all("div", {"class": "description"}):
                description = desc.text.strip()

            if not os.path.exists("Results/" + wh_code):
                os.makedirs("Results/" + wh_code)

            must_in_img = "https://cache.willhaben.at/mmo/"

            image_links = []

            for img in soup_pd.find_all('img'):
                if "https://secure.adnxs.com/" in img['src'] or "hoved.jpg" in img['src'] or ".svg" in img['src']:
                    pass
                elif ".jpg" in img['src'] and must_in_img in img['src']:
                    image_links.append(img['src'])

            for i in image_links:
                response = requests.get(i)

                imagename = f"Image{name_adding}" + ".jpg"

                name_adding += 1
                try:
                    with open(os.path.join(f'Results/' + f"{wh_code}", imagename), "wb") as file:
                        file.write(response.content)
                        file.close()
                        image_to_change = Image.open(f'Results/' + f"{wh_code}/" + imagename)

                        neue_länge = round(int(list(image_to_change.size)[0]) * 0.9)
                        neue_breite = round(int(list(image_to_change.size)[1]) * 0.9)

                        new_image = image_to_change.resize((neue_länge, neue_breite))
                        new_image.save(f'Results/' + f"{wh_code}/" + imagename)
                except:
                    os.remove(f'Results/' + f"{wh_code}/{imagename}")

            infos = open("Results/" + wh_code + f"/Infos {wh_code.split()[1]}.txt", "w", encoding='utf-8',
                         errors='replace')
            infos.write("Titel, Price, ZIP and Place:\n")
            infos.write(heading_item)
            infos.write("\n----------------------------------------------\n")
            infos.write("Description:\n")
            infos.write(description)
            infos.write("\n----------------------------------------------\n")
            infos.write("Willhaben Link:\n")
            infos.write("https://www.willhaben.at" + pdkte)
            infos.write("\n----------------------------------------------\n")
            infos.close()

        print(Fore.GREEN + f"-----------------------\nGrabbing completed.\n-----------------------" + Fore.CYAN)
        self.zeit_ende = time.time()
        self.zeit_dauer = round(self.zeit_ende - self.zeit_start)
        print(f"Grabbing took {self.zeit_dauer} seconds.")

        while True:
            again_grab = input("Do you want to grab more products? Y - Yes oder N - No\n").lower()
            if again_grab == "y":
                self.clear_console()
                self.marktplatz()
                break
            elif again_grab == "n":
                sys.exit(0)
            else:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
