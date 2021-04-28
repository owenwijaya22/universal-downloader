from downloader import download, get_links
from downloader import log
from logger import downloader_logger
def main():
    links = get_links()
    downloads = download(links)

if __name__ == "__main__":
    log()
    
        