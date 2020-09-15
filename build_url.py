from colorama import Fore


def build_willhaben_url(self, uk):
    self.clear_console()
    while True:
        keyword = list(input("Keyword auswählen:\n").strip())
        if not keyword:
            kw_rq = input("Möchten Sie Produkte ohne Keyword grabben? Y - Kein Keyword N - Keyword wählen\n").lower()
            if kw_rq == "y":
                break
            elif kw_rq != "y" and kw_rq != "n":
                print(Fore.RED + "--------------------\nUngültige Auswahl!\n--------------------" + Fore.CYAN)
        else:
            break

    händler_typ = "Von wem sollen Produkte gegrabbt werden?\nP - Privat\nH - Händler\nB - Beides\n"
    types = {"p": "&ISPRIVATE=1", "h": "&ISPRIVATE=0", "b": ""}
    typ = self.str_in_dict(händler_typ, types)

    to_filter = {"+": "%2B", " ": "+", "ö": "%F6", "ü": "%FC", "ä": "%E4", "Ö": "%D6", "Ü": "%DC", "Ä": "%C4", "×": "%D7",
               "#": "%23", "!": "%21", "/": "%2F", ",": "%2C", "€": "%80", "%": "%25", "=": "%3D", "(": "%28",
               ")": "%29", "&": "%26", ";": "%3B", ",": "%2C", ":": "%3A"}

    for i, x in enumerate(keyword):
        if x in to_filter:
            keyword[i] = to_filter[x]

    keyword = "".join(keyword)

    if uk == 20:
        url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/zu-verschenken/marktplatz"  f"?rows=100" + f"&keyword={keyword}"
    elif uk != "":
        while True:
            mindest_preis = self.int_input("Mindestpreis:\n")
            maximal_preis = self.int_input("Maximalpreis:\n")
            if mindest_preis > maximal_preis:
                print(Fore.RED + "--------------------\nUngültige Eingabe!\n--------------------" + Fore.CYAN)

            else:
                break
        url = self.url_base + self.menu["links"][str(
            uk)] + f"?PRICE_FROM={mindest_preis}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximal_preis}" + f"&rows=100"
    else:
        while True:
            mindest_preis = self.int_input("Mindest Preis:\n")
            maximal_preis = self.int_input("Maximal Preis:\n")
            if mindest_preis > maximal_preis:
                print(Fore.RED + "--------------------\nUngültige Eingabe!\n--------------------" + Fore.CYAN)
            else:
                break
        print(Fore.GREEN + "Bitte warten...." + Fore.CYAN)

        url = self.url_base + f"?PRICE_FROM={mindest_preis}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximal_preis}" + "&rows=100"

    return url
