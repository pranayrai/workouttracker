#!/bin/python
import os
import datetime
records = 'records' # a log to store all the information.
now = datetime.datetime.now()

# A function to retrieve infroamtion about your workout
def retrieve():		
        target = input("Set your goal : ")
        started = now.strftime("%H:%M")
        input("Press Enter after you complete your workout")
        did = input("How far did you run: ")
        now2 = datetime.datetime.now()
        ended = now2.strftime("%H:%M")
        with open(records, "a") as myfile:
                myfile.write("workout type " + workout + "\n" + "target " + target + "\n" + "time started " + started + "\n" + "time ended " + ended + "\n" + "How many you did " + did + "\n")
print ("-------------------------------------------------------\n\n Running application\n\n")
print ("\n\n What will you be doing today? \n\n1) Lifting\n2) Running\n3) Situps\n4) Squats\n5) Pushups\n\n-------------------------------------------------------")
workout = input()
with open(records, "a") as myfile:
        day = now.strftime("%Y-%m-%d-%H:%M")
        myfile.write(day + "\n")
if workout == "1":
        FreeorBench = input("Free weights or bench presses: ")
        if FreeorBench == "bench":
                weight = input("Enter weight of weights: ")
                target = input("Enter the number of reps you want to do: ")
                started = now.strftime("%H:%M")
                input("Press Enter when done")
                now2 = datetime.datetime.now()
                ended = now2.strftime("%H:%M")
                did = input("Enter the number of reps you did: ")
                with open(records, "a") as myfile:
                        myfile.write("workout type " + workout + FreeorBench + "\n")
                        myfile.write("weight " + weight + "\n")
                        myfile.write("target " + target + "\n")
                        myfile.write("time started " + started + "\n")
                        myfile.write("time ended " + ended + "\n")
                        myfile.write("Number of reps done " + did + "\n")
		elif FreeorBench == "free":
				weight = input("Enter weight of weights: ")
                target = input("Enter the number of reps you want to do: ")
                started = now.strftime("%H:%M")
                input("Press Enter when done")
                now2 = datetime.datetime.now()
                ended = now2.strftime("%H:%M")
                did = input("Enter the number of reps you did: ")
                with open(records, "a") as myfile:
                        myfile.write("workout type " + workout + "\n")
                        myfile.write("weight " + weight + "\n")
                        myfile.write("target " + target + "\n")
                        myfile.write("time started " + started + "\n")
                        myfile.write("time ended " + ended + "\n")
                        myfile.write("Number of reps done " + did + "\n")
elif workout > "1":
        retrieve()

else:
        print ("Command not found")
        sys.exit()
