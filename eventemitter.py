class EventEmitter:
    def __init__(self):
        self.handler_names = {}

    def emit(self, name, *args):
        if name in self.handler_names:
            for h in self.handler_names[name]:
                h(*args)

    # Do not use lambdas if you intend to unsubscribe from the event,
    # use a function instead!
    def on(self, name, func):
        if name not in self.handler_names:
            print(f"create event {name}")  # print statement for logging purposes
            self.handler_names[name] = set()
        print(f"adding handler for event {name}")  # print statement for logging purposes
        self.handler_names[name].add(func)

    def off(self, name, func):
        if name in self.handler_names:
            print(f"remove handler for event {name}")  # print statement for logging purposes
            self.handler_names[name].remove(func)
