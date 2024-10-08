##########################################################################
#
# Script to create QR Codes for Blue Hour Jazz Club member cards
# 
##########################################################################

version = '0.2 7-Oct-2024'

# install dependencies (one-time)
# pip3 install opencv-python qrcode numpy pillow
# ########################################################################


import qrcode
# example data
data = "Beat Zimmermann Socio 00003"
# output file name
filename = "socio00003.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save("Beat Zimmermann.png")

