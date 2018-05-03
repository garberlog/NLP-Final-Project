from neuralcoref import Coref
from parse import parse


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

    results = resolve(text, coref)

    # fd = open("corefoutput.txt", "w")
    # for y in results:
    #     fd.write(str(y[0]) + "\n")
    # fd.close()

    return results


# Assume: sentenceList is a list of sentences, lines, or some sort of sentence structure.
# Output: (a list of resolved sentences (the index))
def resolve(sentenceList, coref):

    # Create empty sentence buffer for coreference resolution
    resolved = []

    for sentenceBuffer in sentenceList:
        # Currently attempting to use paragraphs to determine info separation.
        # Other ideas: Occurrence of new Proper Noun/title of character?
        #               Mix of both?

        # if sentenceBuffer != "\n":
            # coref resolve sentence in buffer
            # oneshot = coref.one_shot_coref(sentenceBuffer)
        coref.one_shot_coref(unicode(sentenceBuffer, "UTF-8"))
        resolution = coref.get_resolved_utterances()
        resolved.append(["".join(resolution)])
        # else:
        #     # oneshot = coref.one_shot_coref(sentenceBuffer)
        #     coref.one_shot_coref(unicode(sentenceBuffer, "UTF-8"))
        #     resolution = coref.get_resolved_utterances()
        #     resolved.append(["".join(resolution)])

    return resolved


if __name__ == "__main__":
    main()
