from time import sleep
import os
from os import system, name
from colorama import colorama_text
from colorama import init
# from termcolor import colored # Will not work for Windows Terminal (DOS)

#-------------------------------------------------------------------------------------------------
# Credits: I would like to give credit to Mike Dane as I build this app from one of his videos. 
# Original Author: Mike Dane - Youtube Channel for training videos 
# Link: https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=190s
#-------------------------------------------------------------------------------------------------

# import textwrap

class Question: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# data_bank = open("questions.txt", "r")

# print(data_bank.read())



question_prompts = [
    "Question 1:\nSuppose that host A wants to send data over TCP to host B, and host B wants to send data to host A over TCP.\nTwo separate TCP connections - one for each ddirections are needed?\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 2:\nSuppose that the last SampleRTT in TCP connection is equal to 1 sec.\nThen timeout for the connection will necessarily be set to a value >=1sec?\n\n\n(a) True\n(b) False\n\nYour Answer:__", 
    "Question 3:\nUDP socket is identifed by a four-tuple:\n- Source IP\n- Source Port Number\n- Destination IP\n- Destination Port Number?\n\n(a) True\n(b) False\n\n\nYour Answer:__",
    "Question 4:\nTwo arriving TCP segments with different source IP address or source port number will\n(with the exception of a TCP segment carrying the original connection establishment request)\nbe directed to two different sockets.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 5:\nTwo UDP segments have different source IP address and/or source port numbers\nwill be directed to two different sockets.\n\n(a) True\n(b) False\n\n\nYour Answer:__",
    "Question 6:\nBefore sending a packet into a datagram network, the source must determine all of the links\nthat packet will traverse between source and destination.\n\n\n(a) True\n(b) False\n\n\nYour Answer:__",
    "Question 7:\nLayers four and five of the Internet protocol stack are implemented in the end systems\nbut not in the routers in the network core.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 8:\nThe Internet provides its applications two types of services, a TDM service and a FDM service.\n\n\n(a) True\n(b) False\n\nYour Answer:__", 
    "Question 9:\nADSL bandwith is shared.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 10:\nWith ADSL, each subscriber gets more downstream bandwidth than upstream bandwidth.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 11:\nTwisted-pair cooper wire is no longer present in computer networks.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 12:\nSuppose 10 connections traverse the same link of rate 1Gbps.\nSuppose that the client access links all have rate 5Mbps.\nThen the maximum throughput for each connection is 100Mbps.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 13:\nThe acronym API in this textbook stands for \"Advanced performance Internet\".\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 14:\nConsider a queue preceding a transmission link of rate R.\nSuppose a packet arrives to the queue periodically every 1/a seconds.\nAlso suppose all packets are of length L.\nThen the queuing delay is small and bounded as long as aL < R.\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 15:\nIn the connection flooding attack, the attacker sends a deluge of packets to the targeted host,\nclogging the target's access link with packets.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 16:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nInitially suppose there is only one link between source and destination.\nAlso suppose that the entire MP3 file is sent as one packet. The transmission delay is:\n\n\n(a) 3 Seconds\n(b) 3.05 Seconds\n(c) 50 milliseconds\n(d) none of the above\n\nYour Answer:__",
    "Question 17:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nThe end-to-end delay (transmission delay plus propagation delay) is:\n(a) 6 seconds\n(b) 3.05 seconds\n(c) 3 seconds\n(d) none of the above\n\nYour Answer:__",
    "Question 18:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nHow many bits will the source have transmitted when the first bit arrives at the destination?\n(a) 1 bit\n(b) 30,000,000 bits\n(c) 500,000 bits\n(d) non of the above\n\nYour Answer:__",
    "Question 19:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there are two links between source and destination, with one router connecting the two links.\nEach link is 5,000 km long. Again suppose the MP3 file is sent as one packet.\nSuppose there is no congession, so that the packet is transmitted onto the second link as soon as\nthe router receives the entire packet.\nThe end-to-end delay is:\n\n\n(a) 3.05 seconds\n(b) 6.1 seconds\n(c) 6.05 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 20:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose that the MP3 file is broken into 3 packets, each of 10 Mbits.\nIgnore headers that may be added to these packets.\nAlso ignore router processing delays.\nAssuming store and forward packet switching at the router, the total delay is:\n\n\n(a) 6.05 seconds\n(b) 4.05 seconds\n(c) 3.05 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 21:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there is only one link between source and destination, and there are 10 TDM channels in the link.\nThe MP3 file is sent over one of the channels.\n\nThe end-to-end delay is:\n\n\n(a) 30.05 seconds\n(b) 30 seconds\n(c) 300 microseconds\n(d) non of the above\n\nYour Answer:__",
    "Question 22:\nWe are sending a 30 Mbit MP3 file from a source host to a destination host.\nAll links in the path between source and destination have a transmission rate of 10Mbps.\nAssume that the propagation speed is 2 * 10^8 meters/sec, and the distance between source and destination is 10,000 km.\n\n\nQuestion:\nNow suppose there is only one link between source and destination, and there are 10 FDM channels in the link.\nThe MP3 file is sent over one of the channels.\n\nThe end-to-end delay is:\n\n\n(a) 30.05 seconds\n(b) 300 seconds\n(c) 3 seconds\n(d) non of the above\n\nYour Answer:__",
    "Question 23:\nReview the car-caravan example in Section 1.4 (Figure 1.17).\nAssume a propagation speed of 100 km/hr.\nSuppose the caravan travels 200 km, beginning in front of one tollbooth, passing through a second tollbototh,\nand finishing just before a third tollbooth.\nWhat is the end-to-end delay?\n\n\n(a) 64 minutes\n(b) 122 minutes\n(c) 62 minutes\n(d) 124 minutes\n\nYour Answer:__",
    "Question 24:\nReferring to the car-caravan example in Section 1.4 (Figure 1.17) again.\nSuppose now that when a car arrives at the second tollboth,\nIt proceeds through the tollbooth without waiting for the cards behind it.\nWhat is the end-to-end delay?\n\n\n(a) 122 minutes and 24 seconds\n(b) 124 minutes\n(c) 122 minutes and 12 seconds\n(d) 62 minutes\n\nYour Answer:__",
    "Question 25:\nSuppose there are two links between a source and a destination.\nThe first link has transmission rate 100 Mbps and the second link has transmission rate of 10 Mbps.\n Assuming that the only traffic in the network comes from the source,\nwhat is the throughput for a large file transfer?\n\n\n(a) 100 Mbps\n(b) 1 Gbps\n(c) 110 Mbps\n(d) 10 Mbps\n\nYour Answer:__",
    "Question 26:\nStore-and-forward transmission provides aid in which of the following switching approach?\n\n\n(a) Circuit Switching\n(b) Packet Switching\n(c) Both (a) and (b) are correct\n(d) Non of the above\n\nYour Answer:__",
    "Question 27:\nIn which of the approach for moving the data through a network,\nthe resources needed for the link between two end systems are \'reserved\'\nfor the duration of the communication session?\n\n\n(a) Circuit Switching\n(b) Packet Switching\n(c) Both (a) and (b) are correct\n(d) Non of the above\n\nYour Answer:__",
    "Question 28:\nWhich of the tool is used for sniffing the packet over the internet?\n\n\n(a) Minesweeper\n(b) Skype\n(c) Wireshark\n(d) Adobe Capture\n\nYour Answer:__",
    "Question 29:\nThe term defined for the time or duration wated during idle dedicated\ncircuits in circuit switching is refereed as:\n\n\n(a) Silent period\n(b) Unassigned slot\n(c) Dead circuit\n(d) Wasted Frame\n\nYour Answer:__",
    "Question 30:\nWhich of the following layer is NOT part of the TCP/IP model?\n\n\n(a) Session layer\n(b) Application layer\n(c) Network layer\n(d) Transport layer\n\nYour Answer:__",
    "Question 31:\nA compromised network device which can be controlled and leveraged by\ncyber attackers for spam distribution or distributed Denial-of-service (DDoS)\n\n\n(a) Botnet\n(b) Virus\n(c) Worms\n(d) Command-and-control server\n\nYour Answer:__",
    "Question 32:\nWhich of the following type of delay can be referred to in the scenario\nwhere a link experiences heavy traffic and the next packets in line to enter\nthe link have to experience a wait before being transmitted.\n\n\n(a) Queuing Delay\n(b) Transmission delay\n(c) Propagation delay\n(d) Instantaneous delay\n\nYour Answer:__",
    "Question 33:\nWhich of the following is used to overcome the stateless design of\nHTTP protocol and ensure stateful session?\n\n\n(a) Saved logins\n(b) Browser history\n(c) Cookie\n(d) Digital certificate\n\nYour Answer:__",
    "Question 34:\nWireless LAN access/WiFi is based on which IEEE specifications? \n\n\n(a) IEEE 802.3\n(b) IEEE 802.5\n(c) IEEE 802.1X\n(d) IEEE 802.11\n\nYour Answer:__",
    "Question 35:\nFrame is part of which layer?\n\n\n(a) Application layer\n(b) Transport layer\n(c) Network layer\n(d) Link layer\n\nYour Answer:__",
    "Question 36:\nMessage is part of which layer?\n\n\n(a) Application layer\n(b) Transport layer\n(c) Network layer\n(d) Link layer\n\nYour Answer:__",
    "Question 37:\nDatagram is part of which layer?\n\n\n(a) Application layer\n(b) Transport layer\n(c) Network layer\n(d) Link layer\n\nYour Answer:__",
    "Question 38:\nSetment is part of which layer?\n\n\n(a) Application layer\n(b) Transport layer\n(c) Network layer\n(d) Link layer\n\nYour Answer:__",
    "Question 39:\nFull form of HTTP protocol:\n\n\n(a) Hyperlinked Transer Protocol\n(b) Heavy Data Transfer Protocol\n(c) Hypertext Transfer Payload\n(d) Hypertext Transfer Protocol\n\nYour Answer:__",
    "Question 40:\nDNS caching is an import feature of DNS in order to______\n\n\n(a) Improve the delay performance\n(b) Reduce the number of DNS queries\n(c) Both (a) and (b) correct\n(d) None of the above\n\nYour Answer:__",
    "Question 41:\nSMTP or Simple Mail Transfer Protocol by default run on which protocol and service:\n\n\n(a) Port 25, UDP\n(b) Port 161, TCP\n(c) Port 25, TCP\n(d) Port 80, UDP\n\nYour Answer:__",
    "Question 42:\nWhich of the term is used to denote the time taken by a network packet to\ntravel from client to server and then back to a client?\n\n\n(a) Throughput\n(b) Round-trip time\n(c) Transmission delay\n(d) Propagation delay\n\nYour Answer:__",
    "Question 43:\nIn a network application, the software interface which is responsible\nfor the process of sending and receving messages in known as:\n\n\n(a) HTTP\n(b) UDP\n(c) TCP\n(d) Socket\n\nYour Answer:__",
    "Question 44:\nFor major video streaming companies like Youtube, Netflix, etc.,\nthe major problem of maintaining a single data center represents a single point of failure.\nTo deal with this issue, which of the technology is used:\n\n\n(a) Peer-to-Peer networks\n(b) CDN\n(c) DNS Servers\n(d) Bit-Torrent Network\n\nYour Answer:__",
    "Question 45:\nIn a Peer-to-Peer communication, it is important for client to have a connectivity\nwith a common server in order to communicate with each other?\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 46:\nWhich of the following are the classes of DNS servers architecture:\n 1.Root DNS\n 2.Top-Level Domain DNS\n 3.Authoritative DNS\n\n\n(a) Option 1 and 2 only\n(b) Option 1 and 3 only\n(c) All of the options 1, 2 and 3\n(d) Only option 1\n\nYour Answer:__",
    "Question 47:\nWhich of the following options represents the correct fields present in a four-tuple DNS Resource Record?\n\n\n(a) Number of hosts connected, Value, Type, TTL\n(b) Name, Record Expiry Date, Type, TTL\n(c) Value, TTL, Name, Renewal Date\n(d) Name, Value, Type, TTL\n\nYour Answer:__",
    "Question 48:\nSuppose Host A sends two TCP segments back to back to Host B over a TCP connection.\nThe first segment has sequence number 90; the second had sequence number 110\n\n\nHow much data is in the first segment\n\n\n(a) 25 bytes\n(b) 150 bytes\n(c) 20 bytes\n(d) 2 bytes\n\nYour Answer:__",
    "Question 49:\nSuppose Host A sends two TCP segments back to back to Host B over a TCP connection.\nThe first segment has sequence number 90; the second had sequence number 110\n\n\nSuppose that the first segment is lost but the second segment arrives at B.\nIn the acknowledgement that Host B sends to Host A,\nwhat will be the acknowledgement number?    \n\n\n(a) ACK = 90\n(b) ACK = 110\n(c) ACK = 89\n(d) ACK = 91\n\nYour Answer:__",
    "Question 50:\nThe size of the TCP RcvWindow never changes throughout the duration of the connection.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 51:\nSuppose Host A is sending Host B a large file over a TCP connection. \nThe number of unacknowledged bytes that a sends cannot exceed the size of the receiver buffer.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 52:\nHost A is sending Host B a large file over a TCP connection.\nAssume Host B has no data to send Host A.\nHost B will not send acknowledgements to Host A\nbecause Host B cannot piggyback the acknowledgements on data\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 53:\nThe TCP segment has a field in its header for RcvWindow\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 54:\nSuppose Host A is sending a large file to Host B over a TCP connection.\nif the sequence number for a segment of this connection is m,\nthen the sequence number for the subsequent segment will necessarily be m+1?\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 55:\nSuppose that the last sampleRTT in a TCP connection is equal to 1sec.\nThe current value of Timeout Interval for the connection will necessarily be > or = 1 sec.\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    "Question 56:\nSuppose Host A sends one segment with sequence number 38 and 4 bytes of data over a TCP connection to Host B.\nIn this same segment the acknowledgement number ID necessarily 42\n\n\n(a) True\n(b) False\n\nYour Answer:__",
    # "Question :\n   \n\n\n(a) True\n(b) False\n\nYour Answer:__",
    
    
    # "Question :\n   \n\n\n(a) True\n(b) False\n\nYour Answer:__",
    # "Question :\n   \n\n\n(a) M\n(b) S\n(c) W\n(d) A\n\nYour Answer:__",


]

# Answer Keys

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
    Question(question_prompts[25], "b"),
    Question(question_prompts[25], "a"),
    Question(question_prompts[27], "c"),
    Question(question_prompts[28], "a"),
    Question(question_prompts[29], "a"),
    Question(question_prompts[30], "a"),
    Question(question_prompts[31], "a"),
    Question(question_prompts[32], "c"),
    Question(question_prompts[33], "d"),
    Question(question_prompts[34], "d"),
    Question(question_prompts[35], "a"),
    Question(question_prompts[36], "b"),
    Question(question_prompts[37], "b"),
    Question(question_prompts[38], "d"),
    Question(question_prompts[39], "c"),
    Question(question_prompts[40], "c"),
    Question(question_prompts[41], "c"),
    Question(question_prompts[42], "d"),
    Question(question_prompts[43], "c"),
    Question(question_prompts[44], "b"),
    Question(question_prompts[45], "c"),
    Question(question_prompts[46], "d"),
    Question(question_prompts[47], "c"),
    Question(question_prompts[48], "a"),
    Question(question_prompts[49], "b"),
    Question(question_prompts[50], "a"),
    Question(question_prompts[51], "b"),
    Question(question_prompts[52], "a"),
    Question(question_prompts[53], "b"),
    Question(question_prompts[54], "b"),
    Question(question_prompts[55], "b"),
    # Question(question_prompts[56], ""),


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

