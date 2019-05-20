import os

imag_directory = 'C:/FER/3.godina/6.Semestar/Završni rad/SlikeZemris/'

i = 1

for filename in os.listdir(imag_directory):
    print (filename)
    os.rename(os.path.join(imag_directory,filename),  os.path.join(imag_directory,'img' + str(i) + '.jpg'))
    i = i + 1