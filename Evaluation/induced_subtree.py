import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    langs = {}
    ptree = open("3_parenthesis_trees.txt");
    langcodes = open("in_fitch_gt10.txt");
    for line in langcodes:
    	lang = line.split()
    	if lang[0] not in langs:
    		langs[lang[0]]=0
    #print langs
    langs_full = {}
    for pline in ptree:
    	#print type(pline)
    	l=len(pline)
    	for i in range(l-3):
    		str = pline[i]+pline[i+1]+pline[i+2]
    		if str.isalpha():
    			langs_full[str]=0
    pline1=pline
    #cnt=0
    for lfull in langs_full:
    	if lfull not in langs:
    		pline1=pline1.replace(lfull,'')
    while(1):
    	if "(,)" in pline1:
    		pline1 = pline1.replace("(,)",'')
    	else:
    		break
    pline1=pline1.replace("(,","(")
    pline1=pline1.replace(",)",")")
    print pline1
    	
if __name__ == '__main__':
    main()
