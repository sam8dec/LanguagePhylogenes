import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def main():
    #languages = open("languages_with_codes.txt")
    #for lang in languages:
    #	lang_code = lang.split()
    #	print lang_code[len(lang_code)-1],
    #	langname = lang.rsplit(' ', 1)[0]
    #	langname = langname.lower()
    #	langname=langname.strip()
    #	langname = langname.replace(' ','_')
    #	print langname
    
    #language_codes = open("only_codes.txt")
    #for code in language_codes:
    #	datapoints = open("datapoints.csv")
    #	for data in datapoints:
    #		data1=data.split(",")
    #		#print code.strip()," ",data1[0].strip()
    #		if code.strip()==data1[0].strip():
    #			print data
    
    
    features_of_interest = "31A,118A,30A,119A,29A,85A,28A,32A,83A,86A,40A,39A,10A,47A,73A,121A,18A,21A,84A,57A,89A,9A,90A,63A,61A,66A,79A,42A,99A,44A,87A,13A,125A,111A,50A,69A,51A,98A,127A,54A,94A,122A,7A,88A,93A,62A,26A,129A,33A,80A,48A,49A,53A,55A,6A,123A,104A,25A,27A,65A,109A,46A,117A,100A"
    
    
    datapoints = open("datapoints_wikipedia.csv")
    for line in datapoints:
    	lang_line = line.split(",");
    	str=lang_line[0]+","
    	for feature_of_interest in features_of_interest.split(","):
    		k=1
		features = open("feature_id_comma_sep.txt")
		for fid in features:
			if fid.strip()==feature_of_interest.strip():
				#print fid.strip(),k
				break
    			k=k+1
    		str=str+lang_line[k]+","
    	print str
    
if __name__ == '__main__':
    main()
