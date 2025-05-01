from transformers import pipeline

# classifier = pipeline("sentiment-analysis")
# res = classifier("I've been waiting for a HuggingFace course my whole life.")
# print(res)
#
# res2 = classifier([
#     "I've been waiting for a HuggingFace course my whole lift.", "I hate this so much!"
# ])
#
# print(res2)

# classfier = pipeline("zero-shot-classification")
# result = classfier("machine learning is a very hard course!", candidate_labels=['education', "business"])
# print(result)

generator = pipeline("text-generation")
g = generator("Hi, lili. Very happey to meet you! I'm very glad to introduced to you. I am a")
print(g)