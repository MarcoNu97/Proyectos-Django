let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    paging: true,
    scrollCollapse: true,
    scrollY: "250px",
    lengthMenu: [5, 10, 15, 20, 100, 200, 500],
    columnDefs: [
        { className: "centered", targets: [1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [1, 2, 3, 4, 5, 6, 7] },
        { searchable: false, targets: [3, 4, 5, 6, 7] },
        { width: "40%", targets: [7] },
        { width: "20%", targets: [1] },
        { width: "10%", targets: [0] }
    ],
    pageLength: 3,
    destroy: true,
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún Socio encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún Socio encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar Socio:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
        
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await list_cursos();

    dataTable = $("#datatable_cursos").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const list_cursos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/Aplicaciones/Academico/list_cursos/");
        const data = await response.json();

        
        let content = ``;
        data.cursos.forEach((curso, index) => {
            content += `
            
                <tr>

                    <td>${index + 1}</td>
                    <td>${curso.nombre}</td>
                    <td>${curso.codigo}</td>
                    <td>${curso.creditos}</td>
                    <td>${curso.creditos = 1 
                        ? "<i class='fa-solid fa-check' style='color: green;'></i>" 
                        : "<i class='fa-solid fa-xmark' style='color: red;'></i>"}</td>
                    <td>
                        <button class="btn btn-sm btn-primary">Detalles</button>  
                        <button class="btn btn-sm btn-warning"><a href="edicionCurso/${curso.codigo}">Modificar</a></button>
                        <button class="btn btn-sm btn-danger"><a href="eliminarCurso/${curso.codigo}" class="btnEliminacion">Eliminar</a></button>
                        

                    </td>
                </tr>`;

        })
        
        tableBody_cursos.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});


//
//
//Codigo del turorial

(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();


//
//
//Codigo menu desplegable

function toggleDropdown() {
    var dropdown = document.getElementById("myDropdown");
    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}

// Cierra el menú desplegable si se hace clic en cualquier parte de la página
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdown = document.getElementById("myDropdown");
        if (dropdown.style.display === "block") {
            dropdown.style.display = "none";
        }
    }
}

