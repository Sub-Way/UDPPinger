import time
from socket import *

serverAddr = ('127.0.0.1', 12000)
timemax = 1
total_rtt = []
count = 10
lose = 0
sum = 0
for i in range(10):

    with socket(AF_INET, SOCK_DGRAM) as clientSocket:
        clientSocket.settimeout(timemax)

        msg = ('Ping').encode()
        start = time.time()
        clientSocket.sendto(msg, serverAddr)

        try:
            msg, address = clientSocket.recvfrom(1024)
            end = time.time()
            rtt = end-start
            total_rtt.append(rtt)
            sum += rtt
            print(msg.decode() + ' ' +str(i+1) + ' ' + str(rtt)+'s')
        except timeout:
            lose = lose + 1
            print('Ping'+ ' ' + str(i + 1) + ' Request timed out')

print('MIN RTT : ' + str(min(total_rtt)) + ' MAX RTT : ' + str(max(total_rtt)) + ' AVG RTT : ' + str(sum/(count-lose)))
print('Packet loss rate : ' + str((lose/count)*100) + '%')