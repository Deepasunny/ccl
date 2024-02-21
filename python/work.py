import webbrowser as wb

def workauto():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    urls = ["https://www.google.com/maps"]

    for url in urls:
        wb.get(chrome_path).open(url)

workauto()
