import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.size = (260,480)
class PopUps(FloatLayout):
	pass
class BMI_PopUp(FloatLayout):
	def bmi_calculate(self):
		try:
			mass = int(self.ids.weight.text)
			height = int(self.ids.height.text)
			height_meter = (height * 0.0254)**2
			result = mass / height_meter
			ans = str(result)
			self.ids.bmianswer.text = ans
			if (result <= 18.5 ):
				self.ids.review.text = " UNDERWEIGHT"
			elif (result > 18.5 and result <= 24.9):
				self.ids.review.text ="Healthy but How long?"
			elif (result > 24.9 and result <= 29.9):
				self.ids.review.text ="OverWeight"
			elif(result > 29.9 and result <= 34.9):
				self.ids.review.text = "Obesity first stage. Phatt !"
			elif (result > 34.9 and result <= 39.9):
				self.ids.review.text = "Obesity second stage. fucking fat"
			else:
				self.ids.review.text = "Damn!! Elephant Man.You Die soon"

		except :
			pass
class Quadric_Pop(FloatLayout):
	def quadric_calculate(self):
		try:
			xa = int(self.ids.a2.text)
			xb = int(self.ids.b.text)
			xc = int(self.ids.c.text)
			calculation_positive =((-(xb) + ((xb**2) - 4*(xa)*(xc))**(1/2))/(2*xa))
			cp = str(calculation_positive)
			calculation_negative =((-(xb) - ((xb**2) - 4*(xa)*(xc))**(1/2))/ (2*xa))
			cn = str(calculation_negative)
			self.ids.answer1.text = cp
			self.ids.answer2.text = cn
		except :
			self.ids.answer1.text = "Error!"
			self.ids.answer2.text = "Error!"

class nCr_Pop(FloatLayout):
	def comb(self):
		try:
			xn = int(self.ids.n.text)
			xr = int(self.ids.r.text)
			if (xn>xr):
				xc = (xn - xr)
				sum1 = xn
				last1 = 1
				for i in range(0, xn):
					i += 1
					while (sum1 != 1):
						sum1 -= 1
						last1 *= xn * sum1
				answer1 = last1 / (xn ** (xn - 2))

				sum2 = xr
				last2 = 1
				for i in range(0, xr):
					i += 1
					while (sum2 != 1):
						sum2 -= 1
						last2 *= xr * sum2
				answer2 = last2 / (xr**(xr - 2))

				sum3 = xc
				last3 = 1
				for i in range(0, xc):
					i += 1
					while (sum3 != 1):
						sum3 -= 1
						last3 *= xc * sum3
				answer3 = last3 / (xc ** (xc - 2))

				combination = answer1/(answer2*answer3)
				comb = str(combination)
				self.ids.combination_answer.text = comb

			elif(xn == xr):
				self.ids.combination_answer.text = "1"

			else:
				self.ids.combination_answer.text = " n must be >= r"
		except :
			self.ids.combination_answer.text = "  	    ERROR"

class MainScreen(Screen):
	def widgets(self):
		Grids = GridLayout
		Floats = FloatLayout
	def One(self):
		num = "1"
		self.ids.answer.text += num
	def Two(self):
		num = "2"
		self.ids.answer.text += num
	def Three(self):
		num = "3"
		self.ids.answer.text += num
	def Four(self):
		num = "4"
		self.ids.answer.text += num
	def Five(self):
		num = "5"
		self.ids.answer.text += num
	def Six(self):
		num = "6"
		self.ids.answer.text += num
	def Seven(self):
		num = "7"
		self.ids.answer.text += num
	def Eight(self):
		num = "8"
		self.ids.answer.text += num
	def Nine(self):
		num = "9"
		self.ids.answer.text += num
	def Zero(self):
		num = "0"
		self.ids.answer.text += num
	def DoubleZero(self):
		num = "00"
		self.ids.answer.text += num
	def Plus(self):
		num = "+"
		self.ids.answer.text += num
	def Minus(self):
		num = "-"
		self.ids.answer.text += num
	def Multiply(self):
		num = "*"
		self.ids.answer.text += num
	def Divide(self):
		num = "/"
		self.ids.answer.text += num
	def Exponent(self):
		num = "**"
		self.ids.answer.text += num


	def DeleteAll(self):
		self.ids.answer.text = ""

	def Delete(self):
		self.dels = self.ids.answer.text[:-1]
		self.ids.answer.text = self.dels

	def Bracket_Init(self):
		sign = "("
		self.ids.answer.text += sign

	def Bracket_Fin(self):
		sign = ")"
		self.ids.answer.text += sign
	def Dot(self):
		sign = "."
		self.ids.answer.text += sign
	def Root(self):
		sign = "√"
		self.ids.answer.text += "**(1/"





	def EqualsTo(self):
		try:
			function = str(eval(self.ids.answer.text))
			self.ids.answer.text = function

		except :
			self.ids.answer.text = "ERROR"

class Equations(Screen):
	def widgets(self):
		grd = GridLayout()

	def WholeEquation(self):
		PopUp = WholeExponent_Pop()
	def BMI_Pop(self):
		Popup = BMI()
	def Qdrics(self):
		Popup = QuadricEQuation()
	def PermutationCombination(self):
		Popup = nCr_expan()

	def RemoveOnClick_height(self):
		self.ids.height.text = " "
	def RemoveOnClick_weight(self):
		self.ids.weight.text = " "

	def bmi_calculate(self):
		self.hait = self.ids.height.text
		self.ozon = self.ids.weight.text
		self.calculate = (self.hait// self.ozon)
		self.ids.height.text = self.calculate
def WholeExponent_Pop():
    EqPop = PopUps()
    EqiPp =  Popup(title= "Whole Exponents" , content = EqPop , size_hint=(None,None) , size = (200,300) , background_color = (1,0,0.2))
    EqiPp.open()
def BMI():
    BmPop = BMI_PopUp()
    BmPop =  Popup(title= "Body Mass Index" , content = BmPop , size_hint=(None,None) , size = (200,300) , background_color = (0.1,0.4,0.2))
    BmPop.open()
def QuadricEQuation():
	QdPop = Quadric_Pop()
	QdPop = Popup(title="Quadric Equation", content=QdPop, size_hint=(None, None), size=(200, 300),  background_color=(0.1, 0.9, 0.2))
	QdPop.open()
def nCr_expan():
	ExPop = nCr_Pop()
	ExPop = Popup(title="Permutation Combination", content=ExPop , size_hint=(None, None), size=(200, 300),  background_color=(0.1, 0.4, 0.9))
	ExPop.open()



class WindowManager(ScreenManager):
	pass

kv = Builder.load_string("""
WindowManager:
	MainScreen:
	Equations:
	
<MainScreen>:
	name: "Main"
	
	GridLayout:
		cols: 4
		row_force_default: True
		row_default_height: 50
		
		Button:
			text: "("
			background_color: 239/255 , 62/255, 91/255, 1
			on_release: root.Bracket_Init()		
		Button:
			text: ")"
			background_color: 239/255 , 62/255, 91/255, 1
			on_release: root.Bracket_Fin()		
		Button:
			text: "."
			background_color: 239/255 , 62/255, 91/255, 1
			on_release: root.Dot()		
		Button:
			text: "*^√"
			background_color: 239/255 , 62/255, 91/255, 1
			on_release: root.Root()
	
		Button:
			text: "+"
			background_color: 246/255 , 143/255, 160/255, 1
			on_press: root.Plus()
		Button:
			text: "-"
			background_color: 246/255 , 143/255, 160/255, 1
			on_press: root.Minus()
		Button:
			text: "x"
			background_color: 246/255 , 143/255, 160/255, 1
			on_press: root.Multiply()
		Button:
			text: "/"
			background_color: 246/255 , 143/255, 160/255, 1
			on_press: root.Divide()
								
	
	FloatLayout:
	
		TextInput: 
			id:answer
			font_size : 25
			multiline : False
			size_hint: 1 , 0.14	
			pos_hint: {"x":0 , "y" : 0.66}
			
		
	
		Button: 
			id: exponent
			text: "^"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0 , "y" : 0 }
			background_color: 75/255 , 37/255, 109/255, 1
			on_release: root.Exponent()
			
		Button: 
			id: zeros
			text: "00"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.2375 , "y" : 0 }
			background_color: 75/255 , 37/255, 109/255, 1
			on_release: root.DoubleZero()
			
		Button: 
			id: zero
			text: "0"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.475 , "y" : 0 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Zero()
		Button: 
			id: equals
			text: "="
			size_hint: 0.2780 ,0.164
			pos_hint: { "x" : 0.7125 , "y" : 0 }
			background_color: 63/255 , 100/255, 126/255, 1
			on_press: root.EqualsTo()


		Button: 
			id: seven
			text: "7"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0 , "y" : 0.164 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Seven()
		Button: 
			id: eight
			text: "8"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.2375 , "y" : 0.164 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Eight()
		Button: 
			id: nine
			text: "9"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.475 , "y" : 0.164}
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Nine()
		Button: 
			id: findeq
			text: "Find EQ"
			size_hint: 0.2780 , 0.164
			pos_hint: { "x" : 0.7125 , "y" : 0.164 }
			background_color: 149/255 , 212/255, 122/255, 1
			on_release: 
				app.root.current = "equations"
				root.manager.transition.direction = "up"
			
	
		Button: 
			id: four
			text: "4"
			size_hint: 0.2375 ,  0.164
			pos_hint: { "x" : 0 , "y" : 0.328 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Four()
			
		Button: 
			id: five
			text: "5"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.2375 , "y" : 0.328 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Five()
		Button: 
			id: six
			text: "6"
			size_hint: 0.2375 , 0.164
			pos_hint: { "x" : 0.475 , "y" : 0.328 }
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.Six()
		Button: 
			id: deleteall
			text: "Delete All"
			size_hint: 0.2780 , 0.164
			pos_hint: { "x" : 0.7125 , "y" : 0.328 }
			background_color: 149/255 , 212/255, 122/255, 1
			on_release: root.DeleteAll()


		Button:
			id: one 
			text: "1"
			size_hint: 0.2375 ,  0.164
			pos_hint: { "x" : 0 , "y" : 0.492 } 			
			background_color: 170/255 , 160/255, 200/255, 1	
			on_press: root.One()
			
				

		Button:
			id: two 
			text: "2"
			size_hint: 0.2375 ,0.164
			pos_hint: { "x" : 0.2375, "y" : 0.492 } 
			background_color: 170/255 , 160/255, 200/255, 1				
			on_press: root.Two()

		Button: 
			id: three 
			text: "3"
			size_hint:0.2375 ,0.164
			pos_hint: { "x" : 0.475, "y" :  0.492 } 
			background_color: 170/255 , 160/255, 200/255, 1			
			on_press: root.Three()

		Button: 
			id: delete
			text: "Delete"
			size_hint:0.2780 , 0.164
			pos_hint: { "x" : 0.7125 , "y" : 0.492 }
			background_color: 149/255 , 212/255, 122/255, 1
			on_press: root.Delete() 			

<Equations>:
	name: "equations"
	
	GridLayout:
		cols: 2 
		Button: 
			markup : True
			text: "[b]Whole Exponents[b]"
			background_color: 0.1,1,0.8,0.3
			on_release: root.WholeEquation()
			
		Button:
			markup : True
			text: "[b]BMI[b]"
			background_color: 0.8,0.1,0.1,0.3
			on_release: root.BMI_Pop()
			
		Button:
			markup : True
			text:"[b]Quadraic Formula[b]"
			background_color: 0.1,0.5,0.8,0.3
			on_release: root.Qdrics()
			
		Button: 
			markup : True
			text: "[b] nCr ![b]" 
			background_color: 0.1,0.1,0.8,0.3
			on_release: root.PermutationCombination()
	FloatLayout:
		Button: 
			markup : True
			font_size: 12
			text: "[b]Back[b]"			
			background_color: 1,1,1,1
			size_hint: 0.18,0.16
			pos_hint: { "x" : 0.385 , "y" : 0.385 }		
		Button: 
			markup : True
			font_size: 12
			text: "[b]Back[b]"			
			background_color: 0,0,0,1
			size_hint: 0.15,0.13
			pos_hint: { "x" : 0.40 , "y" : 0.4 }
			on_release: 
				app.root.current = "Main"
				root.manager.transition.direction = "left"


<PopUps@Popup>:
	id: WholeEqu
	
	TextInput: 
		markup: True
		font_size: 10
		multiline: False
		pos_hint: { "x" : 0 , "y" : 0.83}
		size_hint: 1, 0.15
		text: "(a+b)^2 = a^2 + 2ab + b^2"
	TextInput: 
		markup: True
		font_size: 10
		multiline: False
		pos_hint: { "x" : 0 , "y" : 0.667}
		size_hint: 1, 0.15
		text: "(a^3 + b^3) = a^3 +3(a^2)(b) + 3(a)(b^3) + b^3)"	
	TextInput: 
		markup: True
		font_size: 10
		multiline: False
		pos_hint: { "x" : 0 , "y" : 0.50}
		size_hint: 1, 0.15
		text: "(a^3+b^3)=(a+b)(a^2 + ab + b^2))" 	
	TextInput: 
		markup: True
		font_size: 10
		multiline: False
		pos_hint: { "x" : 0 , "y" : 0.35}
		size_hint: 1, 0.15
		text: "(2ab+2bc+2ca)=(a+b+c)^2-(a^2+b^2+c^2)" 

<BMI_PopUP@Popup>:
	id: bmi
	TextInput:
		id : weight
		hint_text: "enter your weight:(kg)"
		background_color: 0.4,0.1,0.22, 0.4
		size_hint: 1, 0.2
		pos_hint: { "x" : 0 , "y" : 0.83}
		multiline: False
		on_double_tap: weight.text = " "
		
	TextInput:
		id: height
		hint_text: "enter your height:(inches)"
		background_color: 0.04,0.31,0.22, 0.4
		size_hint: 1, 0.2
		pos_hint: { "x" : 0 , "y" : 0.64}
		multiline: False
		on_double_tap: height.text = " "
		
		
	Button: 
		markup: True
		text: "[b]Calculate[b]"
		size_hint: 0.43 , 0.15
		pos_hint: { "x" : 0.28 , "y" : 0.43 }	
		background_color: 65/255, 105/255 , 225/ 255 , 1
		on_press: root.bmi_calculate()
	
						
	TextInput:
		id: bmianswer
		markup: True
		hint_text: "		  You BMI is : "
		background_color:  255/255, 255/25 , 255/220, 0.2
		size_hint: 1, 0.2
		pos_hint: { "x" : 0 , "y" : 0.21}
		multiline: False
		on_double_tap: bmianswer.text = " " 		

	TextInput:
		id: review
		markup: True
		hint_text: "			  review"
		background_color: 255/250, 255/235 , 255/215, 0.2
		size_hint: 1, 0.2
		pos_hint: { "x" : 0 , "y" : 0.01}
				
		
<Quadric_Pop@Popup>:
	id: qdric
	TextInput:
		id : a2
		hint_text: "a^2"
		background_color: 0.5,0.1,0.22, 0.4
		size_hint: 0.33, 0.2
		pos_hint: { "x" : 0 , "y" : 0.80}
		multiline: False
		on_double_tap: a2.text = " "
		
	TextInput:
		id : b
		hint_text: "+-(b)"
		background_color: 0.1,0.3,0.22, 0.4
		size_hint: 0.33, 0.2
		pos_hint: { "x" : 0.334 , "y" : 0.80}
		multiline: False
		on_double_tap: b.text = " "

	TextInput:
		id : c
		hint_text: "+-(c)"
		background_color: 0.1,0.1,0.22, 0.4
		size_hint: 0.33, 0.2
		pos_hint: { "x" : 0.668 , "y" : 0.80}
		multiline: False
		on_double_tap: c.text = " "			

	Button: 
		markup: True
		text: "[b]Calculate[b]"
		size_hint: 0.43 , 0.15
		pos_hint: { "x" : 0.28 , "y" : 0.63 }	
		background_color: 65/255, 105/255 , 225/ 255 , 1
		on_release: root.quadric_calculate()
	
	TextInput:
		id: answer1
		markup: True
		text : "x1"
		background_color: 25/255, 235/255 , 215/255, 0.4
		size_hint: 0.4, 0.2
		pos_hint: { "x" : 0 , "y" : 0.4}

	TextInput:
		id: answer2
		text_size: 15
		markup: True
		text : "x2"	
		background_color: 25/255, 235/255 , 215/255, 0.4
		size_hint: 0.4, 0.2
		pos_hint: { "x" : 0.59 , "y" : 0.4}			
		
<nCr_Pop@Popup>:
	id: perm_comb
	TextInput:
		id: n
		hint_text: " n :"
		font_size: 15
		background_color:  0.1,0.3,0.22, 0.4
		pos_hint: { "x" : 0 , "y" : 0.80}
		size_hint: 0.49, 0.2
		on_double_tap: n.text = " "

	TextInput:
		id : r
		hint_text: " r:"
		font_size: 15
		background_color: 0.1,0.1,0.22, 0.4
		size_hint: 0.49, 0.2
		pos_hint: { "x" : 0.5 , "y" : 0.80}
		multiline: False
		on_double_tap: r.text = " "	

	Button: 
		markup: True
		text: "[b]Combination[b]"
		size_hint: 0.55 , 0.15
		pos_hint: { "x" : 0.22 , "y" : 0.63 }	
		background_color: 65/255, 105/255 , 225/ 255 , 1
		on_release: root.comb()


	TextInput:
		id : combination_answer
		hint_text: "result:"
		background_color: 0.1,0.4,0.122, 0.4
		size_hint: 1, 0.2
		font_size: 20
		pos_hint: { "x" : 0 , "y" : 0.40}
		multiline: False
		on_double_tap: combination_answer.text = " "	





		
""")
#NEED TO CHANGE ALL Y ordinates...make them small		# make the pop up module

sm = WindowManager()
sm.add_widget(MainScreen(name="Main"))
sm.add_widget(Equations(name="equations"))
class CalculatorApp(App):

	def build(self):
		self.title = "Offensive Calculator"    #Might have to delete this part for apk transformation
		return sm


if __name__ == "__main__":
	CalculatorApp().run()
