class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(words, list) or not isinstance(coefs, list) or len(words) != len(coefs):
            print("coef and/or list are uncorrect")
            print(-1)
            return
        nb = sum(len(word) * coef for word, coef in zip(words, coefs))
        print(nb)
    
    @staticmethod
    def enumerate_evaluate(coefs ,words):
        if not isinstance(words, list) or not isinstance(coefs, list) or len(words) != len(coefs):
            print("coef and/or list are uncorrect")
            print(-1)
            return
        nb = sum(len(word) * coefs[i]for i, word in enumerate(words))
        print(nb)

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
