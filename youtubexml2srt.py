# Usage: python youtubexml2srt.py source.xml output.srt

from xml.dom.minidom import parse
import datetime
import sys
i=1
dom = parse(sys.argv[1])
out = open(sys.argv[2], 'w')
body = dom.getElementsByTagName("transcript")[0]
paras = body.getElementsByTagName("text")
for para in paras:
    out.write(str(i) + "\n")
    seginic = float(para.attributes['start'].value)
    segend = float(para.attributes['dur'].value) + seginic
    out.write('0'+str(datetime.timedelta(seconds=seginic)).replace('.',',').replace("000", "") + ' --> ' + '0' + str(datetime.timedelta(seconds=segend)).replace('.',',').replace("000", "") + "\n")
    for child in para.childNodes:
        if child.nodeName == 'br':
            out.write("\n")
        elif child.nodeName == '#text':
            out.write(unicode(child.data).encode('utf=8'))
    out.write("\n\n")
    i += 1
