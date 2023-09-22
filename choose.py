def getPages(page):
    teller = 0
    with open(page) as f:
        for line in f:
            if line.__contains__('">Last<span class="gui-hidden-mobile"> page</span></a>'):
                myCounts = line.replace('">Last<span class="gui-hidden-mobile"> page</span></a>', '')
                myCount = []
                myCount = myCounts.split('/')
                lastPage = myCount[-1]
                myCount = lastPage.split('page')
                teller = int(myCount[1])
                teller = teller % 15
                return teller
    


def getWallpapers(page):
    with open(page) as f:
        imageUrls=[]
        for line in f:
            if line.__contains__('<a class="wallpapers__link" href="'):
                line = line.replace('<a class="wallpapers__link" href="/download/','').lstrip()
                line = line.replace('">','')
                lines = []
                lines = line.split('/')
                newUrl = "https://images.wallpaperscraft.com/image/single/" + lines[0].rstrip() + "_" + lines[1].rstrip() + ".jpg"
                imageUrls.append(newUrl)
    return imageUrls
