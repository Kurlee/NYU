from time import sleep
import os
from os import system, name
from colorama import colorama_text
from colorama import init

# from termcolor import colored # Will not work for Windows Terminal (DOS)




# import textwrap

class Question: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# data_bank = open("questions.txt", "r")

# print(data_bank.read())



question_prompts = [
    "Question 1:\nSuppose that host A wants to send data over TCP to host B, and host B wants to send data to host A over TCP.\nTwo separate TCP connections - one for each ddirections are needed?\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 2:\nSuppose that the last SampleRTT in TCP connection is equal to 1 sec.\nThen timeout for the connection will necessarily be set to a value >=1sec?\n\n(a) True\n(b) False\n\nYour Answer:__", 
    "Question 3:\nUDP socket is identifed by a four-tuple:\n- Source IP\n- Source Port Number\n- Destination IP\n- Destination Port Number?\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 4:\nTwo arriving TCP segments with different source IP address or source port number will\n(with the exception of a TCP segment carrying the original connection establishment request)\nbe directed to two different sockets.\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 5:\nTwo UDP segments have different source IP address and/or source port numbers\nwill be directed to two different sockets.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 6:\nBefore sending a packet into a datagram network, the source must determine all of the links\nthat packet will traverse between source and destination.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 7:\nLayers four and five of the Internet protocol stack are implemented in the end systems\nbut not in the routers in the network core.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 8:\nThe Internet provides its applications two types of services, a TDM service and a FDM service.\n(a) True\n(b) False\n\nYour Answer:__", 
    "Question 9:\nADSL bandwith is shared.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 10:\nWith ADSL, each subscriber gets more downstream bandwidth than upstream bandwidth.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 11:\nTwisted-pair cooper wire is no longer present in computer networks.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 12:\nSuppose 10 connections traverse the same link of rate 1Gbps.\nSuppose that the client access links all have rate 5Mbps.\nThen the maximum throughput for each connection is 100Mbps.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 13:\nThe acronym API in this textbook stands for \"Advanced performance Internet\".\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 14:\nConsider a queue preceding a transmission link of rate R.\nSuppose a packet arrives to the queue periodically every 1/a seconds.\nAlso suppose all packets are of length L.\nThen the queuing delay is small and bounded as long as aL < R.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 15:\nIn the connection flooding attack, the attacker sends a deluge of packets to the targeted host, clogging the target's access link with packets.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 16:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nInitially suppose there is only one link between source and destination.\nAlso suppose that the entire MP3 file is sent as one packet. The transmission delay is: \n(a) 3 Seconds\n(b) 3.05 Seconds\n(c) 50 milliseconds\n(d) none of the above\n\nYour Answer:__",
    "Question 17:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nThe end-to-end delay (transmission delay plus propagation delay) is:\n(a) 6 seconds\n(b) 3.05 seconds\n(c) 3 seconds\n(d) none of the above\n\nYour Answer:__",
    "Question 18:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nHow many bits will the source have transmitted when the first bit arrives at the destination?\n(a) 1 bit\n(b) 30,000,000 bits\n(c) 500,000 bits\n(d) non of the above\n\nYour Answer:__",
    "Question 19:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there are two links between source and destination, with one router connecting the two links. Each link is 5,000 km long.\nAgain suppose the MP3 file is sent as one packet.\nSuppose there is no congession, so that the packet is transmitted onto the second link as soon as the router receives the entire packet.\nThe end-to-end delay is:\n(a) 3.05 seconds\n(b) 6.1 seconds\n(c) 6.05 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 20:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose that the MP3 file is broken into 3 packets, each of 10 Mbits.\nIgnore headers that may be added to these packets.\nAlso ignore router processing delays.\nAssuming store and forward packet switching at the router, the total delay is:\n(a) 6.05 seconds\n(b) 4.05 seconds\n(c) 3.05 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 21:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there is only one link between source and destination, and there are 10 TDM channels in the link.\nThe MP3 file is sent over one of the channels.\nThe end-to-end delay is:\n(a) 30.05 seconds\n(b) 30 seconds\n(c) 300 microseconds\n(d) non of the above\n\nYour Answer:__",
    "Question 22:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there is only one link between source and destination, and there are 10 FDM channels in the link.\nThe MP3 file is sent over one of the channels.\nThe end-to-end delay is:\n(a) 30.05 seconds\n(b) 300 seconds\n(c) 3 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 23:\nReview the car-caravan example in Section 1.4 (Figure 1.17).\nAssume a propagation speed of 100 km/hr.\nSuppose the caravan travels 200 km, beginning in front of one tollbooth, passing through a second tollbototh,\nand finishing just before a third tollbooth.\nWhat is the end-to-end delay?\n\n\n(a) 64 minutes\n(b) 122 minutes\n(c) 62 minutes\n(d) 124 minutes\n\nYour Answer:__",
    "Question 24:\nReferring to the car-caravan example in Section 1.4 (Figure 1.17) again.\nSuppose now that when a car arrives at the second tollboth,\nIt proceeds through the tollbooth without waiting for the cards behind it.\nWhat is the end-to-end delay?\n\n\n(a) 122 minutes and 24 seconds\n(b) 124 minutes\n(c) 122 minutes and 12 seconds\n(d) 62 minutes\n\nYour Answer:__",
    "Question 25:\nSuppose there are two links between a source and a destination.\nThe first link has transmission rate 100 Mbps and the second link has transmission rate of 10 Mbps.\n Assuming that the only traffic in the network comes from the source,\nwhat is the throughput for a large file transfer?\n\n\n(a) 100 Mbps\n(b) 1 Gbps\n(c) 110 Mbps\n(d) 10 Mbps\n\nYour Answer:__",

]


questions = [
    Question(question_prompts[0], "b"), 
    Question(question_prompts[1], "b"), 
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "b"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "b"),
    Question(question_prompts[17], "c"),
    Question(question_prompts[18], "c"),
    Question(question_prompts[19], "b"),
    Question(question_prompts[20], "a"),
    Question(question_prompts[21], "a"),
    Question(question_prompts[22], "d"),
    Question(question_prompts[23], "c"),
    Question(question_prompts[24], "d"),

]

 
# sleep(4)
init()
print("\n\n")
print("Welcome to Computer Networking Quiz!\n\n")
# print(colored("Welcome to Computer Networking Quiz!\n\n", 'green', 'on_red'))


begin = input("Would you like to begin? Yes or No: \n")

if begin == "yes" or begin == "Yes":
    print("Let's Start! \n")
else: 
    print("Thanks for trying, goodbye :")

def run_test(questions):
    score = 0
    for question in questions:
        os.system("title Computer Networking Sample Test") 
        os.system("cls") # clears the screen must use import os
        sleep(1)
        answer  = input(question.prompt)
        os.system("cls") # clears the screen must use import os
        if answer == question.answer and answer != True:
            score += 1
            print("\nThe Answer: " + answer + " Correct\n\n-----------------------------------------------------\n\n")
            sleep(1)
        else:
            print("\nThe Answer: " + answer + " Incorrect\n\n-----------------------------------------------------\n\n")
            sleep(1)
    
    print("\n\n\n\n")
    os.system("cls")                   
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")



run_test(questions)

