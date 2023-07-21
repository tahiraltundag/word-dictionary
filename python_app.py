
def main():
    word_dictionary = {
        "hi" : "merhaba, selam",
        "eyes" : "göz",
        "earth" : "dünya",
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, " : ", word_dictionary[word])

main()