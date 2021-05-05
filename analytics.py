import csv
import statistics as st

def quartiles(valores):
    valoresCopia= sorted(valores)
    n=len(valoresCopia)
    quartiles=[]
    indexes=[]
    indexes.append(round((n+1)/4))
    indexes.append(round(((n+1)*2)/4))
    indexes.append(round(((n+1)*3)/4))

    quartiles.append(valoresCopia[indexes[0]])
    quartiles.append(valoresCopia[indexes[1]])
    quartiles.append(valoresCopia[indexes[2]])

    return quartiles



def calcularTodo(nombre, valores):
    media = st.mean(valores)
    mediana = st.median(valores)
    if(nombre=='No. Ordenes'):
        moda='Todos los valores tienen el mismo número de ocurrencias'
    else:
        moda = st.mode(valores)
    desviacion = st.stdev(valores)
    cuartiles = quartiles(valores)
    minimo=min(valores)
    maximo=max(valores)

    print('------------------------ ',nombre,' ------------------------')
    print('Media: ',media)
    print('Mediana: ',mediana)
    print('Moda: ',moda)
    print('Desviación Estándar: ',desviacion)
    print('Cuartiles: ',cuartiles)
    print('Rango: ',maximo-minimo,' (Del ',minimo,' al ',maximo,')')
    
    print('\n\n')


customer= []
order = []
total_items = []
discount = []
weekday = []
hour = []
food = []
fresh =[]
drinks= []
home = []
beauty = []
health = []
baby = []
pets = []

with open('ulabox_orders_with_categories_partials_2017.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        if row[0] == 'customer':
            continue
        customer.append(float(row[0]))
        order.append(float(row[1]))
        total_items.append(float(row[2]))
        discount.append(float(row[3]))
        weekday.append(float(row[4]))
        hour.append(float(row[5]))
        food .append(float(row[6]))
        fresh.append(float(row[7]))
        drinks.append(float(row[8]))
        home.append(float(row[9]))
        beauty.append(float(row[10]))
        health.append(float(row[11]))
        baby.append(float(row[12]))
        pets.append(float(row[13]))


calcularTodo('No. Clientes',customer)
calcularTodo('No. Ordenes',order)
calcularTodo('Total Articulos',total_items)
calcularTodo(' Descuento',discount)
calcularTodo('Dia de la semana',weekday)
calcularTodo('Hora',hour)
calcularTodo('% comida',food) 
calcularTodo('% frescos',fresh)
calcularTodo('% bebidas',drinks)
calcularTodo('% casa',home)
calcularTodo('% belleza',beauty)
calcularTodo('% salud',health)
calcularTodo('% bebés',baby)
calcularTodo('% mascotas',pets)



        
        