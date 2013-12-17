import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    langs = {'a':'a'}
    #print len(langs)
    #i=1
    langcodes = open("NewList.txt");
    for lang in langcodes:
    	#print i,lang.strip()
    	#i=i+1
    	if lang.strip() not in langs:
    		langs[lang.strip()]=0
    #print len(langs)
    #print langs
    datapoints = open("datapoints_wikipedia_msf.csv")
    lc=0
    for line in datapoints:
	lang_line = line.split(",");
	if lang_line[0]=="wals_code":
		continue
	if lang_line[0] not in langs:
		continue
	string=lang_line[0]+"       "
	size = len(lang_line);
	fc=0
	for i in range(1,size-1):
		# excluding features which have more than 8 states
		if i==37 or i==49:
			continue
		t="?"
		if lang_line[i]!="":
			fc=fc+1
			t=lang_line[i]
		string=string+t
        #print lang_line[0]
        if fc>10:
        	lc=lc+1
        	#print fc 
        	print string
    print lc
    
if __name__ == '__main__':
    main()
