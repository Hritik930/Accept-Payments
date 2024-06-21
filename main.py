import qrcode

upi_id = input("Enter your upi id = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_qr = qrcode.make(google_url)

# save the qr code to image  file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_qr.save('google_qr.png')

# Display the qr codes (you may need to install pillow library)
phonepe_qr.show()
paytm_qr.show()
google_qr.show()



