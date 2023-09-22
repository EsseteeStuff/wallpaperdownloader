baseUrl = 'https://wallpaperscraft.com'

baseResolution = [
    "3840x2400",
    "3840x2160",
    "2560x1600",
    "2560x1440",
    "2560x1080",
    "2560x1024",
    "2048x1152",
    "1920x1200",
    "1920x1080",
    "1680x1050",
    "1600x900",
    "1440x900",
    "1280x800",
    "1280x720"
]

baseCategorie = [
    "3D",
    "Abstract",
    "Animals",
    "Anime",
    "Art",
    "Black",
    "Black and white",
    "Cars",
    "City",
    "Dark",
    "Fantasy",
    "Flowers",
    "Food",
    "Holidays",
    "Love",
    "Macro",
    "Minimalism",
    "Motorcycles",
    "Music",
    "Nature",
    "Other",
    "Space",
    "Sport",
    "Technologies",
    "Textures",
    "Vector",
    "Words"
]

def savePage(content, page):
    hd = open(page, 'w')
    hd.write(content)
    hd.close()
