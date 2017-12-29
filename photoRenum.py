import os,shutil
cur_path=os.path.dirname(__file__) #取得当前路径
sample_tree=os.walk(cur_path)
output_dir = 'output2'

for dirname,subdir,files in sample_tree:
    allfiles=[]
    basename= os.path.basename(dirname)
    if basename == output_dir:
        continue
    
    for file in files:
        ext=file.split('.')[-1]
        if ext =="jpg":
            allfiles.append(file)
            
    if len(allfiles)>0:
        target_dir = dirname + '/' + output_dir
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        counter=0
        for file in allfiles:
            filename=file.split('.')[0]
            ext=file.split('.')[1]
            m_filename="p" + str(counter)
            destfile = "{}.{}".format(target_dir+'/'+m_filename,ext) #完整路径
            srcfile=dirname+ "/" + file
            print(destfile)
            shutil.copy(srcfile,destfile);
            counter += 1
        
print("完成……")