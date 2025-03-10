import wikipedia

items = ["Artificial intelligence", "Machine learning", "Chiranjeevi", "Jana sena Party", "Data science", "Python programming"]
items_content = {}
for i in items:
    try:
        items_content[i] =  wikipedia.page(i).content
        # wikipedia.summary('Chiranjeevi')
    except:
        pass

items_content.keys()

from sentence_transformers import SentenceTransformer
