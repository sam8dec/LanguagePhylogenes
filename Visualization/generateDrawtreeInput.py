import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    d={}
    cwl = open("codes_with_languages.txt")
    file_with_codes=open("world_tree_gt10.txt","r");
    file_with_names=open("world_tree_gt10_fullnames.txt","a");
    out_st=""
    for line in cwl:
    	s=line.split()
    	d[s[0]]=s[1];
    t=0;
    for line in file_with_codes:
    	i=0
    	l=len(line)
    	for i in range(l):
    		#print i,l-3
    		if t>0:
    			t=t-1;
    			continue
    		if i<(l-3):
    			print i
			str = line[i]+line[i+1]+line[i+2]
			
			if str.isalpha():
				out_st=out_st+d[str]
				t=2
			else:
				out_st=out_st+line[i]
		else:
			out_st=out_st+line[i]
    print >>file_with_names,out_st
    
if __name__ == '__main__':
    main()
