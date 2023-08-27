from PIL import Image, ExifTags #teste1
import exifread #teste2 pip install ExifRead
import logging #teste5

class teste:
    def teste1(self):
        #https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image        

            img = Image.open("IMG-20230526-WA0043.jpg")
            img_exif = img.getexif()
            print(type(img_exif))
            # <class 'PIL.Image.Exif'>

            if img_exif is None:
                print('Sorry, image has no exif data.')
            else:
                for key, val in img_exif.items():
                    if key in ExifTags.TAGS:
                        print(f'{ExifTags.TAGS[key]}:{val}')

    def teste2(self):
         
        # Open image file for reading (binary mode)
        f = open("G0011462.JPG", 'rb')

        # Return Exif tags
        tags = exifread.process_file(f)
        #print(tags.items())
        l = ["EXIF DateTimeDigitized", "EXIF SubSecTimeDigitized", "EXIF SubSecTimeOriginal","EXIF SubSecTime", "EXIF DateTimeOriginal"]
        for i in (l):
            if i in tags.keys():
                logging.basicConfig(level=logging.DEBUG)
                logging.debug("%s: %s (%s)", i, tags[i], tags[i].values)
        



    def teste4(self):
        
        with open("P_20170401_080843_vHDR_On.jpg", 'rb') as image_file:
            my_image = Image(image_file)

        my_image.make = "Python"
        my_image.gps_latitude_ref=exif_lat_ref
        my_image.gps_latitude=exif_lat
        my_image.gps_longitude_ref= exif_lon_ref
        my_image.gps_longitude= exif_lon

        with open("P_20170401_080843_vHDR_On.jpg", 'wb') as new_image_file:
            new_image_file.write(my_image.get_file())

TE = teste()
TE.teste2()