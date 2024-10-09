##########################################################################
#
# Script to create QR Codes for Blue Hour Jazz Club member cards
# 
##########################################################################

version = '0.3'

# version history
# 07/10/2024 initial version (basic only)
# 09/10/2024 added styled method


# dependencies (one-time)
# pip3 install opencv-python qrcode numpy pillow
# pip install "qrcode[pil]"
# ########################################################################


import qrcode

# basic method

# input data
data = "Beat Zimmermann - Socio 00003"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save("Beat Zimmermann.png")

# styled method

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# input data
data = "Beat Zimmermann \n Socio Nº 00003"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(data)

img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), 
                    color_mask=RadialGradiantColorMask(), embeded_image_path="logo.png")
img.save("Styled.png")
