from collections import OrderedDict
import json
if __name__ == "__main__":
    mydict = {
        'second': '2309824902',
        'first': '2394872482',
        'zero': '2428420384'
    }

    order_list = ['zero', 'first', 'second']
    ordered_mydict = OrderedDict(mydict)

    for key in order_list:
        ordered_mydict.move_to_end(key)
    # print(json.dumps(dict(ordered_mydict), indent=4))

    ordered = {key: mydict[key] for key in order_list}
    # print(ordered)

    # rename key name but ordered are changes.
    oldkey = 'first'
    newkey = 'first_new'
    mydict[newkey] = mydict.pop(oldkey)
    # print(mydict)

    renamed = OrderedDict((newkey if k == oldkey else k, v)
                          for k, v in ordered_mydict.items())
    print(renamed)
