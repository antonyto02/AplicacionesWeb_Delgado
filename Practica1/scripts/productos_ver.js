//Obtener el valor del parámetro URL
const ParametroURL = new URLSearchParams(window.location.search);
const id_producto = parseInt(ParametroURL.get('id_producto'), 10);
//Datos del producto
const productos = {
1: {
    nombre: "FUNDA AZUL", 
    imagen: "/assets/producto1.jpeg",
    descripcion: "Descripción del producto",
    precio: "$100.00"

  },
2: {
    nombre: "FUNDA ROSA", 
    imagen: "/assets/producto2.jpeg",
    descripcion: "Descripción del producto",
    precio: "$100.00"

  },
3: {
    nombre: "FUNDA ROJA", 
    imagen: "/assets/producto3.jpeg",
    descripcion: "Descripción del producto",
    precio: "$100.00"

  },
4: {
    nombre: "Audífonos blancos", 
    imagen: "/assets/producto4.avif",
    descripcion: "Descripción del producto",
    precio: "$100.00"

  },
5: {
    nombre: "Audífonos morados", 
    imagen: "/assets/producto5.webp",
    descripcion: "Descripción del producto",
    precio: "$100.00"

  }, 
};
//Actualizar etiquetas HTML según el producto
if (producto[id_producto]) {
  document.getElementById("nombre_producto").textContent=productos[id_producto].nombre;
  document.getElementById("img_producto").src=productos[id_producto].imagen;
  document.getElementById("descripcion_producto").textContent=productos[id_producto].descripcion;
  document.getElementById("precio_producto").textContent=productos[id_producto].precio;
}
else {
  document.getElementById("nombre_producto").textContent="producto no disponible";
  document.getElementById("img_producto").style.display="none";
  document.getElementById("descripcion_producto").textContent="descripción no disponible";
  document.getElementById("precio_producto").textContent="precio no disponible";


}