# -*- encoding:utf-8 -*-
# python py2.py py2exe
from distutils.core import setup
import py2exe

INCLUDES = []

options = {
    "py2exe" :
        {
            "compressed" : 1, # 压缩   
            "optimize" : 2,
            "bundle_files" : 1, # 所有文件打包成一个 exe 文件  
            "includes" : INCLUDES,
            "dll_excludes" : ["MSVCR100.dll"]
        }
}


setup(
    options=options,    
    description = "this is a py2exe test",   
    zipfile=None,
    windows = [{"script":'launch.py',"icon_resources": [(1, u"softmgr.ico")]}]
    )
