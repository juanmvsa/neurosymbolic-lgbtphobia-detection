from transition_amr_parser.parse import AMRParser


class AMRParser:
    def __init__(self, model_name):
        self.parser = AMRParser.from_pretrained(model_name)

    def createAMR(self, sentence):
        tokens, positions = self.parser.tokenize(sentence)
        annotations, machines = self.parser.parse_sentence(tokens)
        amr = machines.get_amr()
        return amr.to_penman(jamr=False, isi=True)

    def generateAMRTree(self, sentence):
        tokens, positions = self.parser.tokenize(sentence)
        annotations, machines = self.parser.parse_sentence(tokens)
        amr = machines.get_amr()
        amr.plot()