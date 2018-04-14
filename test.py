from neuralcoref import Coref

coref = Coref()
# clusters = coref.one_shot_coref(utterances=u"She loves him.", context=u"My sister has a dog.")
# print(clusters)
#
# mentions = coref.get_mentions()
# print(mentions)
#
# utterances = coref.get_utterances()
# print(utterances)
#
# resolved_utterance_text = coref.get_resolved_utterances()
# print(resolved_utterance_text)


loltest = "And Peter won't hate me anymore. I'll come home and show him that the monitor's gone, and he'll see that I didn't make it, either. That I'll just be a normal kid now, like him. That won't be so bad then. He'll forgive me that I had my monitor a whole year longer than he had his. We'll be-- not friends, probably. No, Peter was too dangerous. Peter got so angry. Brothers, though. Not enemies, not friends, but brothers-- able to live in the same house. He won't hate me, he'll just leave me alone. And when he wants to play buggers and astronauts, maybe I won't have to play, maybe I can just go read a book."

lolresult = coref.one_shot_coref(loltest)

print(lolresult)


resolved_utterance_text = coref.get_resolved_utterances()
print(resolved_utterance_text)
