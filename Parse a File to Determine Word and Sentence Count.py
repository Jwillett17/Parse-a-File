def main():
    filename = input('Please enter file name: ')
    try:
        with open(filename, 'r') as f:
            sentence_count = 0
            word_count = 0
            data = f.read()
        
            sentence = data.count(".")
            sentence_count += sentence
            
            words = data.strip().split()
            word_count += len(words)
            
            print("Number of sentences is", sentence_count)
            print("Number of words is", word_count)

    except FileNotFoundError:
        print(filename + " does not exists!")


main()
