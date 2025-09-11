import textwrap #textwrap is module in python which make a long string into multiple into multiple line

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width)) #use textwrap.wrap so that it breaks the line

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)#function call
    print(result)