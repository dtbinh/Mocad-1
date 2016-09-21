import tkinter as tk

class View(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.grid()
		self.canvasTab = []


	def drawWidgets(self, env):
		for i in range(env.gridsizeX):
			tempTab = []
			for j in range(env.gridsizeY):
				c = tk.Canvas(self, width = 10, height = 10, borderwidth = 0)
				c.grid(column = i, row = j)
				tempTab.append(c)
			self.canvasTab.append(tempTab)

	def updateWidgets(self, env):
		for i in range(env.gridsizeX):
			for j in range(env.gridsizeY):
				self.canvasTab[i][j].delete(tk.ALL)
				self.canvasTab[i][j].create_rectangle(0,0,11,11,fill="cyan")
				if env.agTab[i][j] is not None:
					env.agTab[i][j].drawOnCanvas(self.canvasTab[i][j])