from neuralcoref import Coref


# Assume: sentenceList is a list of sentences, lines, or some sort of sentence structure.
# Output: (Undecided)
def parse(sentenceList):

    # Create empty sentence buffer for coreference resolution
    sentenceBuffer = ""

    for x in sentenceList:
        # Currently attempting to use paragraphs to determine info separation.
        # Other ideas: Occurrence of new Proper Noun/title of character?
        #               Mix of both?
        if "\t" not in x:
            # add sentence to coreference buffer
            sentenceBuffer += x + " "
        else:
            # coref resolve sentence in buffer
            resolution = coref.one_shot_coref(sentenceBuffer)

            # do things with resolution

            # clear sentence buffer
            sentenceBuffer = ""
