import os
import sys
import random
import time
from colorama import init, Fore
import colorama
from get_willhaben_item import get_willhaben_item
from build_url import build_willhaben_url


class Willhaben():
    def __init__(self):
        self.url_base = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz"
        self.menu = {"1": "/kaufen-und-verkaufen",
                     "links": {"1": "/antiquitaeten-kunst-6941", "2": "/kameras-tv-multimedia-6808", "3": "/baby-kind-3928",
                               "4": "/kfz-zubehoer-motorradteile-6142", "5": "/beauty-gesundheit-wellness-3076",
                               "6": "/mode-accessoires-3275", "7": "/boote-yachten-jetskis-5007823", "8": "/smartphones-telefonie-2691",
                               "9": "/buecher-filme-musik-387", "10": "/spielen-spielzeug-5136", "11": "/computer-software-5824",
                               "12": "/sport-sportgeraete-4390", "13": "/dienstleistungen-537", "14": "/tiere-tierbedarf-4915",
                               "15": "/freizeit-instrumente-kulinarik-6462", "16": "/uhren-schmuck-2409",
                               "17": "/games-konsolen-2785", "18": "/wohnen-haushalt-gastronomie-5387",
                               "19": "/haus-garten-werkstatt-3541", "20": "/zu-verschenken/"}}
        self.links_with_product = []
        self.marktplatz()

    def logo(self):
        init()
        text = """
▄▄▄▄· ▪   ▄▄ • ▄▄▄▄·       .▄▄ · .▄▄ ·   ▄▄▌ ▐ ▄▌▪  ▄▄▌  ▄▄▌   ▄ .▄ ▄▄▄· ▄▄▄▄· ▄▄▄ . ▐ ▄   ▄▄▄▄▄            ▄▄▌  
▐█ ▀█▪██ ▐█ ▀ ▪▐█ ▀█▪ ▄█▀▄ ▐█ ▀. ▐█ ▀.   ██· █▌▐███ ██•  ██•  ██▪▐█▐█ ▀█ ▐█ ▀█▪▀▄.▀·•█▌▐█  •██   ▄█▀▄  ▄█▀▄ ██•  
▐█▀▀█▄▐█·▄█ ▀█▄▐█▀▀█▄▐█▌.▐▌▄▀▀▀█▄▄▀▀▀█▄  ██▪▐█▐▐▌▐█·██▪  ██▪  ██▀▐█▄█▀▀█ ▐█▀▀█▄▐▀▀▪▄▐█▐▐▌   ▐█.▪▐█▌.▐▌▐█▌.▐▌██▪  
██▄▪▐█▐█▌▐█▄▪▐███▄▪▐█▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█  ▐█▌██▐█▌▐█▌▐█▌▐▌▐█▌▐▌██▌▐▀▐█ ▪▐▌██▄▪▐█▐█▄▄▌██▐█▌   ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
·▀▀▀▀ ▀▀▀·▀▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀▀    ▀▀▀▀ ▀▪▀▀▀.▀▀▀ .▀▀▀ ▀▀▀ · ▀  ▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪   ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
"""
        bad_colors = ['LIGHTGREEN_EX', 'GREEN', 'RED', 'BLUE', 'YELLOW']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars) + Fore.CYAN)

    def str_input(self, text):
        while True:
            rt = input(text)
            if rt != "":
                break
            else:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
        return rt

    def int_input(self, text):
        while True:
            try:
                rt = int(input(text))
                break
            except:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
        return rt

    def str_in_dict(self, stringo, dicto):
        while True:
            stringo_input = input(stringo).lower()
            if stringo_input in dicto:
                break
            else:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
        return stringo_input

    def int_in_dict(self, stringo, dicto):
        while True:
            print(Fore.CYAN + stringo)
            try:
                into_input = int(input(""))
                if into_input in dicto:
                    break
                else:
                    print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
            except:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
        return into_input

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def marktplatz(self):
        self.clear_console()
        self.logo()
        while True:
            mp_first_under = input("Do you want to choose a subcategory? Y - Yes oder N - Nein\n").lower()

            if mp_first_under == "y":
                while True:
                    mp_user_choice_uc = self.int_input("Choose a subcategory:\n"
                                        "0. Back\n"
                                        "1. Antiquitäten / Kunst\n"
                                        "2. Kameras / TV / Multimedia\n"
                                        "3. Baby / Kind\n"
                                        "4. KFZ-Zubehör / Motorradteile\n"
                                        "5. Beauty / Gesundheit / Wellness\n"
                                        "6. Mode / Accessoires\n"
                                        "7. Boote / Yachten / Jetskis\n"
                                        "8. Smartphones / Telefonie\n"
                                        "9. Bücher / Filme / Musik\n"
                                        "10. Spielen / Spielzeug\n"
                                        "11. Computer / Software\n"
                                        "12. Sport / Sportgeräte\n"
                                        "13. Dienstleistungen\n"
                                        "14. Tiere / Tierbedarf\n"
                                        "15. Freizeit / Instrumente / Kulinarik\n"
                                        "16. Uhren / Schmuck\n"
                                        "17. Games / Konsolen\n"
                                        "18. Wohnen / Haushalt / Gastronomie\n"
                                        "19. Haus / Garten / Werkstatt\n"
                                        "20. To give away Free\n")

                    if mp_user_choice_uc in range(21):
                        if mp_user_choice_uc == 0:
                            break
                        else:
                            url = build_willhaben_url(self, mp_user_choice_uc)
                            self.zeit_start = time.time()
                            self.clear_console()
                            print(Fore.GREEN + "Searching for products..." + Fore.CYAN)

                            get_willhaben_item(self, url)
                            self.marktplatz()
                    else:
                        print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)

            elif mp_first_under == "n":
                url = build_willhaben_url(self, "")
                self.zeit_start = time.time()

                get_willhaben_item(self, url)
                break
            else:
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)

obj = Willhaben()
