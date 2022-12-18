from scraper import ScrapImg
from PCH import pch

catdict = {'침대' : 1}
scraper = ScrapImg(catdict)
scraper.NaverShopping('식탁용의자', 'D:\Workspace\SW_academy\Project1\Data\dinning_chair', 4000, 26)
# scraper.WeMakePrice('의자', 'D:\Workspace\SW_academy\Project1\Data\chair_more', 8000, 25)

# def run(path = None, query = None, catdict = None, site = None):
#     scraper = ScrapImg(catdict)
#     if site == 'NaverShopping':
#         scraper.NaverShopping(query, path)
#     if site == 'WeMakePrice':
#         scraper.WeMakePrice(query, path)
#
# def main(path = None, query = None, catdict = None, site = None):
#     if path and query and catdict and site:
#         run(path=path,query=query,catdict=catdict,site=site)
#
# if __name__ == "__main__":
#     main()