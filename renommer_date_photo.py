#!/usr/bin/env python3
import os
#used on the movimentation of file
import shutil
from datetime import datetime
from PIL import Image
import exifread, logging


class PhotoOrganizer:
    """_summary_
    Photo Organizer a été conçu pour faciliter l'organisation 
    des photos, avec un nom par défaut et des dossiers par année. 
    Les paramètres peuvent être modifiés par un formulaire.
    Ce code a été produit sur la base d'une analyse inductive des données de l'auteur.
    De cette façon, il y aura des situations que le code ne couvrira pas.
    Je conseille que le code soit constamment réévalué avant utilisation.

    **MODELO DE ARQUIVO**
    Mostrar um exemplo
    Nome da Imagem - Sufixo numério de arquivo
    Numeração - Importação/Imagem/Sequência (0001)
    Adicional - Data/Dimensões/Etc
    Personalizado - Nome da Captura/Nome Anterior/Texto Personalizado

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """
    
    DATETIME_CREAT_INFO_ID = 36867 #original
    DATETIME_MODF_INFO_ID = 36868  #digitalized
    DATETIME_TAKEN_INFO_ID = 306
    FABRICANT_D_APPAREIL_PHOTO = 271

    photoExtensions = ['jpg', 'jpeg', 'png']
    videoExtensions = ['mp4', 'avi']

    #obtem a data que foto foi tirada
    def datePrisePhoto(self, file):
        """Gets and manipulate the metadata of the file

        :param file: The file location of the photo
        :type file: str
        :param self: refers to own class
            (default of py)
        :returns: a date of shooting photo
        :rtype: list
        """
        #reStructuredText Docstrings. Python's own. For great documentations.
        
        date = None
        photo = Image.open(file)
        if hasattr(photo, '_getexif'):
            info = photo._getexif()
            if info:
                #variavel constante com o indice da informação que a foto foi tirada
                if self.DATETIME_CREAT_INFO_ID in info:
                    date = info[self.DATETIME_CREAT_INFO_ID]
                    date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        photo.close()
        return date

    #obtem a data que foto foi modificada ou criada
    def dateModificationPhoto(self, file):
        date = None
        try:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        except:
            date = datetime.fromtimestamp(os.stat(file).st_mtime)
        finally:
            if date != None:
                date = date
                #teste do finally
        return date
    
    def obtenirFichierDate(self, file):
        """this sourse try to identify where is the data of the photo
            Não esta sendo usado no momento
        Args:
            file (_type_): _description_

        Returns:
            _type_: _description_
        """
        """
        #IMG-20230526-WA0043 - Padrão whats app - Acessar Modificado em
        #20210723_085747.jpg - Padrão Samsung
        #IMG_20210408_144201186 - Padrão foto tirada pelo FaceBook
        #G0011462.JPG - Padrão GOPRO - Acessar o criado em
        """
        date = None
        date = self.datePrisePhoto(file)
        if not date:
            date = self.dateModificationPhoto(file)
        return date
    
    def renommerLeFichier(self, fichier:str, nom):
        """
        Parameters
        ----------
        name : str
            The name of the file (is not optional)
        NotImplementedError
            If no file is passed in as a parameter.
        """
        #NumPy/SciPy Docstrings
        manterNomeAntigo = False
        try:
            if fichier is None:
                raise NotImplementedError("No args are not supported!")
            if manterNomeAntigo:
                nom = fichier, f"{nom}-"+fichier
                os.rename(fichier, nom)
            else:
                nom = f"{nom}."+fichier.split(".")[-1]
                os.rename(fichier, nom)
            return nom #retornava o novo nome
            #return True
        except:
            return None
        
    def video_shooting_date_created(self, file:str): 
        return None
    
    def deplaceFichier(self, fichier, date):
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
        try:
            nouveau_dossier = date.strftime('%Y')
            if not os.path.exists(nouveau_dossier):
                os.makedirs(nouveau_dossier)
            shutil.move(fichier, nouveau_dossier + '/' + fichier)
            return True
        except:
            return False
    
    def reconnaîtreModèle(self, nomFichier, dataM):
        wapp = nomFichier.split("-")
        dataNouveau = None
        for i in wapp:
            if i.isnumeric():
                try:
                    dataNouveau = datetime.strptime(i + dataM.strftime('%H%M%S'), "%Y%m%d%H%M%S")
                except:
                    print("Não era data :/")
        return dataNouveau
    
    def testerLaDifférence(self, data1, data2, tolerance: int):
        """_summary_
            Vérifie si les dates sont proches en fonction de la tolérance définie
        Returns:
            _type_: _description_
        """
        if data1 and data2:
            dias = data1 - data2
            if (dias.days > tolerance) or (dias.days < (-1 * tolerance)):
                return False
            else:
                return True 
        else:
            return False
    
    def organize(self):
        """_summary_
            Ce code fonctionnera avec des modules, pouvant offrir plusieurs possibilités
         à renommer en fonction des choix de l'utilisateur.
            Pour cela, la répartition des fonctions sera judicieuse afin qu’il n’y ait pas de redondance de code.
        """
        
        #sélectionnez les fichiers qui sont des photos et pris en charge
        photos = [
            nomFichier for nomFichier in os.listdir('.')
                if os.path.isfile(nomFichier) and any(nomFichier.lower().endswith('.' + ext.lower()) for ext in self.photoExtensions)
        ]
        for nomFichier in photos:
            """
            1 pegar a data que foi tirada
            2 pegar a data de modificação do arquivo
            3 verificar a diferença entre elas, se for pequena manter a data que foi tirada
            4 se for grande verificar o nome se tem algum padrão de data,
                se encontrar.
            5 verificar a diferença entre elas se não for grande e escolher a que estiver mais próxima
                se não tiver padrão pegar o nome do aparelho que tirou a foto e 
                perguntar o que fazer.
            não implementado 6 se o usuário escolher uma data padrão para as fotos, voltar fazendo alteração
            7 fotos que não tiverem metadados, fazer a comparação de data de modificação com o 
                padrão que for identificado no nome se nao houver padrão no nome repetir o procedimento 6.
            """
            dataShot = self.datePrisePhoto(nomFichier)
            dataMod = self.dateModificationPhoto(nomFichier)
            dateDefaut = None
            if dataShot and dataMod:
                if self.testerLaDifférence(dataShot, dataMod, 3):
                    dateDefaut = dataShot
                else:
                    dataNom = self.reconnaîtreModèle(nomFichier, dataShot)
                    if self.testerLaDifférence(dataNom, dataMod, 3):
                        dateDefaut = dataNom
            else:
                dataNom = self.reconnaîtreModèle(nomFichier, dataMod)
                if not dataNom:
                    #reconhece que é gopro
                    f = open(nomFichier, 'rb') # Open image file for reading (binary mode)
                    tags = exifread.process_file(f) # Return Exif tags
                    if "Image Make" in tags.keys():
                        if tags["Image Make"].values == "GoPro":
                            print("É gopro!")
                    f.close()
                    print("Nesse ponto, a data que a foto foi tirada \n é muito diferente"+
                           "da data que foi modificada, \n e pra piorar não tem padrão de data no nome."+
                           "\nverificar com o usuário se ele quer colocar uma data, se não, colocar nada.")
                else:
                    if self.testerLaDifférence(dataNom, dataMod, 3):
                        dateDefaut = dataMod

            #data = self.obtenirFichierDate(nomFichier)
            if dateDefaut:
                dataNom = dateDefaut.strftime('%Y%m%d-') + dateDefaut.strftime('%H%M%S')
                nomFichier = self.renommerLeFichier(nomFichier, dataNom)
                if nomFichier:
                    if not self.deplaceFichier(nomFichier, dateDefaut):
                        print("Erro ao movimentar arquivo.")

        video = [
            nomFichier for nomFichier in os.listdir('.')
                if os.path.isfile(nomFichier) and any(nomFichier.lower().endswith('.' + ext.lower()) for ext in self.videoExtensions)
        ]
        for index in range(len(video)):
            print("Encontrou video o video: " + video[index]+". No index:" + str(index))
            #self.renomeia_arquivo(nomFichier)


PO = PhotoOrganizer()
PO.organize()
