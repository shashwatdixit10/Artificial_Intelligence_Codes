class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chaining(self):
        inferred_facts = set()
        while True:
            new_inferences = False
            for r in self.rules:
                ant, cons = r
                if all(f in self.facts or f in inferred_facts for f in ant) and cons not in self.facts:
                    self.facts.add(cons)
                    inferred_facts.add(cons)
                    new_inferences = True
            if not new_inferences:
                break

    def print_facts(self):
        print("Facts in the Knowledge Base:")
        for fact in self.facts:
            print(fact)


kb = KnowledgeBase()
kb.add_fact('A')
kb.add_fact('B')
kb.add_rule((['A'], 'C'))
kb.add_rule((['B'], 'D'))
kb.add_rule((['C', 'D'], 'E'))
print("Initial state of the knowledge base:")
kb.print_facts()
kb.forward_chaining()
print("\nAfter applying forward chaining:")
kb.print_facts()
