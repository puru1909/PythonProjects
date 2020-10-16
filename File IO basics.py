#File IO Basics
#volatile-ram(jb v hm computer ko band krte h ar jitna v data hamare RAM m h wo udd jayega)
#non volatile- hard disk(isme data save rehta h) ar yha data file m save hota h
# file k ander text ho skta h,binary data,img(binary data),mp3(binary data) ye sb ko encode krke hm file m daal
# dete h ar phir mp3 player hon gya ya image viewer ho gya wo decode krta h
"""
"r"- (read mode)open file for reading- default mode
"w"- (write mode)open file for writing
"x"- (exclusive mode)Creates file if not exits and if the file is already present this operation fails
"a"- (append mode) Add  more content to a file at the end of the file
"t"- (text mode) mtlb ki hamari file m text data h like notepad,- default mode
     as a string deal krna chahta hu apni data se to textmode m kholunga
"b"- (binary mode)
"+" - ye hmlog file ko open krte h update krne k liye yani ki (read+ write) both

Question of the day:
1.func m hame docstring ko access krne k liye kya likhte h
mtlb func k docstring ko read krne ka ar print krne k kya krte h-
print(funcname.__doc__)

"""
