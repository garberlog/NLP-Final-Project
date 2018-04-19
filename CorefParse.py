from neuralcoref import Coref
from parse import parse
from embedder import makeSentenceEmbeddings
import spacy

def main():


    coref = Coref()
    results = []
    text = parse("ender_tmp.txt")
    # text = ["Stanley is a bird. Makayla is a fox.", "\tGive me twenty bees."]
    # text = ["Ender nodded. It was a lie, of course, that it wouldn't hurt a bit. But since adults always said it when it was going to hurt, he could count on that statement as an accurate prediction of the future. Sometimes lies were more dependable than the truth."]
    for x in text:
        # singleEmbed = makeSentenceEmbeddings(x,spacy.load('en'))
        output = resolve(x, coref)
        results.append(output)
        # print (singleEmbed)

    # for x in range(len(text)):
    #     print (text[x])
    #     print (results[x])

    for x in results:
        print (x)

# Assume: sentenceList is a list of sentences, lines, or some sort of sentence structure.
# Output: (Undecided)
def resolve(sentenceList, coref):

    # Create empty sentence buffer for coreference resolution
    resolved = []
    sentenceBuffer = ""


    for x in sentenceList:
        # Currently attempting to use paragraphs to determine info separation.
        # Other ideas: Occurrence of new Proper Noun/title of character?
        #               Mix of both?
        if x != "\n":
            # add sentence to coreference buffer
            sentenceBuffer += x
        else:
            # coref resolve sentence in buffer
            # oneshot = coref.one_shot_coref(sentenceBuffer)
            coref.continuous_coref(sentenceBuffer)
            resolution = coref.get_resolved_utterances()
            resolved.append(resolution)


            # do things with resolution

            # clear sentence buffer
            sentenceBuffer = ""
            sentenceBuffer += x + " "

    # Parse remaining info
    if sentenceBuffer != "":
        # oneshot = coref.one_shot_coref(sentenceBuffer)
        coref.continuous_coref(sentenceBuffer)
        resolution = coref.get_resolved_utterances()
        resolved.append(resolution)
        # print(resolution)
        sentenceBuffer = ""

    return resolved

if __name__ == "__main__":
    main()
