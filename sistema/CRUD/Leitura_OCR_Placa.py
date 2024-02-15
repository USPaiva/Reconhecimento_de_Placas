import os
import cv2
import CRUD.Filtros as F
from CRUD.Filtros import pytesseract
class Leitura_OCR_Placa:
    
    def debug_img(img):
        cv2.imshow('Imagem', img)
        cv2.waitKey(0)
        
    def apply_filter(plate):
        #Leitura_OCR_Placa.debug_img(plate)
        gray = F.Filtros.get_grayscale(plate)
        #Leitura_OCR_Placa.debug_img(gray)
        thresh = F.Filtros.thresholding(gray)
        #Leitura_OCR_Placa.debug_img(thresh)
        return thresh


    def scan_plate(image):
        custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
        plate_number = (pytesseract.image_to_string(image, lang='eng', config=custom_config))
        #plate_number = (pytesseract.image_to_string(image, lang='eng'))
        #print(plate_number)
        return plate_number.strip()


    def Processamento():
        imagens_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Captura')
        _, _, filenames = next(os.walk(imagens_dir))

        # Verifica se há arquivos na pasta
        if len(filenames) == 0:
            return "Nenhum arquivo encontrado na pasta."

        # Ordena a lista de nomes de arquivos por data de modificação (o último arquivo será o último elemento)
        filenames.sort(key=lambda x: os.path.getmtime(os.path.join(imagens_dir, x)))

        # Obtém o caminho completo do último arquivo adicionado
        last_file = os.path.join(imagens_dir, filenames[-1])

        # Carrega a imagem do último arquivo
        plate = cv2.imread(last_file)

        # Aplica o filtro à imagem
        plate_filter_applied = Leitura_OCR_Placa.apply_filter(plate)
        
        #Leitura_OCR_Placa.debug_img(plate_filter_applied)
        
        # Realiza a leitura da placa
        plate_number = Leitura_OCR_Placa.scan_plate(plate_filter_applied)
        print(plate_number)
        return plate_number

