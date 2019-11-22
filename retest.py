import re
import nltk
import reader

article_text = (
    "Consumer goods have a significance that goes be- yond their utilitarian character and commercial value."
    + "This significance rests largely in their ability to carry and communicate cultural meaning (Douglas and"
    + "Isherwood 1978; Sahlins 1976). During the last decade, a diverse body of scholars has made the cultural"
    + "sig- nificance of consumer goods the focus of renewed academic study (Belk 1982; Bronner 1983;"
    + "Felson 1976; Furby 1978; Graumann 1974-1975; Hirschman 1980; Holman 1980; Leiss 1983; Levy 1978;"
    + "McCracken 1985c; Prown 1982; Quimby 1978; Rodman and Phi- libert 1985; Schlereth 1982; Solomon"
    + "1983). These scholars have established a subfield extending across the social sciences that now devotes"
    + "itself with increasing clarity and thoroughness to the study of person-object relations."
)
article_text = re.sub("[^a-zA-Z]", " ", article_text)  # removes citation
article_text = re.sub(r"\s+", " ", article_text)
formatted_article_text = re.sub("[^a-zA-Z]", " ", article_text)
formatted_article_text = re.sub(r"\s+", " ", formatted_article_text)

sentence_list = nltk.sent_tokenize(article_text)
print(sentence_list)
