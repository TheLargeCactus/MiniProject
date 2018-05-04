class Question:
    def __init__(self, prompt, incorrect0, incorrect1, incorrect2, answer):
        self.prompt = prompt
        self.incorrect0 = incorrect0
        self.incorrect1 = incorrect1
        self.incorrect2 = incorrect2
        self.answer = answer
    # Returns the question prompt to the caller
    def getPrompt(self):
        return self.prompt;
    # Returns the answer to the caller
    def getAnswer(self):
        return self.answer;
    # Returns the
    def getInc0(self):
        return self.incorrect0;

    def getInc1(self):
        return self.incorrect1;

    def getInc2(self):
        return self.incorrect2;

    def checkAnswer(self, index):
        return 3 == index;  # Think that should work
