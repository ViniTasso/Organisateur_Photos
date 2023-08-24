#!/usr/bin/env python3
import os
#used on the movimentation of file
import shutil
from datetime import datetime
from PIL import Image


class PhotoOrganizer:
    """_summary_
    Photo Organizer a été conçu pour faciliter l'organisation 
    des photos, avec un nom par défaut et des dossiers par année. 
    Les paramètres peuvent être modifiés par un formulaire.

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """
    DATETIME_EXIF_INFO_ID = 36867
    photoExtensions = ['jpg', 'jpeg', 'png']
    videoExtensions = ['mp4', 'avi']

    #utilizada para criar dois diretórios com o ano e data da foto
    def folder_path_from_photo_date(self, file, ):
        date = self.photo_shooting_date_created(file)
        return date.strftime('%Y') #+ '/' + date.strftime('%Y-%m-%d')

    #obtem a data que foto foi tirada
    def photo_shooting_date_created(self, file):
        """Gets and manipulate the metadata of the file

        :param file: The file location of the photo
        :type file: str
        :param self: refers to own class
            (default of py)
        :returns: a date alread managed as the need
        :rtype: list
        """
        #reStructuredText Docstrings. Python's own. For great documentations.
        
        date = None
        photo = Image.open(file)
        if hasattr(photo, '_getexif'):
            info = photo._getexif()
            if info:
                #utiliza a variavel constante declarada com o indice do provavel campo que a foto foi tirada
                if self.DATETIME_EXIF_INFO_ID in info:
                    date = info[self.DATETIME_EXIF_INFO_ID]
                    date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        # if date is None:
        #     date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def getDataFile(self, file):
        date = None
        if any(file.lower().endswith('.' + ext.lower()) for ext in self.photoExtensions):
            date = self.photo_shooting_date_created(file)
        if any(file.lower().endswith('.' + ext.lower()) for ext in self.videoExtensions):
            date = self.video_shooting_date_created(file)
        return date

    def renomeia_arquivo(self, file:str):
        """
        Parameters
        ----------
        name : str
            The name of the file (is not optional)
        NotImplementedError
            If no file is passed in as a parameter.
        """
        #NumPy/SciPy Docstrings

        data = self.getDataFile(file)
        if data != None:
            #renomeia para data e hora juntos
            #data = data.strftime('%Y%m%d') + data.strftime('%H%M%S')
            #renomeia para data e horas separados por traço
            dataNome = data.strftime('%Y%m%d ') + data.strftime('%H%M%S')
            #os.path.split(file)
            dataNome = f"{dataNome}."+file.split(".")[-1]
            os.rename(file, dataNome)
            self.move_photo(dataNome, data)
            if file is None:
                raise NotImplementedError("No args are not supported!")

    def video_shooting_date_created(self, file:str): 
        return None
    
    def move_photo(self, file, data):
        """Gets and prints the spreadsheet's header columns

        @type file: str
        @param file: The name of file,  considering it's in the same directory
        @type data: Date
        @param data: Date that the picture has been taken
            (default is False)
        @returns: need to be implemented, a bool return
        @NotImplementedError: if the file is not found
        """
        #Epytext Docstrings. For Java developers.

        new_folder = data.strftime('%Y')
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)
        

    def organize(self):
        photos = [
            filename for filename in os.listdir('.')
                if os.path.isfile(filename) and any(filename.lower().endswith('.' + ext.lower()) for ext in self.photoExtensions)
        ]
        for filename in photos:
            self.renomeia_arquivo(filename)
        
        video = [
            filename for filename in os.listdir('.')
                if os.path.isfile(filename) and any(filename.lower().endswith('.' + ext.lower()) for ext in self.videoExtensions)
        ]
        for index in range(len(video)):
            print("Encontrou video o video: " + video[index]+". No index:" + str(index))
            #self.renomeia_arquivo(filename)


PO = PhotoOrganizer()
PO.organize()
