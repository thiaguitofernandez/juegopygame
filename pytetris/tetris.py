import pygame
import colores
import configuracion
import random





tick = 0
tamaño_bloque = 30

#cuadricula
lista = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0], 
]

class bloques:
    def __init__(self,posicion_x,posicion_y,estado = 0,rect = None,color = None):
        self.posicion_x = posicion_x+1
        self.posicion_y = posicion_y+1
        self.estado = estado
        self.rect = rect
        self.color = color
def cuadricula_cordenadas():
    y = 0
    cuadricula = []
    for verticales in lista:
        y += 1
        x = -1
        for horizontales in verticales:
            x += 1
            cuadricula.append(bloques(x,y))
    return cuadricula

def dibujar_cuadricula():
    x = 90
    y = 0

    while x <= 390:
        pygame.draw.line(pantalla,colores.GRAY,(x,0),(x,690),1)
        x += 30
    while y <= 690:
        pygame.draw.line(pantalla,colores.GRAY,(90,y),(390,y),1)
        y += 30

def redibujar_contenido():
    for i in range(len(cuadricula)):
        if cuadricula[i].estado == 1:
            espacio = cuadricula[i] 
            dibujar_bloques(espacio.posicion_x,espacio.posicion_y,espacio.color,60,0)

def pasar_a_cuadricula(forma):
    for bloque in forma.rect:
        for i in range(len(cuadricula)):
            if bloque[0] ==  ((60+ ( ((cuadricula[i].posicion_x)) * 30 ) )) and bloque[1] == (0+ ( cuadricula[i].posicion_y * 30) ):
                cuadricula[i].estado = 1
                cuadricula[i].color = forma.color
                cuadricula[i].rect = bloque[0],bloque[1],30,30
                print("choco")
    
    return True
#util 
def dibujar_bloques(posicion_x,posicion_y,color,x = 90,y = 0):
    for e_lista in range(posicion_x):
        x += tamaño_bloque
    for e_lista in range(posicion_y):
        y += tamaño_bloque
    return pygame.draw.rect(pantalla,color,(x,y,tamaño_bloque,tamaño_bloque))

def redibujar_bloques(posicion_x,posicion_y,color,x = 90,y = 0):
    for e_lista in range(posicion_x):
        x += tamaño_bloque
    for e_lista in range(posicion_y):
        y += tamaño_bloque
    return pygame.draw.rect(pantalla,color,(x,y,tamaño_bloque,tamaño_bloque))

##movimeintos y limites jugador
def bajar(forma):
    for bloque in forma.rect:
        if bloque[1]+30 > 660:
            return
    for bloque in forma.rect:
        pygame.Rect.move_ip(bloque,0,tamaño_bloque)

def derecha(forma):
    for bloque in forma.rect:
        if bloque[0]+30 > 360:
            return
    for bloque in forma.rect:
        pygame.Rect.move_ip(bloque,tamaño_bloque,0)

def izquierda(forma):
    for bloque in forma.rect:
        if bloque[0]-30 < 90:
            return
    for bloque in forma.rect:
        pygame.Rect.move_ip(bloque,-tamaño_bloque,0)

def rotar(forma):
    forma.rotacion += 1
    match forma.forma:
        case 1:
            forma.forma = forma.forma[:8]
        case 2:
            forma.forma = forma.forma+" I"
        case 3:
            forma.forma = forma.forma[:8]
            forma.forma = forma.forma+" R"
        case 4:
            forma.forma = forma.forma[:8]
            forma.forma = forma.forma+" D"
def colision_fondo(forma):
    for bloque in forma.rect:
        x = 75
        for puntos in range(10):
            x += 30
            if pygame.Rect.collidepoint(bloque,x,675):
                jugador = pasar_a_cuadricula(forma)
                return jugador

def colision_contenido(forma):
    for bloque in forma.rect:
        for i in range(len(cuadricula)):
            if cuadricula[i].rect != None and forma != None:
                if pygame.Rect.colliderect(bloque,cuadricula[i].rect):
                    for bloque in forma.rect:
                            pygame.Rect.move_ip(bloque,0,-tamaño_bloque)
                    jugador = pasar_a_cuadricula(forma)
                    return jugador

def actulizar_jugador(forma):
    for bloque in forma.rect:
        pygame.draw.rect(pantalla,forma.color,bloque)

def eleccion_forma():
    
    probabilidad_bloque = random.randint(0, 100)
    probabilidad_bloque = 29
    if probabilidad_bloque < 10:
       return  I
    elif probabilidad_bloque < 30:
       return  T
    elif probabilidad_bloque < 60:
        probabilidad_lado = random.randint(0, 100) 
        if probabilidad_lado <= 50:
            return z_derecha
        else: return  z_izquierda
    elif probabilidad_bloque < 70:
       return  cuadrado
    elif probabilidad_bloque <=100:
        probabilidad_lado = random.randint(0, 100) 
        if probabilidad_lado <= 50:
           return  l_derecha
        else: return l_izquierda
        

#formas
class formas:
    def __init__(self,color,forma,posicionX = 210,posicionY = 0,rotacion = 1) -> None:
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.color = color
        self.forma = forma
        self.rotacion = rotacion

    def crear_posiciones(self)-> None:
        self.crear_forma()

    def modificar_posiciones(self)-> None:
        self.posiciones_normal()
        self.posiciones_derecha()
        self.posiciones_rervez()
        self.posiciones_izquierda()

    def crear_forma(self)-> None:
        match(self.forma):
            case "cuadrado":
                self.rect = []
                for vertical in range(2):
                    for horizontal in range(2):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "L derecha":
                self.rect = []
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY )  )
                self.rect.append(  dibujar_bloques(  0,1,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + (tamaño_bloque) )  )   )
                
            case "L izquierda":
                self.rect = []
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques (  horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY)  )
                self.rect.append(   dibujar_bloques(  0,1,self.color,self.posicionX,( self.posicionY + ( tamaño_bloque ) )  )   )
                               
            case "I":
                self.rect = []
                for vertical in range(4):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "Z derecha":
                self.rect = []
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY)  )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques( horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + tamaño_bloque )  )   )

            case "Z izquierda":
                self.rect = []
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY  )   )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

            case "T":
                self.rect = []
                self.rect.append(   dibujar_bloques(0,0,self.color,( self.posicionX + tamaño_bloque ),self.posicionY )  )
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

    def posiciones_normal(self)-> None:
        match(self.forma):
            case "cuadrado":
                
                for vertical in range(2):
                    for horizontal in range(2):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "L derecha":
                
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY )  )
                self.rect.append(  dibujar_bloques(  0,1,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + (tamaño_bloque) )  )   )
                
            case "L izquierda":
                
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques (  horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY)  )
                self.rect.append(   dibujar_bloques(  0,1,self.color,self.posicionX,( self.posicionY + ( tamaño_bloque ) )  )   )
                               
            case "I":
                
                for vertical in range(4):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "Z derecha":
                
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY)  )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques( horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + tamaño_bloque )  )   )

            case "Z izquierda":
                
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY  )   )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

            case "T":
                
                self.rect.append(   dibujar_bloques(0,0,self.color,( self.posicionX + tamaño_bloque ),self.posicionY )  )
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )
    def posiciones_izquierda(self)-> None:
        match(self.forma):
            case "cuadrado I":
                
                for vertical in range(2):
                    for horizontal in range(2):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "L derecha I":
                
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY )  )
                self.rect.append(  dibujar_bloques(  0,0,self.color,self.posicionX,( self.posicionY + (tamaño_bloque) )  )   )
                
            case "L izquierda I":
                
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + 30 ) )  )
                self.rect.append(  dibujar_bloques(  0,0,self.color,self.posicionX,( self.posicionY )  )   )
                               
            case "I I":
                
                for vertical in range(1):
                    for horizontal in range(4):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "Z derecha I":
                
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY)  )
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques( horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

            case "Z izquierda I":
                
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY  )   )
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + tamaño_bloque )  )   )

            case "T I":
                for bloque in self.rect:

                    self.rect.append(   redibujar_bloques(0,0,self.color,( bloque[0] + tamaño_bloque ),(bloque[1] + tamaño_bloque) )  )
                    for vertical in range(3):
                        for horizontal in range(1):
                            self.rect.append(   redibujar_bloques(horizontal,vertical,self.color,bloque[0],( bloque[1]  )  ) )
    def posiciones_rervez(self)-> None:
        match(self.forma):
            case "cuadrado R":
                
                for vertical in range(2):
                    for horizontal in range(2):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "L derecha R":
                
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY )  )
                self.rect.append(  dibujar_bloques(  0,0,self.color,self.posicionX,( self.posicionY  )  )   )
                
            case "L izquierda R":
                
                for vertical in range(3):
                    for horizontal in range(1):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX ,self.posicionY )  )
                self.rect.append(  dibujar_bloques(  1,0,self.color,self.posicionX,( self.posicionY  )  )   )
                               
            case "I R":
                
                for vertical in range(4):
                      for horizontal in range(1):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "Z derecha R":
                
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY)  )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques( horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + tamaño_bloque )  )   )

            case "Z izquierda R":
                
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY  )   )
                for vertical in range(1):
                    for horizontal in range(2):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

            case "T R":
                
                self.rect.append(   dibujar_bloques(0,0,self.color,( self.posicionX + tamaño_bloque ),(self.posicionY + tamaño_bloque ) )  )
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY   )   )    
    def posiciones_derecha(self)-> None:
        match(self.forma):
            case "cuadrado D":
                
                for vertical in range(2):
                    for horizontal in range(2):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "L derecha D":
                
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,( self.posicionY + (tamaño_bloque) ))  )
                self.rect.append(  dibujar_bloques(  2,0,self.color,self.posicionX,self.posicionY   )   )
                
            case "L izquierda D":
                
                for vertical in range(1):
                    for horizontal in range(3):
                        self.rect.append(  dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY )  )
                self.rect.append(  dibujar_bloques(  2,0,self.color,self.posicionX,( self.posicionY + tamaño_bloque ) )   )
                               
            case "I I":
                
                for vertical in range(1):
                    for horizontal in range(4):
                        self.rect.append(  dibujar_bloques( horizontal,vertical,self.color,self.posicionX,self.posicionY )  )

            case "Z derecha D":
                
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),self.posicionY)  )
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques( horizontal,vertical,self.color,self.posicionX,( self.posicionY + tamaño_bloque )  )   )

            case "Z izquierda D":
                
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,self.posicionX,self.posicionY  )   )
                for vertical in range(2):
                    for horizontal in range(1):
                        self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY + tamaño_bloque )  )   )

            case "T D":
                for bloque in self.rect:
                    
                    self.rect.append(   dibujar_bloques(0,0,self.color,self.posicionX,(self.posicionY + tamaño_bloque) )  )
                    for vertical in range(3):
                        for horizontal in range(1):
                            self.rect.append(   dibujar_bloques(horizontal,vertical,self.color,( self.posicionX + tamaño_bloque ),( self.posicionY )  ) )


cuadrado = formas(colores.YELLOW2,"cuadrado")
l_derecha = formas(colores.BLUE,"L derecha")
l_izquierda = formas(colores.CARROT,"L izquierda")
I = formas(colores.SKYBLUE,"I")
z_derecha = formas(colores.RED1,"Z derecha")
z_izquierda = formas(colores.GREEN2,"Z izquierda")
T = formas(colores.PURPLE,"T")


#comienza juego
pygame.init()
##config inicial
corriendo = True
pantalla = pygame.display.set_mode((configuracion.ALTO_VENTANA,configuracion.ANCHO_VENTANA))
pygame.display.set_caption(configuracion.NOMBRE_VENTANA)
jugador = eleccion_forma()
jugador.crear_posiciones()
cuadricula = cuadricula_cordenadas()


pygame.display.flip()

## loop de juego
while corriendo:

    
     
##chequeo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bajar(jugador)
            elif event.key == pygame.K_LEFT:
                izquierda(jugador)
            elif event.key == pygame.K_RIGHT:
                derecha(jugador)
            elif event.key == pygame.K_UP:
                rotar(jugador)
                jugador.modificar_posiciones()
    tick += 1           
    if tick == 60 :
        bajar(jugador)
        tick = 0
    
    if colision_contenido(jugador):
        jugador = None
    elif colision_fondo(jugador):
        jugador = None
    if jugador == None:
        jugador = eleccion_forma()
        jugador.crear_posiciones()
        
##actualizar a pantalla ocurrido            
    pantalla.fill(colores.BLACK)
    
    dibujar_contenido()
    actulizar_jugador(jugador)
    dibujar_cuadricula()
    pygame.display.flip()
    pygame.time.Clock().tick(configuracion.fps)



##fin de juego
pygame.quit()
