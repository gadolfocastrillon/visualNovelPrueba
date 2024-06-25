class Item: 
    """
    Clase que representa un elemento en el inventario. 

    Atributes: 
        codigo(int): identificador único del elemento.
        nombre(str): Nombre del objeto.
        cantidad(int): Cantidad del elemento en el inventario.
        precio(float): Precio del elemento.
        direccion(str): Dirección de la imagen del elemento.
        image_icon()PENDIENTE SI DEJARLO
        active_to_sell(bool): Si el elemento se puede vender.
        active_to_eat(bool): Si el elemento se puede comer.
        active_to_use(bool): Si el elemento se puede usar.
        cantidad_maxima(int): Cantidad máxima de elementos en el inventario.
    """


    def __init__(self,codigo_,nombre_,cantidad_, precio_, image_icon_= 'No_direccion'):
        """
        Inicializa la clase Objeto con los valores dados.

        Args: 
            codigo(int): identificador único del elemento.
            nombre(str): Nombre del objeto.
            cantidad(int): Cantidad del elemento en el inventario.
            precio(float): Precio del elemento.
            direccion(str)(opcional): Dirección de la imagen del elemento.
        """
        self.codigo = codigo_ 
        self.nombre = nombre_ 
        if(cantidad_<0):
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = cantidad_
        self.precio = precio_
        self.direccion = image_icon_
        #self.image_icon = mpimg.imread(self.direccion)
        self.active_to_sell = True #Se puede vender en la tienda
        self.active_to_eat = True  #Se puede comer fuera de combate
        self.active_to_use = True  #Se puede usar en combate.
        self.cantidad_maxima = 20
       
    #---------------------------------------------------------------------
    #--------------------Getters------------------------------------------
    #---------------------------------------------------------------------
    def get_active_to_sell(self):
        """
        Obtiene si el objeto esta activo para vender
        
        Returns:
            bool:True si el objeto se puede vender.
                 False si no se puede vender.
        """
        return self.active_to_sell
    
    def get_active_to_eat(self): 
        """
        Obtiene si el objeto esta activo para comer
        
        Returns:
            bool:True si el objeto se puede comer.
                 False si no se puede comer.
        """
        return self.active_to_eat
    
    def get_active_to_use(self): 
        """
        Obtiene si el objeto esta activo para usar.

        Returns:
            bool:True si el objeto se puede usar.
                 False si no se puede usar.
        """
        return self.active_to_use
    
    def get_cantidad_maxima(self):
        """
        Obtiene la cantidad maxima de objetos

        Returns:
            int: cantidad máxima en el inventario.
        """
        return self.cantidad_maxima
    
    def get_codigo(self): 
        """
        Obtiene el codigo unico el objeto.

        Returns:
            str: Codigo del elemento.
        """
        return self.codigo 
    
    def get_nombre(self): 
        """
        Obtiene el nombre del objeto.

        Returns:
            str: nombre del elemento.
        """
        return sel.nombre
    
    def get_cantidad(self): 
        """
        Obtiene la cantidad de este objeto en el inventario.
        
        Returns:
            int: cantidad en el inventario.
        """
        return self.cantidad
    
    def get_precio(self): 
        """
        Obtiene el precio del objeto.

        Returns:
            float: Precio del elemento.

        """
        return self.precio
    
    def get_direccion(self):
        """
        Obtiene la dirección del objeto donde encuentro la imagen del mismo.
        
        Returns:
            str: dirección del elemento.

        """
        return self.direccion
    
    #---------------------------------------------------------------------
    #--------------------Setters------------------------------------------
    #---------------------------------------------------------------------
    def set_cantidad(self,valor):
        """
        Modifica la cantidad del objeto dentro del inventario.

        Args: 
            valor(int): Ingresa el valor a disminuir la cantidad.
        """
        self.cantidad = self.cantidad + valor
    
    def set_cantidad_maxima(self,valor):
        """
        Modifica la cantidad máxima del objeto

        Args: 
            valor(int): Ingresa la nueva cantidad máxima.
        """
        self.cantidad_maxima = valor
        
    def set_active_to_sell(self,valor):
        """
        Modifica si el objeto se puede vender o no.
        
        Args: 
            valor(bool) : true si el elemento se puede vender, False en caso contrario
        
        """
        if(type(valor) != bool):
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_sell = valor
            
    def set_active_to_eat(self,valor):
        """
        Modifica si el objeto se puede comer o no.
        
        Args: 
            valor(bool) : true si el elemento se puede comer, False en caso contrario
        """
        if(type(valor)!= bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_eat = valor
        
    def set_active_to_use(self,valor): 
        """
        Modifica si el objeto se puede usar o no.

        Args: 
            valor(bool) : true si el elemento se puede usar, False en caso contrario
        """
        if(type(valor) != bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_use = valor
    
    def mod_car(self,val1,val2,val3):
        if(type(val1)!= bool or type(val2)!=bool or type(val3)!= bool):
            raise TypeError("Los valores ingresados no corresponde a booleanos")
        self.set_active_to_use(val1)
        self.set_active_to_eat(val2)
        self.set_active_to_sell(val3)


    #---------------------------------------------------------------------
    #--------------------Funciones----------------------------------------
    #---------------------------------------------------------------------
    def __iadd__(self,valor): 
        """
        Aumenta la cantidad del elemento usando el operador +=

        Args: 
            Valor(int): Cantidad a aumentar el objeto.
        Ejm:
            Si en la tienda compro 2 objetos del mismo, valor = 2, el objeto aumenta 
            en una cantidad de 2.
        """
        self.cantidad += valor
        return self
    
    def __isub__(self,valor):
        """
        Disminuye la cantidad del elemento usando el operador -=

        Args: 
            Valor(int): Cantidad a disminuir del objeto.
        Ejm:
            Si gasto una poción, valor = 1, el objeto disminuye en una 
            cantidad de 1.
        """
        if (self.cantidad <= 0): 
            self.cantidad = 0
        else: 
            self.cantidad -= valor
        return self
    
    def particionar_cantidad(self,cantidad): #PENDIENTE A REVISIÓN SI DEJAR O NO.
        """
        Convierte la cantidad ingresada en una relacionada a oros platas y bronces.
        

        Args: 
            Cantidad(int): Cantidad a convertir
        returns: 
            Vector(int): Retorna un vector de 3 componentes enteras. 
                         La primer componente es la cantidad de oros.
                         La segunda componente es la cantidad de platas.
                         La tercera componente es la cantidad de bronces.  
        """ 
        valor_oro = 10000
        valor_plata = 100
        oro = cantidad // valor_oro 
        residuo = cantidad % valor_oro 
        plata = residuo // valor_plata
        bronce = residuo % valor_plata
        return [oro,plata,bronce]

    def __str__(self):
        """
        Muestra la información del objeto usando el operador print(objeto)

        returns: 
            str: Retorna un string con la información del objeto.
        Ejm:
            Manzana
            Cantidad: 10
            Precio: 1 oros 2 platas 3 bronces
            
        """ 
        cadena = self.nombre + "\n"
        cadena += "\tCantidad: " + str(self.cantidad) +"\n"
        precios = self.particionar_cantidad(self.precio)
        cadena += "\tPrecio: " + str(precios[0]) + " oros " + str(precios[1]) + " platas " + str(precios[2]) + " bronces\n"
        return cadena


    def consumir(self):
        """
        Elimina en una cantidad el objeto del inventario y retorna un mensaje

        Returns:
            str: Retorna el mensaje en función de la cantidad actual de esos elementos.
        """
        if self.cantidad <= 0:
            return "No tengo más elementos de eso"
        
        self.set_cantidad(-1)
        return f"La cantidad actual es: {self.cantidad}"

class Comida(Item):
    """
    Clase que hereda los elementos de Item y aparte crea unas nuevas caracteristicas.
    Esta clase trata de simular en un item de comida dentro del juego. 

    Atributes: 
        reg_life(int): Cantidad de vida que regenera.
        reg_mana(int): Cantidad de mana que regenera.

    Nota:
        - La comida no se puede usar dentro de combate 
        - Tiene un maximo de 50 elementos. 
    """
    def __init__(self,codigo_,nombre_,cantidad_, precio_,reg_life_,reg_mana_):
        super().__init__(codigo_,nombre_,cantidad_, precio_)
        self.set_active_to_use = False #No se puede usar en combate.
        self.set_cantidad_maxima = 50 #Cantidad maxima de este objeto en 50.
        self.reg_life = reg_life_ #Cantidad de vida que regenera.
        self.reg_mana = reg_mana_ #Cantidad de mana que regenera.

    def get_reg_life(self):
        """
        Obtiene la regeneración de vida del objeto.

        Returns: 
            int: regeneración de vida del objeto
        """
        return self.reg_life

    def get_reg_mana(self):
        """
        Obtiene la regeneración de mana del objeto.

        Returns: 
            int: regeneración de mana del objeto
        """
        return self.reg_mana

    def consumir(self,obj):
        """
        Consume el objeto del inventario. 
        Permite aumentar la vida y mana actual del personaje.

        Args:
            obj: Clase de Personaje, para modificar ciertos atributos de este.
                Modifica la vida y mana actual.
        """
        #if(self.cantidad<=0):
        totalMana = obj.get_mana + self.reg_mana
        totalLife = obj.get_life + self.reg_life

        if (totalMana>obj.get_manaMax) and (totalLife > obj.get_lifeMax):
            return "Tengo todos mis atributos al máximo"

        if self.cantidad <= 0:
            return "No tengo más elementos de eso"

        if(obj.get_mana == obj.get_manaMax):
            print("Tengo el mana al máximo")
        if(obj.get_life == obj.get_lifeMax):
            print("Tengo la vida al máximo")

        super().consumir()
        obj.set_life(self.reg_life)  # Regenera la vida del personaje
        obj.set_mana(self.reg_mana)  # Regenera el mana del personaje

class Personaje:
    """
    Clase que representa un personaje. 

    Atributes: 
        name(str): Nombre del personaje.
        life(int): Vida del personaje.
        mana(int): Mana del personaje.
    """
    def __init__(self, name_= "Julius", life_=100, mana_= 50):
        self.name = name_ 
        self.life = life_ 
        self.mana = mana_ 
        self.lifeMax = 100
        self.manaMax = 50

    def get_name(self):
        """
        Obtiene el nombre del personaje

        Returns: 
            str: nombre del personaje
        """
        return self.name 

    def get_life(self):
        """
        Obtiene la vida del personaje.

        Returns: 
            int: Vida actual del personaje.
        """
        return self.life

    def get_mana(self):
        """
        Obtiene el mana del personaje.

        Returns: 
            int: mana actual del personaje.
        """
        return self.mana

    def get_lifeMax(self):
        """
        Obtiene la vida máxima del personaje.

        Returns: 
            int: Vida total máxima del personaje.
        """
        return self.lifeMax

    def get_manaMax(self):
        """
        Obtiene la mana máximo del personaje.

        Returns: 
            int: mana total máximo del personaje.
        """
        return self.manaMax

    def set_name(self,valor):
        """
        Modifica el nombre del personaje.

        Args: 
            valor(str): El nombre nuevo del personaje.
        """
        self.name = valor

    def set_life(self,valor):
        """
        Modifica la vida del personaje.
        Tiene un modificador para que la vida no aumente a valores mayores a la vida maxima.

        Args: 
            valor(int): La cantidad a disminuir la vida.
        """
        if (self.life > self.lifeMax):
            self.life = self.lifeMax

        self.life = self.life + valor 

    def set_mana(self,valor):
        """
        Modifica el mana del personaje.
        Tiene un modificador para que el mana no aumente a valores mayores al mana máximo.

        Args: 
            valor(int): La cantidad a disminuir el mana.
        """
        if(self.mana > self.manaMax):
            self.mana = self.manaMax

        self.mana = self.mana + valor


    def set_lifeMax(self,valor):
        """
        Modifica la vida máxima del personaje.

        Args: 
            valor(int): El nuevo valor de la vida total.
        """
        self.lifeMax = valor

    def set_manaMax(self,valor):
        """
        Modifica la mana maximo del personaje.

        Args: 
            valor(int): El nuevo valor del mana total.
        """
        self.manaMax = valor 

    def __str__(self):
        """
        Muestra la información del personaje.

        returns: 
            str: Retorna un string con la información del personaje.
        Ejm:
            Julius
            Vida: 100/100
            Mana: 40/50
            
        """ 
        cadena = f"Nombre: {self.name}.\nVida: {self.life}/{self.lifeMax}.\nMana: {self.mana}/{self.manaMax}" 
        return cadena

if __name__ == '__main__':
    """
    Ejemplo de como crear un objeto. 

    """
    #Manzana = Item("0001","manzana",3,100, image_icon_= 'images/manzana')
    #print(Manzana)
    #Manzana.consumir()
    #print(Manzana)
    #Manzana2 = Comida("0001","manzana",0,100,1,1)
    Manzana = Item("0001","manzana",3,100)
    Manzana.mod_car(False,False,False)
    pj = Personaje(name_= "Gustavo")
    print(pj)
    pj.set_life(-10)
    print(pj)
    #print(Manzana2)
    #Manzana2.consumir(pj)