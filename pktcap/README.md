## 功能

使用scapy第三方库简单实现：

1. 指定网卡嗅探数据包，显示相关数据包，并可以保存到相应的文件中
2. 从指定文件中读取数据包，并显示相关数据包

## TODO

1. 完善数据包细节展示（与scapy相关的实现方法仍在寻找中）
2. 赶上tcpdump的水平

## usage

```
$ sudo python pktcap.py -h
Usage: pktcap.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --iface=INTERFACE
                        listen packets on the given interface
  -f CAPTURE_FILTER, --filter=CAPTURE_FILTER
                        provide a BPF capture filter
  -c COUNT, --count=COUNT
                        number of packets to capture
  -r READ_FILE, --read=READ_FILE
                        parse packets from the file
  -w WRITE_FILE, --write=WRITE_FILE
                        write the sniffed packets into pcap file
  -v, --verbose         print the verbose packets info
```

## example 

```
$ sudo python pktcap.py -r ppp0.pcap
23:35:15 IP / TCP 10.170.60.9:40937 > 103.192.178.117:2443 FA
23:35:15 IP / TCP 10.170.60.9:40940 > 103.192.178.117:2443 FA
23:35:15 IP / TCP 10.170.60.9:40941 > 103.192.178.117:2443 FA
23:35:15 16.6.223.240 > 45.195.111.182 icmp frag:1600 / Padding
23:35:15 16.6.223.240 > 45.195.111.182 icmp frag:1600 / Padding
23:35:15 IP / TCP 10.170.60.9:39091 > 216.58.197.100:https S
23:35:15 16.6.223.240 > 45.195.111.182 icmp frag:1600 / Padding
23:35:15 16.6.223.240 > 45.195.111.182 icmp frag:1600 / Padding
23:35:15 16.6.223.240 > 45.195.111.182 icmp frag:1600 / Padding
23:35:15 IP / TCP 10.170.60.9:39095 > 216.58.197.100:https S
```

