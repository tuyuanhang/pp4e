"""
python cpall.py dirFrom dirTo
"""

import os, sys
maxfileload = 1000000
blksize = 1024 * 500

def copyfile(pathFrom, pathTo, maxfileload = maxfileload):
    """
    将单个文件逐字节从pathFrom复制到pathTo;
    使用二进制文件模式阻止unicode解码及换行符转换
    """
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read()
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')
        fileTo = open(pathTo, 'wb')
        while True:
            bytesFrom = fileFrom.read(blksize)
            if not bytesFrom: break
            fileTo.write(bytesFrom)

def copytree(dirFrom, dirTo, verbose=0):
    """
    将dirFrom下的内容复制到dirTo, 返回（文件，目录)数目形式的元组
    为避免在某些平台上目录名不可解码，可能需要为其名使用字节
    在Unix下可能需要更多文件类型检查：跳过链接，fifo之类
    """
    fcount = dcount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom, filename)
        pathTo = os.path.join(dirTo, filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose > 1: print('copying', pathFrom, 'To', pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Erro copying', pathFrom, 'to', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info(1))
        else:
            if verbose: print('copying dir', pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)
                below = copytree(pathFrom, pathTo) #递归进入子目录
                fcount += below[0] #加上子目录的文件数
                dcount += below[1]
                dcount += 1
            except:
                print('Error creating', pathTo, '--skipping')
                print(sys.exc_info()[0], sys.exc_info()[1])
    return (fcount, dcount)

def getargs():
    """
    获取并验证文件目录名参数，碰到错误时默认返回None
    """
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Usage error: cpall.py dirFrom dirTo')
    else:
        if not os.path.isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        elif not os.path.exists(dirTo):
            os.mkdir(dirTo)
            print('Note: dirTo was created')
            return (dirFrom, dirTo)
        else:
            print('Warning: dirTo already exists')
            if hasattr(os.path, 'samefile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
            if same:
                print('Error: dirFrom same as dirTo')
            else:
                return (dirFrom, dirTo)

if __name__ == '__main__':
    import time
    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.clock()
        fcount, dcount = copytree(*dirstuple)
        print('Copied', fcount, 'files', dcount, 'directories', end=' ')
        print('in', time.clock() - start, 'seconds')
