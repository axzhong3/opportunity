import getopt, os, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "g:i:c:h", ["golden=", "input=", "column=", "help"])
except getopt.GetoptError as err:
    print "ERROR parsing args"
    usage()
    sys.exit(2)

def usage():    
    print "python -g GOLDEN_FILE -i INPUT_VECTOR_FILE -c COLUMN_NUMBER"

golden = ''
input  = ''

for o, a in opts:
    if o == "-g":
        if os.path.isfile(a):
            golden = a
        else:
            print "GOLDEN FILE does not exist"
            sys.exit(2)
    elif o in ("-i", "--input"):
        if os.path.isfile(a):
            input = a
        else:
            print "INPUT VECTOR FILE does not exists"
            sys.exit(2)
    elif o in ("-h", "--help"):
        usage()
        sys.exit()
    elif o in ("-c", "--column"):
        column = int(a)
        assert(int(a) > 0)
    else:
        print "ERROR: UNKNOWN arguments"
        sys.exit(2)

if not input or not golden:
    print "ERROR: no golden or no input vector file"
    usage()
    sys.exit(2)

gp = open(golden)
ip = open(input)
gv = []
iv = []
gv_dict = {}
 
for line in gp:
    c = int(line.split()[-1*column])
    gv.append(c)
    if not gv_dict.has_key(c):
        gv_dict[c] = 1
    else:
        gv_dict[c] += 1 
for line in ip:
    iv.append(int(line))
assert(len(iv) == len(gv))
l = len(iv)
F1 = 0
for key in gv_dict.keys():
    tp = [gv[i] == key and iv[i] == key for i in range(0, l)].count(True)
    fp = [gv[i] != key and iv[i] == key for i in range(0, l)].count(True)
    fn = [gv[i] == key and iv[i] != key for i in range(0, l)].count(True)
    precision = 1.0 * tp / (tp + fp)
    recall = 1.0 * tp / (tp + fn)
    F1 += 2.0*gv_dict[key]/len(gv)*(precision*recall)/(precision+recall)
print F1
