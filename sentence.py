import nltk

class Sentence:
    def __init__(self):
        self.topic_word = 0.0
        self.transition_word = 0.0
        self.punctuation = 0.0
        self.valid = False

        def get_topic_word(self):
            return self.topic_word

        def get_transition_word(self):
            return self.transition_word

        def get_punctuation(self):
            return self.punctuation

        def get_valid(self):
            return self.valid

        def set_topicword(self, topic):
            assert type(topic) == str
            return topic

        def set_transition_word(self, transition):
            assert type(transition) == str
            return transition

        def set_punctuation(self, punctuation):
            assert type(punctuation) == str
            return punctuation

        def set_valid(self, valid):
            assert type(valid) == bool
            return valid
