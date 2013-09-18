'''
	Yipiii text parser (for the translation job) 
	
	This script parses tpl files, extracts english texts, removes duplicates
	and stores them in a single text file  
'''
import os

textlist = []
directory = os.path.join("c:\\docs\\yipiii\\templates-v2")
# files = ['.#standard.tpl.1.16']
for root, dirs, files in os.walk(directory):
    for file in files:
        try:
            print 'Open ', file, '...' 
            f = open(directory +'\\' + file, 'r')
        except IOError:
                print 'cannot open:', file
                continue

        print file, '...'
        content = f.read()
        index = 0
        while True: 
            end_pos = content.find("\"|t}", index)
            if end_pos <> -1:
                        begin_pos = content.rfind("{\"", index, end_pos)
                        str = content[begin_pos + 2 : end_pos]
                        textlist.append(str)
                        index = end_pos + 1 
            else:
                        break

        f.close()		

print 'Total Number of strings found: ', len(textlist)

print 'Removing duplicates...'
cleanlist = []
while len(textlist)>0:
    str = textlist[0]
    cleanlist.append(str)
    while True:
        try:
            textlist.remove(str)
        except ValueError:
            break

print 'Number of unique strings: ', len(cleanlist)

fout = open('translate_output_'+ repr( len(cleanlist) ) + '.txt', 'w')
for str in cleanlist:
	fout.write( str + "\n\n" )

fout.close();	
print "Unique strings saved in file!"	


