#Final project
#name: Batyr Issabekov

import math

def clean_text(txt):
    """takes txt and retursn list with words in txt"""
    s = txt
    s = s.lower()
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    s = s.replace('"', '')
    s = s.split(' ')
    return s

def sample_file_write(filename): #given
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

def sample_file_read(filename): #given
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def stem(s):
    """accepts a string, returns stem of s"""
    s = s.lower()
    if s[-1] == 'y':      #if last letter is y, changes it to i
        s = s[:-1] + 'i'
    if s[-1] == 's':
        s = s[:-1]
    if s[-3:] == 'ies': #if last three letters are ies, removes es
        s = s[:-2]
    if s[-1] == 'e':
        s = s[:-1]
    if s[-3:] == 'ing':
        s = s[:-3]
    if s[-2:] == 'ly':
        s = s[:-2]
    if s[-2:] == 'er':
        s = s[:-2]

    return s   #in total handles 7 different cases

def compare_dictionaries(d1,d2):
    """takes two dict and returns the log similarity score"""
    score = 0
    total = sum(d1.values())

    for i in d2:
        if i in d1:
            p1 = d1[i] / total
            log1 = math.log(p1)
            score += (d2[i] * log1) #step by step given
        else:
            p2 = (0.5/ total)
            log2 = math.log(p2)
            score += (d2[i] * log2)
    return score

class TextModel:
    def __init__(self, model_name):
        """accepts string and initializes attributes"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punc_frequency = {}


    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) +'\n'
        s += '  number of punctuation frequencies: '  + str(len(self.punc_frequency))
        return s

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """

        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!

        word_list = clean_text(s)


        # Template for updating the words dictionary.
        for w in range(len(word_list)):
            key = word_list[w]
            if key not in self.words:
                self.words[key] = 1 #if the word is not in dictionary, sets to 1
            else:
                self.words[key] += 1 #otherwise, adds to existing key

        # Update self.words to reflect w
        # either add a new key-value pair for w
        # or update the existing key-value pair.

        # Add code to update other feature dictionaries.

        #dictoinary word_lengths
        for i in word_list:
            length_key = len(i) #key is the lenghts of each word
            if length_key not in self.word_lengths:  #if word lengths not in dict
                self.word_lengths[length_key] = 1 #sets to one
            else:
                self.word_lengths[length_key] += 1 #otherwise, adds 1 to existing

        #dictionary word_stems
        for st in range(len(word_list)):
            stem_key = stem(word_list[st]) #goes through and stems each word
            if stem_key in self.stems: #if that word is in dict
                self.stems[stem_key] += 1 #adds 1 to existing number
            else:
                self.stems[stem_key] = 1 #otherwise, sets new 1

        #dictionary sentence_lengths
        s = s.replace('!','. ')
        s = s.replace('?','. ') #replaces each ending sentence with .
        sentence_list = s.split('. ') #split at each ending sentence
        for l in sentence_list:
            sentences = clean_text(l) #clean the text
            length = len(sentences) #count length of list
            if length in self.sentence_lengths: #is length int in dictionary
                self.sentence_lengths[length] += 1 #add 1 to it
            else:
                self.sentence_lengths[length] = 1 #otherwise, set 1 no new

        #dictionary punc_frequency
        s = s.replace('!','.')
        s = s.replace('?','.')
        s = s.replace(',','.')
        s = s.replace(':','.')
        s = s.replace(';','.') #replace all punctionation with .
        punc_list = s.split('. ') #split list at .
        for i in range(len(punc_list)):
            frequency_key = punc_list[i]
            if frequency_key in self.punc_frequency: #counts the number of .
            #by splits
                self.punc_frequency[frequency_key] +=1 #if frequency is existent, add to it
            else:
                self.punc_frequency[frequency_key] = 1 #otherwise, creates a new one
        for i in self.punc_frequency:
            self.punc_frequency[i] /= len(punc_list) # frequency of punctuation





    def add_file(self,filename):
        """adds txt filename to the model"""

        f = open(filename, 'r', encoding='utf8', errors='ignore')

        ttt = f.read()
        f.close()
        self.add_string(ttt)

    def save_model(self):
        """writes various features dictionary to files"""

        f1 = open(self.name + '_' + 'words', 'w') #given
        f1.write(str(self.words))  #for self.words
        f1.close

        f2 = open(self.name +'_' + 'word_lengths', 'w') #given
        f2.write(str(self.word_lengths)) #for self.word_lengths
        f2.close

        f3 = open(self.name +'_' + 'stems', 'w') #given
        f3.write(str(self.stems)) #for self.stems
        f3.close

        f4 = open(self.name +'_' + 'sentence_lengths', 'w') #given
        f4.write(str(self.sentence_lengths)) #for self.sentence_lengths
        f4.close

        f5 = open(self.name +'_' + 'punc_frequency', 'w') #given
        f5.write(str(self.punc_frequency)) #for self.punc_frequency
        f5.close

    def read_model(self):
        """reads the stored dictionaries from their files and assigns them to
        attributes"""

        f1 = open(self.name + '_' +'words','r') #taken from sample_file_read
        d_att = f1.read() #naming scheme from self_model
        f1.close()
        self.words = dict(eval(d_att))

        f2 = open(self.name +'_' + 'word_lengths','r') #for word_lenghts
        d_att = f2.read()
        f2.close()
        self.word_lengths = dict(eval(d_att))

        f3 = open(self.name +'_' + 'stems','r')
        d_att = f3.read()
        f3.close()
        self.stems = dict(eval(d_att))

        f4 = open(self.name +'_' + 'sentence_lengths','r')
        d_att = f4.read()
        f4.close()
        self.sentence_lengths = dict(eval(d_att))

        f5 = open(self.name +'_' + 'punc_frequency','r')
        d_att = f5.read()
        f5.close()
        self.punc_frequency = dict(eval(d_att))

    def similarity_scores(self,other):
        """compares disctionaties and returns a list of with scores"""

        score1 = compare_dictionaries(other.words, self.words) #given as example
        score2 = compare_dictionaries(other.word_lengths, self.word_lengths)
        score3 = compare_dictionaries(other.stems,self.stems)
        score4 = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        score5 = compare_dictionaries(other.punc_frequency, self.punc_frequency)

        return [score1, score2, score3, score4, score5] #shortened names, to write them faster


    def classify(self, source1, source2):
        """compares text model source to another source and determines which
        is more like the source of the called text model """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print("scores for "+ source1.name +":", scores1)
        print("scores for "+ source2.name +":", scores2)

        weighted_sum1 = 10*scores1[0] + 10*scores1[1] + 10*scores1[2] + 10*scores1[3]+10*scores1[4]
        weighted_sum2 = 10*scores2[0] + 10*scores2[1] + 10*scores2[2] +10*scores2[3]+10*scores1[4]

        if weighted_sum1> weighted_sum2:
            print(self.name, 'is more likely to come from ' + source1.name) #if total sum of 1 is larger than sum2
        elif weighted_sum2> weighted_sum1:
            print(self.name, 'is more likely to come from ' + source2.name) #other way around

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('rowling')
    source1.add_file('rowling_source_text.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')

    new1 = TextModel('wr120')
    new1.add_file('essay3.txt')
    new1.classify(source1, source2)

    new2 = TextModel('wr112')
    new2.add_file('summary_analysis.txt')
    new2.classify(source1, source2)

    new3 = TextModel('ah201')
    new3.add_file('final_research_paper.txt')
    new3.classify(source1, source2)

    new4 = TextModel('ge100')
    new4.add_file('lecture_notes.txt')
    new4.classify(source1, source2)
