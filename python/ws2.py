import webbrowser as wb

def workauto():
    codepath = ""
  #  os.startfile(codepath)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    urls = ["https://www.google.com/maps"]

    for url in urls:
        wb.get(chrome_path).open(url)
     #url = input("enter the website") helps to go to that particular website
workauto()
