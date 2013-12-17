import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    langs = {'a':'a'}
    langcodes = open("codes_with_languages.txt");
    for lang in langcodes:
    	lang1 = lang.split()
    	if lang1[0] not in langs:
    		langs[lang1[0]]=lang1[1]
    datapoints = open("datapoints_wikipedia_msf.csv")
    n=0
    for line in datapoints:
    	lang_line = line.split(",");
	if lang_line[0]=="wals_code":
    		continue
    	n=n+1
    
    print "#nexus"
    print
    print "BEGIN Taxa;"
    print "DIMENSIONS ntax="+str(n)+";";
    print "TAXLABELS"
    datapoints = open("datapoints_wikipedia_msf.csv")
    n1=0
    for line in datapoints:
        lang_line = line.split(",");
    	if lang_line[0]=="wals_code":
    		continue
    	n1=n1+1
    	print "["+str(n1)+"]"+" "+"'"+langs[lang_line[0]]+"'"
    print ";"
    print "END; [Taxa]"
    print ""
    print "BEGIN Unaligned;"
    print "DIMENSIONS ntax="+str(n)+";"
    print "FORMAT"
    print "\tdatatype=STANDARD"
    print "\tmissing=0"
    print "\tsymbols=\"1 2 3 4 5 6 7 8 9\""
    print "\tlabels=left"
    print ";"
    print "MATRIX"
    datapoints = open("datapoints_wikipedia_msf.csv")
    for line in datapoints:
    	lang_line = line.split(",");
    	if lang_line[0]=="wals_code":
    		continue
    	string="'"+langs[lang_line[0]]+"'"+"\t"
    	size = len(lang_line);
    	for i in range(1,size-1):
    		t="0"
    		if lang_line[i]!="":
    			t=lang_line[i]
    		string=string+t
    	if i==n:
    		string=string+";"
    	else:
    		string=string+","
    	print string
    print "END; [Unaligned]"
    
if __name__ == '__main__':
    main()
