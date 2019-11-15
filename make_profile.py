# encoding: utf-8
# @Time : 2019-09-24 12:47
# author : liuwangxuezhang
__author__ = 'Ted'

from PIL import Image

head = "ted.jpeg"
logo = "add.png"

source = Image.open(head)
add = Image.open(logo)

mod_add = add.resize(source.size)

source.paste(mod_add,(0,0),mod_add)
source.save("final.png")




