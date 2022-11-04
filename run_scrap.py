from scraper import ScrapImg
from PCH import pch

catdict = {'모션베드' : 1}
scraper = ScrapImg(catdict)
scraper.NaverShopping('모션베드', 'D:\Workspace\SW_academy\Project1images')
scraper.WeMakePrice('모션베드', 'D:\Workspace\SW_academy\Project1images')

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