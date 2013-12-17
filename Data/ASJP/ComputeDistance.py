import sys
import time

def levenshtein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    matrix = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1):
      matrix[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2):
      for sz in range(0,l1):
        if s1[sz] == s2[zz]:
          matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
        else:
          matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
    #print "That's the Levenshtein-Matrix:"
    #printMatrix(matrix)
    L = max(l1,l2)
    #print L, matrix[l2][l1]
    return float(matrix[l2][l1])/L
    #return matrix[l2][l1]

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

#levenstein distance between two list of words
def levens_dist(A,B):
	levmin = 1.0
	for wordA in A:
		for wordB in B:
			lev = levenshtein(wordA.lower(),wordB.lower())
			if lev<levmin:
				levmin=lev
	#print A,B,levmin
	#print levenshtein('liziyo','fatu')
	return levmin
	
def FeatureDistance(A1,B1):
	if A1==B1:
		return 0
	length = len(A1)
	c=0
	for i in range(length):
		if A1[i]==B1[i] and A1[i]!='?':
			c=c+1
		#if A1[i]!='?' and B[i]!='?':
		#	length=length+1
	#print c,length
	#if length==0:
	#	return 1
	return 1-(float(c)/length)
	
def main():
    dlangs={}
    langs_gt_20 = open("in_phylip_gt10.txt")
    #file_with_codes=open("parenthesis_induced_gt_20_full.txt","r");
    #file_with_names=open("parenthesis_induced_gt_20_full_langnames.txt","a");
    wals_dist={}
    wals_fs={}
    for line in langs_gt_20:
    	str1=line.split()
    	wals_dist[str1[0]]={}
    	wals_fs[str1[0]]=str1[1]
    	dlangs[str1[0]]={};
    for lang1 in dlangs:
    	for lang2 in dlangs:
    		#if lang1=="spa" and lang2=="pol":	
		wals_dist[lang1][lang2]=FeatureDistance(wals_fs[lang1],wals_fs[lang2])
		#if wals_dist[lang1][lang2]<0.5:
		#	print lang1,lang2
		#	print wals_dist[lang1][lang2]
		
    #dlangs={"rus":{}}
    c=0
    for lang in dlangs:
    	#print lang
    	lang_words = open("./LanguageFiles/"+lang+".txt");
    	c=0
    	for line in lang_words:
    		
    		c=c+1
    		if c<3:
    			continue
    		#str2=line.split(",")
    		#print str2
    		str1=line.split()
    		dlangs[lang][str1[0]]=[]
    		#print type(dlangs[lang]["1"])
    		
    		l=len(str1)
    		str2=""
    		for i in range(2,l):
    			if '%' in str1[i]:
    				str1[i]=str1[i].replace('%','')
    			#print str1[i],
    			if str1[i]=="XXX":
    				continue
    			if str1[i]=="//":
    				break
    			if ',' in str1[i]:
    				str1[i]=str1[i].replace(',','')
    				str2 = str2+str1[i]
    				dlangs[lang][str1[0]].append(str2)
    				str2=""
    				continue
    			if str2!="":
    				str2=str2+" "+str1[i]
    			else:
    				str2=str2+str1[i]
    		if str2!="":
    			dlangs[lang][str1[0]].append(str2)
    			
    #for i in range(1,101):
    #   	if str(i) in dlangs["jpn"]:
    #   		print i,dlangs["jpn"][str(i)]
    lang_dist={}
    
    for lang1 in dlangs:
    	#if lang1!="zul":
    	#	continue
    	lang_dist[lang1]={}
    	for lang2 in dlangs:
    		#if lang2!="zul":
    		#	continue
    		#print lang1,lang2
    		c=0;
    		ld=0.0;
    		for i in range(1,101):
    			key = str(i)
    			#print dlangs[lang1]
    			#if key not in dlangs[lang1] or key not in dlangs[lang2]:
    			#	print lang1,lang2,key
    			if key in dlangs[lang1] and key in dlangs[lang2]:
    				if len(dlangs[lang1][key])==0 or len(dlangs[lang2][key])==0:
    					continue
    				#print lang1,dlangs[lang1][key],lang2,dlangs[lang2][key]
    				ldist=levens_dist(dlangs[lang1][key],dlangs[lang2][key])
    				#print dlangs[lang1][key],dlangs[lang2][key],ldist
    				ld=ld+ldist
    				c=c+1
    		if c==0:
    			print lang1,lang2
    		lang_dist[lang1][lang2]=ld/c;
    		#if(lang_dist[lang1][lang2]<0.5):
    		#	print lang1,lang2,lang_dist[lang1][lang2]
    for lang in dlangs:
    	print lang+"      ",
    	for lang1 in dlangs:
    		net_dist = 0.4*wals_dist[lang][lang1]+0.6*lang_dist[lang][lang1];
    		print("%.4f" % net_dist),
    	print ""
    
if __name__ == '__main__':
    main()
