import os, sys                     #for reaching files in the system
import soundfile as sf         
from soundfile import SoundFile    #for reading chracteristic of soundfiles
import numpy as np                 
from scipy.io.wavfile import read  #for reading data as numpy array
import math                        #for calculating dB levels
import simpleaudio as sa           
from pydub import AudioSegment     #for manipulating wav files

path='C:/Users/emine/Desktop/'

#Changing subtype of file into 16-PCM
for file in os.listdir(path):                                           #for all files in path

  if (file.endswith('.wav')):   
    myfile=SoundFile(path+file)    
    print(myfile.subtype_info)                                     #find subtype of  file

    if(myfile.subtype_info != 'Signed 16 bit PCM'):                   
        name= file.rsplit('.',1)                                        #find name of file
        data, samplerate = sf.read(path+file)                           #read data from file                                     
        sf.write(path+name[0]+'16BIT.wav',data, samplerate, 'PCM_16')   #write data into new file as 16 BIT
        os.remove(path+file)                                            #remove old file               

#Increasing volume of the sound   
for file in os.listdir(path):                                           #for all files in path

  if(file.endswith('.wav')):
    samprate, wavdata = read(path+file)                                 #read data as numpy array
    abs_data= abs(wavdata)                                              #take absolute value of data                 
    max_data=np.amax(abs_data)                                          #find maximum value of data 
    dbs=20*math.log(max_data,10)                                        #find max dB level
    print(dbs,'dB')                                                    
    if(dbs<87):                                                         #87 chosen as threshold
      sound = AudioSegment.from_file(path+file, format="wav")           
      gap=87-dbs                                                        #find gap                                                    
      HighSound=sound + gap                                             #increase volume with value of gap
      name= file.rsplit('.',1)  
      file_handle = HighSound.export(path+name[0]+'HV.wav', format="wav")    #create new file
      os.remove(path+file)                                              #remove old file
    else:
      print('Volume is sufficient')
