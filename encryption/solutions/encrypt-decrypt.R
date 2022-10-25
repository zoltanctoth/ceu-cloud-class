encrypted.data <- PKI.encrypt(charToRaw("Hello, asymmetric encryption, again!"), pub.key.loaded)
write.binfile <- file("encrypted_data_file.dat", "wb")
writeBin(encrypted.data, write.binfile)
close(write.binfile)

read.binfile <- file("encrypted_data_file.dat", "rb")
reread.encrypted.data <- readBin(read.binfile, raw(), n=999999999) # 'n' says how many bytes
close(read.binfile)

encrypted.data == reread.encrypted.data

