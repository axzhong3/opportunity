import getopt, os, sys, sqlite3, re, glob

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:d:l:hr:", ["column_names=", "data_dir=", "label_legend=", "help", "regex"])
except getopt.GetoptError as err:
    print "ERROR parsing args"
    usage()
    sys.exit(2)

def usage():    
    print "usage: python %s [options]" % sys.argv[0]
    print " [-c, --column_names=COLUMN_NAMES.TXT]"
    print " [-l, --label_legend=LABEL_LEGEND.TXT]"
    print " [-d, --data_dir=DATA_DIR]"
    print " -r, --regex=DATA_FILES_TO_INCLUDE"

col_names = os.getcwd() + '/column_names.txt'
legend = os.getcwd() + '/label_legend.txt'
data_dir = os.getcwd()
regex = re.compile("S.*dat$")

for o, a in opts:
    if o == '-c':
        col_names = a            
    elif o == '-l':
        legend = a
    elif o == "-d":
        data_dir = a
    elif o == "-r":
        regex = re.compile(a)
    else:
        print "ERROR: UNKNOWN arguments"
        usage()
        sys.exit(2)

assert os.path.isfile(col_names), "column_name.txt does not exist" 
assert os.path.isfile(legend), "legend does not exist" 
assert(os.path.isdir(data_dir)), "data directory does not exist"

conn = sqlite3.connect(data_dir+"/data.db")
cur = conn.cursor()
col2colname = {}
colname2col = {}
colname2label = {}
def subname(name):
    name = re.sub("\^", "", name)
    name = re.sub("\s", "", name)
    name = re.sub("-", "", name)
    return name
    
def col2col(col, colname):
    colname = subname(colname)
    if colname2col.has_key(colname):
        i = 1
        while (colname2col.has_key(colname+str(i))):
            i += 1
        colname = colname + str(i)
    col2colname[int(col)] = colname
    colname2col[colname] = int(col)

# column name table
table_name = "column_names"
item_names = ["column", "column_name", "value", "unit"]
item_types = ["int" , "text", "text", "text"]
items = [" ".join(i) for i in zip(item_names, item_types)]
cur.execute("DROP TABLE IF EXISTS %s" % table_name)
cur.execute("CREATE TABLE %s(%s)" % (table_name, ', '.join(items)))
cn_regex = re.compile("Column:\s+([0-9]+)\s+([^\r]+)")
cn_regex2 = re.compile("(.+);\s*value\s*=\s*(.+),\s*unit\s*=\s*(.+)")
cf = open(col_names)

for line in cf:
    result = cn_regex.match(line)
    if result:
        result2 = cn_regex2.match(result.group(2))
        if result2:
            record = (result.group(1), ) + result2.groups()
            col2col(result.group(1), result2.group(1))
        else:
            record = (result.group(1), ) + (result.group(2), "NA", "NA")
            col2col(result.group(1), result.group(2))
        cur.execute("INSERT INTO %s VALUES(?,?,?,?)" % table_name, record)

cf.close()

# legend table
lf = open(legend)
lg_regex = re.compile("([0-9]+)\s*-\s*(\S+)\s*-\s*(\S+)")
for line in lf:
    result = lg_regex.match(line)
    if result:
        if not colname2label.has_key(result.group(2)):
            colname2label[result.group(2)] = {}
        colname2label[result.group(2)][int(result.group(1))] = subname(result.group(3))
lf.close()

# data tables
for file in os.listdir(data_dir):
    if regex.match(file):
        table_name = re.sub("\.*", "", file)
        table_name = re.sub("-", "", table_name)
        cur.execute("DROP TABLE IF EXISTS %s" % table_name)
        items = [col2colname[i+1]+' int' for i in range(len(col2colname))]
        for key in colname2label.keys():
            items[colname2col[key]-1] = key + ' text'
        print items
        cur.execute("CREATE TABLE %s(%s)" % (table_name, ', '.join(items)))        
        df = open(data_dir+'/'+file)
        for line in df:
            line_split = line.split()
            for key in colname2label.keys():
                unique_index = int(line_split[colname2col[key]-1])
                if not colname2label[key].has_key(unique_index):
                    line_split[colname2col[key]-1] = "NULL"
                else:
                    line_split[colname2col[key]-1] = colname2label[key][unique_index]
            cur.execute("INSERT INTO %s VALUES(%s)" % (table_name, ','.join(["?"]*len(col2colname))), line_split)
        df.close()
conn.commit()
conn.close()
cf.close()
