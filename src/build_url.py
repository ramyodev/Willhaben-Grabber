from colorama import Fore


def build_willhaben_url(self, uk):
    self.clear_console()
    while True:
        keyword = list(input("Select keyword:\n").strip())
        if not keyword:
            kw_rq = input("Do you want to grab products without a keyword? Y - No Keyword N - Choose Keyword\n").lower()
            if kw_rq == "y":
                break
            elif kw_rq != "y" and kw_rq != "n":
                print(Fore.RED + "--------------------\nInvalid selection!\n--------------------" + Fore.CYAN)
        else:
            break

    types = {"d": "&ISPRIVATE=1", "h": "&ISPRIVATE=0", "b": ""}
    typ = self.str_in_dict("By whom should products be grabbed?\nD - Private dealers\nH - Business Dealers\nB - Both\n", types)

    to_filter = {"+": "%2B", " ": "+", "ö": "%F6", "ü": "%FC", "ä": "%E4", "Ö": "%D6", "Ü": "%DC", "Ä": "%C4", "×": "%D7",
               "#": "%23", "!": "%21", "/": "%2F", ",": "%2C", "€": "%80", "%": "%25", "=": "%3D", "(": "%28",
               ")": "%29", "&": "%26", ";": "%3B", ",": "%2C", ":": "%3A"}

    for i, x in enumerate(keyword):
        if x in to_filter:
            keyword[i] = to_filter[x]

    keyword = "".join(keyword)

    if uk == 20:
        url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/zu-verschenken/marktplatz"  f"?rows=100" + f"&keyword={keyword}"
    else:
        while True:
            minimum_price = self.int_input("Minimum price:\n")
            maximum_price = self.int_input("Maximum price:\n")
            if minimum_price > maximum_price:
                print(Fore.RED + "---------------------------------------------------\nMinimum price cannot be higher than maximum price!\n---------------------------------------------------" + Fore.CYAN)

            else:
                break
        print(Fore.GREEN + "Please wait..." + Fore.CYAN)

        if uk != "":
            url = self.url_base + self.menu["links"][str(uk)] + f"?PRICE_FROM={minimum_price}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximum_price}" + f"&rows=25"
        else:
            url = self.url_base + f"?PRICE_FROM={minimum_price}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximum_price}" + "&rows=25"

    return url
