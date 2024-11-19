# Writing a Class in python

class EventStream():

    def __init__(self):
        self.value = -2
    
    def get_value(self, input):
        for i in range(input):
            self.value += 2
            print(self.value)

class OddEventStream():

    def __init__(self):
        self.value = -1
    
    def get_value(self, input):
        for i in range(input):
            self.value += 2
            print(self.value)

def print_from_stream(n, stream = EventStream()):
    stream.get_value(n)

if __name__ == '__main__':
    
    queries = int (input())

    for i in range(queries):
        stream_name, n = input().split()

        if stream_name == "even":
            print_from_stream(int(n))
        else:
            print_from_stream(int(n), OddEventStream())