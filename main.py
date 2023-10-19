import socket
from dnslib import DNSRecord, RCODE, RR, QTYPE
import json

port = 53

CACHE_FILE = 'dns_cache.json'


class SimpleDNSServer:
    def __init__(self):
        self.cache = {}
        self.load_cache()

    def load_cache(self):
        try:
            with open(CACHE_FILE, 'r') as f:
                self.cache = json.load(f)
        except FileNotFoundError:
            self.cache = {}

    def save_cache(self):
        with open(CACHE_FILE, 'w') as f:
            json.dump(self.cache, f)

    def handle_request(self, data, addr, sock):
        request = DNSRecord.parse(data)

        qname = str(request.q.qname)
        qtype = QTYPE[request.q.qtype]
        cached = "yes" if (qname in self.cache and qtype in self.cache[qname]) else "no"
        print('Request recieved for : ' + qname + ' , Type : ' + qtype +", Cached : "+cached);
        if qname in self.cache and qtype in self.cache[qname]:
            # Serve from cache
            reply = request.reply()
            addresses = self.iterative_query(qname, qtype)
            for address in addresses:
                reply.add_answer(address)
        else:
            if request.header.rd:  # Recursive query
                reply = self.recursive_query(request)
                if reply:
                    if not qname in self.cache:
                        self.cache[qname] = {}
                    self.cache[qname][qtype] = str(reply.rr[0].rdata)
            else:  # Iterative query - Note: Simplifying by using cache/recursive for this example
                reply = request.reply()
                addresses = self.iterative_query(qname, qtype)
                for address in addresses:
                    reply.add_answer(address)

        sock.sendto(reply.pack(), addr)
        self.save_cache()

    def iterative_query(self , qname , qtype ):
        ## Expects the zone info in format 'qname IN qtype dnsAddr'
        answers = RR.fromZone(qname + " IN " + qtype + " " + self.cache[qname][qtype]);
        return answers;

    def recursive_query(self, request):
        # Sending request to a real DNS server, in this case, Google's 8.8.8.8
        forwarder = ('8.8.8.8', 53)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(request.pack(), forwarder)
        data, _ = s.recvfrom(512)
        return DNSRecord.parse(data)

    def start(self):
        print("Listening for DNS queries at 127.0.0.1 ...")
        self.load_cache();
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('0.0.0.0', port))
            while True:
                data, addr = s.recvfrom(512)
                self.handle_request(data, addr, s)


if __name__ == "__main__":
    server = SimpleDNSServer()
    server.start()
