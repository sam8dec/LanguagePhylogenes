import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    languages = open("LANGUAGE_NAMES.txt")
    languages_wals = open("languages.csv")
    wals_code={:}
    for line in languages_wals:
    		details = line.split(",")
    		wals_code[details[1]]=details[0]
    #print d
    for line in languages:
    	wikipedia_languages = line.split(",")
    #print wikipedia_languages
    for language in wikipedia_languages:
    	if language in wals_code:
    		print language," ",wals_code[language]
    		#a=[]
    	else:
    		#print language
    		a=[]
    
if __name__ == '__main__':
    main()
