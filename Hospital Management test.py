"""Este fue mi primer proyecto con menu y opciones en python, para una materia de fundamentos de informatica donde no vimos
la programacion orientada a objetos"""

from 

#alumno: Ivan Emiliano Bogado Olmedo		comision:08

#Para la promocion de la materia realice un programa relacionado a la gestión de pacientes
#que se encarga de cargar en una lista con datos del paciente, quitar una sublista en base al nombre que de el usuario 
#y fijarse por medio del nombre para que especialidad tienen turno.
#todo esto acompañado por un menú que permitira al usuario navegar por esas opciones.

print("Hospital Management")
'''1_programa para cargar datos de los pacientes'''

def cargar_pacientes(list):
#luego de definir la funcion agregue una lista vacia que almacenara a los pacientes
#agregue la variable POSICION para que el usuario tenga una guia a la hora de eliminar la lista de un paciente
	patient_name=input("Please enter your first name or 'x' to exit ")
	while patient_name.lower()!="x":
			patient_surname=input('Please enter your last name: ')
			patient_id=input("Please enter your ID number: ")
			doctor_major=input("What specialty do you need?: ")
			list.append([patient_name, patient_surname,patient_id, doctor_major])
			patient_name=input("Please enter your first name or 'x' to exit: ")
#los datos que el usuario ingreso se agregan a la lista que anteriormente estabab vacia para ser retornados 

'''2_funcion para ver para que especialidad tienen turno por el nombre'''
#los parametros que recibe esta funcion son lista y nombre
def show_shift(List_seeked,search_id):
	if List_seeked==[]:
		#tengo que modularizar mejor y poner los mensajes con un if en los llamados desde la opcion 2
		return 'no shift asigned'
	else:
#Aqui el for recorrera la lista
		for t in List_seeked:
#cuando se encuentre un valor en la lista en la posicion de dni al ingresado se devolvera la especialidad en base a su posicion
			if t[2]==search_id:
				return t[3]

'''3_funcion para borrar un turno'''
#los parametros que recibe esta funcion son lista y posicion de la sublista a eliminar
def delete_shift(delete_list,dni):
#no puede borrar
	if delete_list!=[]:#una vez verificado que el valor a eliminar existe, lo eliminamos y retornamos la lista para que el usuario vea los cambios
		for D in range(len(delete_list)+1):
			if delete_list[D][2]==dni:
				delete_list.pop(D)
				print(f"se borraron los datos del paciente con dni:	 {dni}")
				break		
	else:
		return "\33[92m user id is not register in our's database\33[0m]"
	return delete_list

'''4_porcetaje de especialidades'''
#La variable nombre_especialidad sera ingresada por el usuario y nos servira para saber que comparar
def percentage_of_majors(L,nombre_especialidad):
	if L==[]:
		return 'lista vacia'
	else:
		i=0
		c=0
#Aca uso un while para recorrer la lista y con el contador voy a hacer el porcentaje
		while len(L)>i:
			if L[i][3]==nombre_especialidad:
				c=c+1
			i=i+1
#una vez que el while ya recorrio toda la lista, ya tengo todos los datos que necesito para proceder a realizar los calculos del porcentaje
		porciento= c/len(L)*100
	return porciento
"""Secret option to see the list"""
def show_list(list):
	for i in range(len(list)):
		print(list[i])

#menú
patients_list=[["obama", "what's obama first name","1255", "doctor"],["jose","williams","324","doctor"]]
#En el menu estaran las invocaiones de la funcion asociadas a una opcion que ingrese el usuario
print("-".ljust(80, "-"))
print("1_ Load patient data")
print("2_ Check assigned shifts")
print("3_ Cancel a shift")
print("4_ Percentage of specialties required")
#secret option with konami code
print("-".ljust(80, "-"))
user_election=input("\033[92m Select one option or 'x' to exit: \033[0m")
while user_election!="x":
	if user_election=="1":
		cargar_pacientes(patients_list)
		print(patients_list)
	elif user_election=="2":
		seeked_id=input('Please enter ID number: ')
		print(show_shift(patients_list,seeked_id))
	elif user_election=="3":
#El print de pacientes lo agregue para que el usuario tenga una guia a la hora de borrar
		print(patients_list)
		reference_id=input('Enter a id: ')
		delete_shift(patients_list,reference_id)
		
	elif user_election=="4":
		espec=input('Ingrese especialidad para sacar porcentaje: ')
		print(f"El {percentage_of_majors(patients_list,espec)}% de nuestros pacientes estan registrados para la especialida {espec}")
	elif user_election=="konami code":
		show_list(patients_list)
	else:
		print('opcion incorrecta')
	print("-".ljust(80, "-"))
	print("1_ Load patient data")
	print("2_ Check assigned shifts")
	print("3_ Cancel a shift")
	print("4_ Percentage of specialties required")
	print("-".ljust(80, "-"))
	user_election=input("\033[92m Select one option or 'x' to exit: \033[0m")
#ahora hace falta aprender orientado a objetos y crear las clases doctor y paciente par un hospital
