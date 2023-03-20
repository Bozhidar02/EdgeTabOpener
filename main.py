import webbrowser
from time import sleep

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))


def openedge():
    for _ in range(30):
        webbrowser.get('edge').open_new_tab('https://www.bing.com/search?q=star+wars&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq'
                                            '=star+wars&sc=10-9&sk=&cvid=79773F1A90AE4672A42526DD531C174F&ghsh=0&ghacc='
                                            '0&ghpl=')
        sleep(0.1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    openedge()
