##########################################################################
#
# Script to create QR Codes for Blue Hour Jazz Club member cards
# 
##########################################################################

version = '1.1'

# version history
# v0.1 07/10/2024 initial version (basic only)
# v0.2 09/10/2024 added styled method for vertical bars and gradient
# v0.3 added pandas for handling member data
# v0.4 converted whole dataframe to type str
# v0.5 added batch import functionality
# v0.6 changed formatting of data string for QR code text
# v1.0 first fully functional version published
# v1.1 moved QR code files to subfolder
# v1.2 added Nombre to file name

# dependencies (one-time)
# pip3 install opencv-python qrcode numpy pillow pandas
# pip install "qrcode[pil]"
# ########################################################################


import qrcode
import pandas as pd
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


# Prompt for import filename
fileinput = str(input("Introduce el nombre del fichero.csv de socios: "))
if not ".csv" in fileinput:
    fileinput += ".csv"   

# Load data from CSV
df = pd.read_csv(fileinput)
df = df.astype(str)
print()
print(df)
print()

# insert prompt to check and proceed or abort
# WIP

# create QR code for each row

for ind in df.index:
    print("Nombre: " + df['Nombre'][ind] + chr(10),
          "Socio: " + df['Socio'][ind] + chr(10), 
          "Tipo Socio: " + df['Membresia'][ind] + chr(10), 
          "Valido hasta: " + df['validez'][ind] + chr(10)),
              
    # input data and generate QR code with email address as filename.png

    data = "Nombre: " + df['Nombre'][ind] + chr(10) + "Socio: " + df['Socio'][ind] + chr(10) + "Tipo Socio: " + df['Membresia'][ind] + chr(10) + "Valido hasta: " + df['validez'][ind]
    
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(), 
                        color_mask=RadialGradiantColorMask(), embeded_image_path="logo.png")
    qrCodeFile = "Tarjetas\\" + df["Nombre"][ind] + " - " + df["email"][ind] + ".png"
    img.save(qrCodeFile)