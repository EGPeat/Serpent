import icecream as ic

def inputVal(maxSize=16, valType=int, options=False):  # unused

    while True:
        try:
            if not options:
                info = valType(input())
                if isinstance(info, str) and (len(info) > maxSize):
                    raise IndexError
                elif isinstance(info, int) and (info > maxSize):
                    raise IndexError
                return info
            else:
                info = input()
                if info.isnumeric():
                    info = int(info)
                    if info > maxSize:
                        raise IndexError
                    return info
                elif isinstance(info, str) and (len(info) > maxSize):
                    raise IndexError
                return info

        except ValueError:
            info = f"It seems you entered something that isn't a {valType}. Please try again"
        except IndexError:
            info = "you put in something that is a larger int than is allowed, or a longer string than is allowed"