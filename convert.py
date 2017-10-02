from OpenSSL import crypto

"""

  Takes a .pfx or .p12 and converts it into .pem format. 

  Files will be output as 

    - CertName.pem (Contains Public Key) and CertName.key.pem (Contains Private Key)

"""

CertName = raw_input("What's the Certificate URL?: ")
OldCertFile = raw_input("Original Certificate file?: ")
CertPass = raw_input("Cert Password?: ")
ConvertedCertFile = CertName + ".pem"
ConvertedKeyFile = CertName + ".key.pem"
# Import Original
p12 = crypto.load_pkcs12(file((OldCertFile), 'rb').read(), (CertPass))
# PEM formatted private key
print crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
# PEM formatted certificate
print crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
# Save Files
SaveFile = open(ConvertedCertFile, 'w')
SaveFileKey = open(ConvertedKeyFile, 'w')
SaveFileKey.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()))
SaveFile.write(crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate()))