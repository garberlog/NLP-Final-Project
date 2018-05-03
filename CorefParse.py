from neuralcoref import Coref
from parse import parse
import spacy


def main():
    filename = "ender_tmp.txt"
    text = parse(filename)

    for x in text:
        print(x)

    results = doCoref(text)

    for x in results:
        print (x)


# Input: Text file of list of sentences
# Output: List of sentences with order index and coreference resolution
#             corefoutput.txt file with list printed out
def doCoref(text):

    # Initialize Coref object and counters
    coref = Coref()
    results = []
    linecount = 0

    # Example text options (comment out)
    # text = ["Stanley is a bird. Makayla is a fox.", "\tGive me twenty bees."]
    # text = ["Andrew could not remember how to speak. They lifted him onto the table. They checked his pulse, did other things; he did not understand it all"]

    results = resolve(text, coref)

    linecount += 1

    # for x in range(len(text)):
    #     print (text[x])
    #     print (results[x])

    fd = open("corefoutput.txt", "w")

    for y in results:
        # print (y)
        fd.write(str(y[0]) + "\n")

    fd.close()

    return results


# Assume: sentenceList is a list of sentences, lines, or some sort of sentence structure.
# Output: (Undecided)
def resolve(sentenceList, coref):

    # Create empty sentence buffer for coreference resolution
    resolved = []
    sentenceBuffer = ""

    for sentenceBuffer in sentenceList:
        # Currently attempting to use paragraphs to determine info separation.
        # Other ideas: Occurrence of new Proper Noun/title of character?
        #               Mix of both?
        if sentenceBuffer != "\n":
            # coref resolve sentence in buffer
            # oneshot = coref.one_shot_coref(sentenceBuffer)
            coref.one_shot_coref(sentenceBuffer)
            resolution = coref.get_resolved_utterances()
            # print ("Resolution = " + str(resolution))

            # do things with resolution
            resolved.append(["".join(resolution)])

        # Parse remaining info
        else:
            # oneshot = coref.one_shot_coref(sentenceBuffer)
            coref.one_shot_coref(sentenceBuffer)
            resolution = coref.get_resolved_utterances()
            resolved.append(["".join(resolution)])

    return resolved


if __name__ == "__main__":
    main()
