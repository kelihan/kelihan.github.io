import os
from os.path import isfile, join
targetPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../_albums')
dirPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../keli_photo')
dirNames=['ID', 'group', 'life', 'others', 'work']
dirMap={
    'ID':'证件照',
    'feature':'feature',
    'group':'集体合影',
    'life':'生活照',
    'others':'其他',
    'work':'工作照',
}

pdffiles = [f[:-3] for f in os.listdir('../docs/') if isfile(join('../docs/', f))]
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
        md += '点击放大\n'
        md += '<style>.gallery-img{ height: 150px;object-fit: cover;margin-bottom: 4px;}</style>\n'
        for file in files:
            if dirName == 'ID':
                md += '<a href="../keli_photo/'+ dirName + '/'+file+'"><img src="../keli_photo/'+ dirName + '/' +file+'" height="100"></a>\n'
            elif file[:-3] in pdffiles:
                md += '<figure><a href="../keli_photo/'+ dirName + '/'+file+'"><img class="gallery-img" src="../keli_photo/'+ dirName + '/' +file+'" width="24%"></a><figcaption align = "center"><b>报道</b></figcaption></figure>\n'
            else:
                md += '<a href="../keli_photo/'+ dirName + '/'+file+'"><img class="gallery-img" src="../keli_photo/'+ dirName + '/' +file+'" width="24%"></a>\n'
        
        md_filename = os.path.join(targetPath, md_filename)
        print(md_filename)
        with open(md_filename, 'w') as f:
            f.write(md)
