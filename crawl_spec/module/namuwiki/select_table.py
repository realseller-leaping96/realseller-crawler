def select_table(soup):
    table = ""
    if soup.select(".wiki-heading-content > .wiki-paragraph > div > .wiki-table-wrap > .wiki-table"):
        table = soup.select(".wiki-heading-content > .wiki-paragraph > div > .wiki-table-wrap > .wiki-table")[0]
    elif soup.select(".wiki-heading-content > .wiki-table-wrap > .wiki-table"):
        table = soup.select(".wiki-heading-content > .wiki-table-wrap > .wiki-table")[0]
    else:
        pass

    return table