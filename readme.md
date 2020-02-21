# Python event emitter. Based on observable pattern and node.js eventEmitter

Usage:

```
def view1_on_click(key, id):
    print("view1_on_click says", key, id)


def view2_on_click(key, id):
    print("view2_on_click says", key, id)


emitter = EventEmitter()
emitter.on("click", view1_on_click)
emitter.on("click", view2_on_click)
emitter.emit("click", "hallo", 1)
emitter.off("click", view2_on_click)
emitter.emit("click", "hallo", 2)
```

Output:

```
create event click
adding handler for event click
adding handler for event click
view2_on_click says hallo 1
view1_on_click says hallo 1
remove handler for event click
view1_on_click says hallo 2
```
