import random


class Server:
    def __init__(self):
        self.score = 0
        self.next_seq = 1
        self.pending = {}
        self.responses = {}
        self.outbox = []

    def receive_score(self, seq, delta):
        self._receive(seq, ("update", delta))
        self.outbox.append((seq, "ack"))

    def return_score(self, seq):
        self._receive(seq, ("get", None))
        self.outbox.append((seq, self.responses.get(seq)))

    def _receive(self, seq, op):
        if seq < self.next_seq or seq in self.pending:
            return
        self.pending[seq] = op
        while self.next_seq in self.pending:
            kind, delta = self.pending.pop(self.next_seq)
            if kind == "update":
                self.score += delta
            else:
                self.responses[self.next_seq] = self.score
            self.next_seq += 1


class Client:
    def __init__(self):
        self.seq = 0
        self.outbox = []

    def update_score(self, delta):
        self.seq += 1
        self.outbox.append(("update", self.seq, delta))
        return self.seq

    def get_score(self):
        self.seq += 1
        self.outbox.append(("get", self.seq, None))
        return self.seq


def deliver(server, messages):
    for kind, seq, delta in messages:
        if kind == "update":
            server.receive_score(seq, delta)
        else:
            server.return_score(seq)


client = Client()
client.update_score(5)
client.update_score(-10)
client.get_score()
server = Server()
deliver(server, [client.outbox[2], client.outbox[0], client.outbox[1], client.outbox[2]])
print(server.outbox)

client = Client()
client.get_score()
client.update_score(7)
client.get_score()
client.update_score(3)
client.get_score()
gets = [m for m in client.outbox if m[0] == "get"]
server = Server()
deliver(server, list(reversed(client.outbox)) + gets)
print(server.outbox)

server = Server()
deliver(server, [client.outbox[1], client.outbox[1], client.outbox[0], client.outbox[1]] + client.outbox[2:])
print(server.outbox, server.score)

server = Server()
deliver(server, [client.outbox[1], client.outbox[2], client.outbox[2]])
print(server.outbox, server.next_seq, sorted(server.pending))

random.seed(8)
for _ in range(1000):
    client = Client()
    expected = {}
    running = 0
    for _ in range(random.randint(1, 15)):
        if random.random() < 0.6:
            d = random.randint(-10, 10)
            client.update_score(d)
            running += d
        else:
            expected[client.get_score()] = running
    msgs = client.outbox[:]
    random.shuffle(msgs)
    retries = [m for m in client.outbox if m[0] == "get"]
    server = Server()
    deliver(server, msgs + retries)
    assert len(server.outbox) == len(msgs) + len(retries)
    final = {seq: resp for seq, resp in server.outbox[len(msgs):]}
    assert final == expected
print("1000 random shuffled orders all correct")
