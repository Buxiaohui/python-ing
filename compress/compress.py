import os
import os.path
import zipfile



class ZFile(object):

    def __init__(self, filename, mode='r', basedir=''):
        print('mode is %s'%mode)
        self.filename = filename
        self.mode = mode
        if self.mode in ('w', 'a'):
            self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)
        else:
            self.zfile = zipfile.ZipFile(filename, self.mode)
        self.basedir = basedir
        if not self.basedir:
            self.basedir = os.path.dirname(filename)

    def addfile(self, path, arcname=None):
        print('addfile--path is %s' % path)
        path = path.replace('//', '/')
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = ''
        '''有两种方式，一种是把一个文件写入一个已经存在的zip文件中，另一种是写入一个字符串writestr'''
        self.zfile.write(path, arcname)

    def addfiles(self, paths):
        for path in paths:
            print('addfiles--each path is %s'%path)
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    def close(self):
        self.zfile.close()

    def extract_to(self, path):
        for p in self.zfile.namelist():
            self.extract(p, path)

    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            open(f, 'wb').write(self.zfile.read(filename))


'''
mode为
'w'：创建一个zipfile
'a'：追加到zipfile。
如果是写入，则还可以跟上第三个参数：
compression=zipfile.ZIP_DEFLATED ：注意 ZIP_DEFLATED是压缩标志，如果使用它需要编译了zlib模块
compression=zipfile.ZIP_STORED ：而ZIP_STORED只是用zip进行打包，并不压缩
'''
# 接受的参数是元组类型
def create(zfile, files):
    print('zfile is %s, files is %s'%(zfile,files))
    z = ZFile(zfile, 'w')
    print('new z is %s' % z)
    z.addfiles(files)
    z.close()


def extract(zfile, path):
    print('extract-- path is %s'%path)
    z = ZFile(zfile)
    z.extract_to(path)
    z.close()

create('files/origin_01.zip',('files/origin_00.jpg','files/origin_01.jpg'))
extract('files/origin_01.zip',('./'))