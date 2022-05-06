import os
targetPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../_albums')
dirPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../keli_photo')
dirNames=['ID','group', 'life', 'others', 'work']
dirMap={
    'ID':'证件照',
    'feature':'feature',
    'group':'集体合影',
    'life':'生活照',
    'others':'其他',
    'work':'工作照',
}
pdfPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../docs/')
for root,d, files in os.walk(pdfPath):
    pdffiles = [f[:-4] for f in files]
    
for dirName in dirNames:
    print(dirPath+'/'+dirName)
    for root,d, files in os.walk(dirPath+'/'+dirName):
        print(files)
        md_filename=dirName+'.md'
        md=''
        md += '---\n'
        md += 'title: "'+dirMap[dirName]+'"\n'
        md += 'collection: albums\n'
        md += 'permalink: /album/'+dirName+'\n'
        md += '---\n'
        md += '点击可放大\n'
        md += '<style>.gallery-img{height: 150px;object-fit: cover;margin-bottom: 4px;}</style>\n'
        for file in files:
            if dirName == 'ID':
                md += '<a href="../keli_photo/'+ dirName + '/'+file+'"><img src="../keli_photo/'+ dirName + '/' +file+'" height="100"></a>\n'
            elif file[:-4] in pdffiles:
                md += '<table style="float: left; width:30%"><tr><td><a href="../keli_photo/'+ dirName + '/'+file+'"><img class="gallery-img" src="../keli_photo/'+ dirName + '/' +file+'" width="24%"></a></td></tr><tr><td><em>报道</em></td></tr></table>\n'
            else:
                md += '<table style="float: left; width:30%"><tr><td><a href="../keli_photo/'+ dirName + '/'+file+'"><img class="gallery-img" src="../keli_photo/'+ dirName + '/' +file+'" width="24%"></a></td></tr><tr><td><em></em></td></tr></table>\n'
        
        md_filename = os.path.join(targetPath, md_filename)
        print(md_filename)
        with open(md_filename, 'w') as f:
            f.write(md)
