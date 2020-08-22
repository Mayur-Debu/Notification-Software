from pygame import mixer
import time
import schedule
import datetime

global water_counter
water_counter=3500

def play_music_water():

    """This function plays the music for water drinking notification"""

    global water_counter
    water_counter=water_counter-150
    mixer.init()
    mixer.music.load("Pani-Da-Rang-(Male)-Ayushmann-Khurrana.mp3")
    mixer.music.play(loops=100)

    if water_counter==0:
        mixer.music.stop()
        print("You are completely hydrated now !!!")
    else:
        print("\n********************* WATER DRINKING REMAINDER *********************")
        print("PLEASE STAY HYDRATED, YOU WILL BE MORE PRODUCTIVE!!!!!!!!!")
        print("ATleast drink 150 ml water. :-)\n")
        ch=input("Please Enter, \"DRANK / drank\" If You Hydrated Yourself: ")
        choice=ch.lower()

        if choice=="drank":
          mixer.music.stop()
          file=open("Log File.txt","a")
          date_time=datetime.datetime.now()
          file.write("Water remainder at: ["+str(date_time)+"]\n")
          file.close()

def play_music_eyes():

    """This function plays the music for eyes relaxing notification"""

    mixer.init()
    mixer.music.load("Naina_(Dangal)_128_Kbps.mp3")
    mixer.music.play(loops=100)

    print("\n********************* EYE's RELAXING REMAINDER *********************")
    print("PLEASE RELAX YOUR EYE's, THEY ARE THE REASON WHY YOU SEE THIS BEAUTIFUL WORLD !!!!!!!\n")
    ch = input("Please Enter, \"RELAXED / relaxed \" If Your Eye's Are Relaxed: ")
    choice = ch.lower()

    if choice == "relaxed":
        mixer.music.stop()
        file = open("Log File.txt", "a")
        date_time = datetime.datetime.now()
        file.write("Eye Remainder at: [" + str(date_time) + "]\n")
        file.close()

def play_music_physical():

    """This function plays the music for physical activity notification"""

    mixer.init()
    mixer.music.load("01 - Brothers Anthem - DownloadMing.SE.mp3")
    mixer.music.play(loops=100)

    print("\n********************* PHYSICAL ACTIVITY REMAINDER *********************")
    print("PLEASE DO SOME PHYSICAL ACTIVITY, TAKE A SMALL WALK, THAT COULD HELP YOU PERFORM BETTER!!!!!!!\n")
    ch = input("Please Enter, \"GOOD \ good\" If Your Eye's Are Relaxed: ")
    choice = ch.lower()

    if choice == "good":
        mixer.music.stop()
        file = open("Log File.txt", "a")
        date_time = datetime.datetime.now()
        file.write("Physical remainder at: [" + str(date_time) + "]\n")
        file.close()


# Main program starts here
if __name__ == '__main__':

 """This Software is dedicated to my mom, her name is Manisha and that's the name of my software bot ."""

 print("\n\n\n ||||----|||| WElCOME TO THE ADVANCED HEALTHY PROGRAMMER NOTIFICATION SOFTWARE ||||----||||\n")
 print("*********************************************************************************************************\n")
 print("Hi I am Manisha,",end=" ")
 print("You will be notified to drink water and take short breaks.")
 print("I will see you in a bit.")

 schedule.every(30).minutes.do(play_music_water)
 schedule.every(1).hour.do(play_music_eyes)
 schedule.every(2).hours.do(play_music_physical)
 while(True):
    schedule.run_pending()
    time.sleep(1)
