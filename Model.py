import math
import cv2
import psycopg2

class ifChar:

    def __init__(self, cntr):
        self.contour = cntr

        self.boundingRect = cv2.boundingRect(self.contour)

        [x, y, w, h] = self.boundingRect

        self.boundingRectX = x
        self.boundingRectY = y
        self.boundingRectWidth = w
        self.boundingRectHeight = h

        self.boundingRectArea = self.boundingRectWidth * self.boundingRectHeight

        self.centerX = (self.boundingRectX + self.boundingRectX + self.boundingRectWidth) / 2
        self.centerY = (self.boundingRectY + self.boundingRectY + self.boundingRectHeight) / 2

        self.diagonalSize = math.sqrt((self.boundingRectWidth ** 2) + (self.boundingRectHeight ** 2))

        self.aspectRatio = float(self.boundingRectWidth) / float(self.boundingRectHeight)


class PossiblePlate:

    def __init__(self):
        self.Plate = None
        self.Grayscale = None
        self.Thresh = None

        self.rrLocationOfPlateInScene = None

        self.strChars = ""


def checkIfChar(possibleChar):
    if (possibleChar.boundingRectArea > 80 and possibleChar.boundingRectWidth > 2
            and possibleChar.boundingRectHeight > 8 and 0.25 < possibleChar.aspectRatio < 1.0):

        return True
    else:
        return False


def distanceBetweenChars(firstChar, secondChar):
    x = abs(firstChar.centerX - secondChar.centerX)
    y = abs(firstChar.centerY - secondChar.centerY)

    return math.sqrt((x ** 2) + (y ** 2))

def angleBetweenChars(firstChar, secondChar):
    adjacent = float(abs(firstChar.centerX - secondChar.centerX))
    opposite = float(abs(firstChar.centerY - secondChar.centerY))

    if adjacent != 0.0:
        angleInRad = math.atan(opposite / adjacent)
    else:
        angleInRad = 1.5708

    angleInDeg = angleInRad * (180.0 / math.pi)

    return angleInDeg

def buscaInformacoes(ocrPhrase):
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "1234567",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "db_detran")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT a.PlacaVeiculo, "
            "a.Fabricante, "
            "a.Modelo, "
            "a.AnoFabricacao, " 
            "b.Descricao, "
            "COALESCE(c.Nome, c.RazaoSocial), "
            "COALESCE(c.Cpf, c.Cnpj), "
            "c.TipoProprietario " 
            "FROM tb_veiculos a "
            "INNER JOIN tb_status b ON a.CodStatus = b.CodStatus " 
            "INNER JOIN tb_proprietario c ON a.CodProprietario = c.CodProprietario "
            "WHERE a.PlacaVeiculo LIKE '" + ocrPhrase + "'")
        
        registros = cursor.fetchall()

        for r in registros:

            if r[7] == 1:
                tipoProprietario = "Pessoa Física"
            else:
                tipoProprietario = "Pessoa Jurídica"

            informacoes = ("*** Proprietário *** \n\n" +
            "Tipo: " + tipoProprietario + "\n" +
            "Nome ou Razão Social: " + r[5] + "\n" +
            "CPF ou CNPJ: " + r[6] + "\n\n" +
            "*** Veículo *** \n\n" +
            "Placa: " + r[0] + "\n" +
            "Fabricante: " + r[1] + "\n" +
            "Modelo: " + str(r[2]) + "\n" +
            "Fabricação: " + str(r[3]) + "\n\n" +
            "Situação: " + r[4] + "\n")

    except (Exception, psycopg2.Error) as error :
        print ("Erro ao conectar-se com o PostgreSQL!", error)
        
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexão com o PostgreSQL encerrada!")
    
    return informacoes