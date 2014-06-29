# -*- coding: utf-8 -*-
#==============================================================
#
#   ウディタ付属合成器のデフォキャラ用パーツ分離スクリプト
#   グラフィック合成器\Graphics\デフォルト規格 内の各パターンを1枚ずつpngに分割します。
#
#   Copyright (c) 2014 Keita Nakazawa
#   Released under the MIT license
#   http://opensource.org/licenses/mit-license.php
#
#==============================================================

from PIL import Image
import os
import os.path
import sys

argvs = sys.argv
argc = len(argvs)

allparts = [u"装飾", u"追加", u"頭", u"頭追加", u"肌", u"服", u"目"]

dirnames = [u"下", u"左下", u"左", u"右下", u"右", u"左上", u"上", u"右上"]
outdirname = "out"

if argc < 2:
    print(u"Param too small amount")

else:
    path = argvs[1]

    # todo:以下もすべてパラメータから指定できるようにする
    xnum = 6
    ynum = 4
    ptnnum = 3

    parts_w = 120 / xnum
    parts_h = 112 / ynum

    print(u"Param:" + path)

    folder_levels = path.split("\\")

    for partname in allparts:

        print(u"[{0}]".format(partname))

        dir_name = os.path.sep.join(folder_levels) + partname

        outdirpath = dir_name + os.path.sep + outdirname

        if os.path.isdir(outdirpath) == False:
            os.makedirs(outdirpath)

        filelist = os.listdir(dir_name)

        currentno = 1
        for filepath in filelist:
            path = dir_name + os.path.sep + filepath
            if os.path.isdir(path) == False :
                img_in = Image.open(path)
                xlist = range(0, xnum-1)
                ylist = range(0, ynum-1)
                filename = filepath.split(os.path.sep)[-1].split(".")[0]
                for y in ylist:
                    for x in xlist:
                        cropbox = (int(x * parts_w), int(y * parts_h), int((x+1) * parts_w), int((y+1) * parts_h))
                        img_out = img_in.crop(cropbox)
                        savepath = "{0}{1}{2}_{3}_{4}.png".format(outdirpath, os.sep, filename, dirnames[int((y * xnum + x) / 3)], str(int(x) % int(xnum)))
                        img_out.save( savepath, "PNG")
                        print(u"\t完了[{0}/{1}]：{2}".format(currentno, len(filelist), filename))
                currentno+=1
