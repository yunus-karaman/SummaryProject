import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
nltk.download("punkt_tab",quiet=True)
original_text = input(".txt uzantılı özetlenecek metin belgesini giriniz: ")
summary_text = input(".txt uzantılı özetin koyulacağı  metin belgesini giriniz: ")
# Dosyayı açın ve metni okuyun
with open(f"{original_text}.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Cümlelere ayırma
sentences = sent_tokenize(text)

# Metindeki kelimeleri tokenle
words = word_tokenize(text.lower())

# Durma kelimeleri (stop words) filtrele
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

# Kelime sıklığına göre dağılım oluştur
freq_dist = FreqDist(filtered_words)

# En sık geçen kelimeler
most_common_words = nlargest(10, freq_dist, key=freq_dist.get)

# Cümlelerin skorlanması (kelime frekansı bazında)
sentence_scores = {}
for sentence in sentences:
    sentence_words = word_tokenize(sentence.lower())
    score = sum(freq_dist[word] for word in sentence_words if word in most_common_words)
    sentence_scores[sentence] = score

# Skorları yüksek olan cümleleri sıralayıp seçmek
summary_sentences = nlargest(2, sentence_scores, key=sentence_scores.get)

# Özeti yazdır
summary = " ".join(summary_sentences)
with open(f"{summary_text}.txt", mode="w") as myNewFile:
        myNewFile.write(summary)
