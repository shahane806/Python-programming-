import wikipedia
if __name__ == '__main__':
    search = input()
    search = wikipedia.summary(search, sentences=5)
    print(search)
