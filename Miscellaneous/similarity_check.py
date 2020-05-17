import scipy.spatial
import gensim
a = 'bake'
b = 'cook'
model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)  
print(scipy.spatial.distance.cosine(word2vec(a),word2vec(b)))
