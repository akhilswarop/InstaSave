from datetime import datetime
import requests
import re
import sys

print(''' 

01001001 01101110 01110011 01110100 01100001 01010011 01100001 01110110 01100101 
                        [Coded By Sameera a.k.a άλφα Χ]

''')

def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def download_image_video():

    url = input("Please enter image URL: ")
    x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                print("Downloading the image...")
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                response = requests.get(final).content
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                f = open(filename + '.jpg', 'wb')
                f.write(response)
                f.close
                print("Image downloaded successfully")

            if final == "video": 
                msg = input("You are trying to download a video. Do you want to continue? (Yes or No): ".lower())
                if msg == "yes":
                    print("Downloading the video...")
                    extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                    video_link = extract_video_link.group()
                    final = re.sub('meta property="og:video" content="', '', video_link)
                    response = requests.get(final).content
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    f = open(filename + '.mp4', 'wb')
                    f.write(response)
                    f.close
                    print("Video downloaded successfully")
                if msg == "no":
                    exit()  
        else:
            print("Entered URL is not an instagram.com URL.")
    except AttributeError:
        print("Unknown URL")

if connection() == True:
    try:
        while True:
            download_image_video()
            sys.exit()
    except(KeyboardInterrupt):
        print("\nProgramme Interrupted")
else:
    sys.exit(0)