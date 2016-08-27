from graphics import *

def draw_new_number(number, size):
	win = GraphWin('Number', size*28, size*28) # give title and dimensions
	counter = 0
	for pixel in number:
		pt1 = Point(size*(counter%28), size*((counter-1)//28))
		pt2 = Point(size*(1+(counter%28)), size*(1+((counter-1)//28)))
		rec = Rectangle(pt1,pt2)
		col = color_rgb(255-int(pixel*255), 255-int(pixel*255), 255-int(pixel*255))
		rec.setOutline(col)
		rec.setFill(col)
		rec.draw(win)
		counter=counter+1
	win.getMouse()
	#win.close()
    
def update_number(number, size, win):
	counter = 0
	for pixel in number:
		pt1 = Point(size*(counter%28), size*((counter-1)//28))
		pt2 = Point(size*(1+(counter%28)), size*(1+((counter-1)//28)))
		rec = Rectangle(pt1,pt2)
		col = color_rgb(255-int(pixel*255), 255-int(pixel*255), 255-int(pixel*255))
		rec.setOutline(col)
		rec.setFill(col)
		rec.draw(win)
		counter=counter+1
