########### EJEMPLO DE FUNCION ########
#recordemos que las funciones son bloques independientes de codigo.
#las funciones encapsulan dos cosas: discrete task(I/O, pointing to objects, receiving input or giving output)
#la segunda razon para tomar algo y volverlo una funcion es para operaciones repetitivas.
############################Formula################################
# Formula for a circumference is c = pi * diameter  <--- para obtener la circumferencia de un circulo.
# Formula for a diameter is d = 2 * radius   <--- para obtener el Diametro de un circulo.
#########################################Funcion para resolver circumferencia#########################
#funcion encargada de resolver el problema de encontrar una circumferencia.
#def circumference(radius):
#  pi = 3.14 # (va codificado en este ejemplo o puede ir de forma dinamica, hardcoded/codificado para el ejemplo)
#  circumferenceValue = pi * radius * 2 #Variable dentro de la cual se resuelve el valor de Circunferencia.
#  return circumferenceValue #recordemos Return se utiliza dentro de un metodo o funcion para mostrar un resultado.

#funcion encarga de tomar el output de funcion circumference y llevar tasks adicionales.
#def printCircumference(radius):
#  myCircumference = circumference(radius) #Variable invoca o hace uso de funcion circumference y alberga su resultado.
#  print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(myCircumference)) #concatenacion de valores a mostrar en pantalla.

#Misma funcion pero con una modificacion para delimitar el numero de decimales que recibimos en la respuesta.
#def printCircumference2(radius):
#  myCircumference = circumference(radius) #Variable invoca o hace uso de funcion circumference y alberga su resultado.
#  circleValue = "{:.2f}".format(myCircumference)
#  print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(circleValue)) #concatenacion de valores a mostrar en pantalla.  
##########################################Termina definicion de funciones###########################################################

################################ invocacion/uso de las funciones########################################
#ejemplo1 con variables de valor estatico(el valor lo predefinieron ya dentro de la variable.)
#radius1 = 2  
#radius2 = 5
#radius3 = 7
#Valor dentro de variables radius 1, radius 2 y radius 3 se ingrensan como argumento al momento de llamar la funcion printCircumference.
#printCircumference(radius1) 
#printCircumference(radius2)
#printCircumference(radius3)


#Ejemplo2 con Variable Valor dinamico(en conbinacion de funcion int() y input() que acepta cualquier valor(radio) que ingresemos).
#radius4 = int(input("enter the Radius of your circle: "))
#printCircumference(radius4)


#######################################Clase Circulo#######################################################
#recordemos que una clase es una receta para poder a partir de esta crear instancias u objetos 
# estos objetos tienen dos caracteristicas comportamientos(metodos) y atributos/propiedades(variables)

#class Circle:

#    def __init__(self, radius):
#        self.radius = radius

#    def circumference(self):
#        pi = 3.14
#        circunferenceValue = pi * self.radius *2
#        return circunferenceValue

#    def printCircunferencia(self):
#        myCircumference = self.circumference()
#        print("circumference of a circle with a radius of  " +  str(self.radius)+ " is " +str(myCircumference))

#    def printCircunferencia2(self):
#        myCircumference = self.circumference() #Variable invoca o hace uso de funcion circumference y alberga su resultado.
#        circleValue = "{:.2f}".format(myCircumference)
#        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(circleValue))

###########################Agregando metodos para resolver el Area de un circulo#################################

#    def area(self):
#        pi = 3.14
#        AreaValue = pi * self.radius**2
#        return AreaValue


#    def printArea(self):
#        myArea = self.area()
#        print("the area of a circle with a radius of " + str(self.radius)+" is " + str(myArea))   
###########################################creando objetos de la clase Circle (creando instancias de Circle)#############

#objeto1 = Circle(7)
#objeto1.printArea()
#objeto1.printCircunferencia2()
#######################################Uso de la clase Circle#####################################################  
   
#circulo = Circle(2) # creacion de una instancia/objecto a partir de la clase Circle.
#circulo.printCircunferencia()  #Objeto luego usa sus propiedades/atributos(variables) y su comportamiento(Metodos).




###################################################################################################################

#¿Cómo aprendemos a crear una clase?
#definimos la clase con y su nombre con la siguiente sintaxis --->  class <nombre de la clase>:
#paso 2: definir un constructor
#paso 3: definir estados/variables/atributos.
#paso 4: definir comportamientos/metodos.
#nota: el comportamiento del objeto hace referencia a los metodos a los que tiene acceso el objeto.
#Estos metodos son muchas veces dependientes del estado del objeto(variable/atributo).
#Si actualizo el estado de un objeto los metodos pueden ejecutarse de una forma distinta (con diferentes valores!)

#######################################Metodo Constructor#####################################################
#SELF : es un keyword especial de python que hace referencia a la instancia actual de la clase, se usa para acceder a los atributos y metodos de la clase.
#cuando creamos una clase definimos principalmente el metodo init el cual es invocado durante la instancia o creacion de un objeto.
#__init__ es invocado cada vez que instanciamos/creamos un objeto a partir de una clase.
#el metodo deja ala clase iniciar los atributos/variables/estado del objeto.

# Syntax:  def __init__(self,radius,area)
#               self.atributo = Atributo  
#               self.radius = radius 
#               self.area = 100  
#############################################################################################################
####################################ejemplo clase#############################

#class humano:
#    def __init__(self,sexo):
#        self.sexo=sexo 

#    def hablar(self,habla):
#        print(habla)

#    def caminar(self,camina):
#        print(camina)

#    def cantar(self,cantar):
#        print(cantar)


#bebe1 = humano("hombre")
#bebe1.hablar("hello world")
#bebe1.caminar("soy un ser humano y ser caminar")
#bebe1.cantar("soy un ser humano y mi hoobie es cantar!! lalala")

#################################ejemplo#2############################

#class mujer:
#    def __init__(self):
#        self.sexo = "femenino"
#        print("soy un instancia de la clase mujer")
#
#    def hablar(self,habla):
#        print(habla)
#
#    def conducir(self):
#        print("ya se manejar al malll...")
#
#    def correr(self):
#        print("ahora se correr y salgo a correr....")
#
#
#humano = mujer()
#humano.hablar("me encanta hablar con mmis amigas por telefono")

#print(mujer.__dict__)
