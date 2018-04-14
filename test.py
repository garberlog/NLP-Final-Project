from neuralcoref import Coref

coref = Coref()
clusters = coref.one_shot_coref(utterances=u"She loves him.", context=u"My sister has a dog.")
print(clusters)

mentions = coref.get_mentions()
print(mentions)

utterances = coref.get_utterances()
print(utterances)

resolved_utterance_text = coref.get_resolved_utterances()
print(resolved_utterance_text)
