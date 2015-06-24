_BASE_URL = ""
_BASE_PARENT = 'config-root'
_BASE_PARENT_IMID = 'contrail:config-root:root'

def write(gen_file, gen_str):
    gen_file.write("%s\n" %(gen_str))
