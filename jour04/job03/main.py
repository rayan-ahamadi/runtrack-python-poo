from rectangle import Rectangle
from parallélépipède import Parallélépipède

rec = Rectangle(5,10)
d= rec.getDimension()
p = rec.périmètre()
s = rec.surface()
print("Dimension : {} \npérimètre : {} \nsurface : {}".format(d,p,s))