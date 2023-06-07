import unittest
from ClaseLista import ListaVehiculo
from ClaseVehiculo import Vehiculo

class TestAutomatizado(unittest.TestCase):
    def setUp(self):
        self.lista=ListaVehiculo()
    def Test_Agregar(self):
        vehiculo=Vehiculo("Marca4","Modelo4","Blanco",22000)
        self.lista.AgregarVehiculo(vehiculo)
        self.assertEqual(self.lista.getTope(),1)
    def Test_Insertar(self):
        vehiculo1=Vehiculo("Marca1","Modelo1","Rojo",4,20000)
        self.lista.InsertarVehiculo(0,vehiculo1)
        self.assertEqual(self.lista.MostrarVehiculo(0),vehiculo1)
    
        
        # Prueba de inserción en una posición intermedia
        vehiculo2 = Vehiculo( "Marca2", "Modelo2", 2, "Azul", 15000)
        vehiculo3 = Vehiculo("Marca5", "Modelo5", 2, "Negro", 22000)
        self.lista.AgregarVehiculo(vehiculo3)
        self.lista.InsertarVehiculo(1, vehiculo2)
        self.assertEqual(self.lista.MostrarVehiculo(1), vehiculo2)
        
         # Prueba de inserción en la última posición
        vehiculo4 = Vehiculo("Marca3", "Modelo3", 4, "Negro", 18000)
        self.lista.InsertarVehiculo(self.lista.getTope(), vehiculo4)

        self.assertEqual(self.lista.getTope(), 4)

    def Test_Mostrar(self):
            
        vehiculo5 = Vehiculo(False, "Marca5", "Modelo5", 4, "Gris", 17000)
        self.lista.AgregarVehiculo(vehiculo5)
        self.assertEqual(self.lista.MostrarVehiculo(0), vehiculo5)
            
    def test_ModificarPrecio(self):
            
        vehiculo6 = Vehiculo(True, "Marca3", "Modelo3", 4, "Negro", 18000,"","AABBCC",2010)
        self.lista.AgregarVehiculo(vehiculo6)
        precio_venta_anterior = vehiculo6.importeVenta()
        precio_venta_posterior = self.lista.ModificaBase("AABBCC")
        
        self.assertNotEqual(precio_venta_anterior,precio_venta_posterior)

if __name__ == "_main_":
    unittest.main()    
