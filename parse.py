import re


def parse(filename):
    # filename = raw_input("file: ")
    # filename = "ender_tmp.txt"
    file = open(filename, "r")
    filestr = ""
    fileall = ""
    for line in file:
        fileall += line
        filestr += line.replace("\n", " ")

    # everything, punctuation and all
    count = 0
    quote = 0
    temp = ""
    everything = []
    ender = ".", "?", "!"  # in case delimiters changes
    for count in range(0, len(fileall)):
        char = fileall[count]
        # quote starting
        if char == "\"":
            temp += char
            if quote == 0:
                quote = 1
            else:
                # quote ending, nothing following
                if fileall[count + 1] == "\n":
                    temp += " "
                    everything.append(temp)
                    temp = ""
                    count += 1
                    quote = 0
                else:
                    temp += " "
                    quote = 0
        else:
            # in quote, continue no matter what
            if quote == 1:
                if char != "\n":
                    temp += char
                else:
                    temp += " "
            # out of quote, sentence ended
            elif char in ender:
                temp += char + " "
                everything.append(temp)
                temp = ""
            else:
                if char != "\n":
                    temp += char
                else:
                    temp += " "
    return everything


if __name__ == "__main__":
    everything = parse("ender_tmp.txt")
