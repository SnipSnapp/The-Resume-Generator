from scapy.all import *
#ALWAYS RUN IN PROD
TTL=1
while True:
  Cool_guy_mac = Ether(src='FF:FF:FF:FF:FF:FF', dst= 'FF:FF:FF:FF:FF:FF')/IP(src='0.0.0.0',dst='0.0.0.0',ttl=TTL)/ICMP()
  TTL = TTL + 1
  sendp(Cool_guy_mac)
  if TTL > 10:
    TTL=1
