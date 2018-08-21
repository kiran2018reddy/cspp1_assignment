def load_stopwords(filename)
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text_ = text.lower()
    text_list = text_.split(" ")
    text_list = ["".join([j if ord(j) in range(ord('a'), ord('z')+1) \
                else "" for j in i]) for i in text_list]
    stop_words = load_stopwords("stopwords.txt")
    text_list = [i for i in text_list if i not in stop_words]

    return text_list

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    indexx_ = {}
    docs_cleaned = [word_list(i) for i in docs]
    for doc in docs_cleaned:
        for i in doc:
            if i not in indexx_:
                indexx_[i] = [(indx_, doc_.count(i)) \
                for indx_, doc_ in enumerate(docs_cleaned) if i in doc_]
    return indexx_

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents =[]
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
