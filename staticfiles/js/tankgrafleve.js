setTimeout(function () {
    $("#subscribeModal").modal("show");
}, 2e3)
// Obtener una referencia al elemento canvas del DOM
const $grafica1 = document.querySelector("#grafica1");
// El titulo de la grafica. 
//const titulo1 = "Nivel del Tanque #1x"
var titulo1 = document.getElementById('titulox1').value;
// Las etiquetas son las que van en el eje X. 
const etiquetas = [document.getElementById('datox11').value, 
    document.getElementById('datox21').value, 
    document.getElementById('datox31').value, 
    document.getElementById('datox41').value,
    document.getElementById('datox51').value,
    document.getElementById('datox61').value,
    document.getElementById('datox71').value,
    document.getElementById('datox81').value,
    document.getElementById('datox91').value,
    document.getElementById('datox101').value,
    document.getElementById('datox111').value,
    document.getElementById('datox121').value,
    document.getElementById('datox131').value,
    document.getElementById('datox141').value,
    document.getElementById('datox151').value,
    document.getElementById('datox161').value,
    document.getElementById('datox171').value,
    document.getElementById('datox181').value,
    document.getElementById('datox191').value,
    document.getElementById('datox201').value,
    document.getElementById('datox211').value,
    document.getElementById('datox221').value,
    document.getElementById('datox231').value,
    document.getElementById('datox241').value    
]
    // Podemos tener varios conjuntos de datos
const datosLinea01 = {
    label: titulo1,
    data: [document.getElementById('datoy11').value, document.getElementById('datoy21').value,
        document.getElementById('datoy31').value, document.getElementById('datoy41').value,
        document.getElementById('datoy51').value, document.getElementById('datoy61').value,
        document.getElementById('datoy71').value, document.getElementById('datoy81').value,
        document.getElementById('datoy91').value, document.getElementById('datoy101').value,
        document.getElementById('datoy111').value, document.getElementById('datoy121').value,
        document.getElementById('datoy131').value, document.getElementById('datoy141').value,
        document.getElementById('datoy151').value, document.getElementById('datoy161').value,
        document.getElementById('datoy171').value, document.getElementById('datoy181').value,
        document.getElementById('datoy191').value, document.getElementById('datoy201').value,
        document.getElementById('datoy211').value, document.getElementById('datoy221').value,
        document.getElementById('datoy231').value, document.getElementById('datoy241').value
    ], 
    // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
    backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo
    borderColor: 'rgba(54, 162, 235, 1)', // Color del borde
    borderWidth: 1,// Ancho del borde
};

new Chart($grafica1, {
    type: 'line',// Tipo de gráfica o 'bar'
    data: {
        labels: etiquetas,
        datasets: [
            datosLinea01,
            // Aquí más datos...
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
    }
});