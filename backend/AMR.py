from transition_amr_parser.parse import AMRParser


class AMR:
    def __init__(self, model_name):
        self.parser = AMRParser.from_pretrained(model_name)

    def createAMR(self, sentences):
        tokens_final = []
        nodes_final = [] 
        edges_final = []
        roots_final = []
        # plots_final = []
        
        for sentence in sentences:
            tokens, positions = self.parser.tokenize(sentence)
            annotations, machines = self.parser.parse_sentence(tokens)
            amr = machines.get_amr()
            tokens_final.append(amr.tokens)
            nodes_final.append(amr.nodes)
            edges_final.append(amr.edges)
            roots_final.append(amr.root)
            # plots_final.append(amr.plot())
            
        return tokens_final, nodes_final, edges_final, roots_final#, plots_final    
        #return amr.to_penman(jamr=False, isi=True)

    def generateAMRTree(self, sentence):
        tokens, positions = self.parser.tokenize(sentence)
        annotations, machines = self.parser.parse_sentence(tokens)
        amr = machines.get_amr()
        amr.plot()