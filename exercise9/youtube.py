def shortner(list):
        return ["youtu.be/" + (x[31:]) for x in list]


videoer = [
'http://www.youtube.com/watch?v=oKI-tD0L18A',
'http://www.youtube.com/watch?v=82LCKBdjywQ',
'http://www.youtube.com/watch?v=GpNSip5gyKo' ,
'http://www.youtube.com/watch?v=rHG-JO8gIGk' ,
'http://www.youtube.com/watch?v=ZFngtBIxRPk' ,
'http://www.youtube.com/watch?v=OZBWfyYtYQY'
]

short = shortner(videoer)
for s in short:
    print(s)
