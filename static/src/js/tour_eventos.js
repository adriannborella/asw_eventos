odoo.define('website_sale.tour', function (require) {
    'use strict';
    
    var tour = require("web_tour.tour");

    var options = {
        test: false, // este valos se usa para saber si lo va a ver el usuario
        url: '/web',
    };
    
    var tour_name = 'crear_eventos';

    var pasos = [tour.STEPS.MENU_MORE,
        {
            content: "Crear un Evento",
            trigger: '.oe_menu_toggler[data-menu="70"]',
            run: "auto",
        },
        {
            content: "Ver la lista de Eventos",
            trigger: '.oe_menu_leaf[data-menu="72"]',
            run: "auto"
        },
        {
            content: "Cree un Evento",
            trigger: 'button.o_list_button_add',
            extra_trigger:'.o_list_view',            
            run: "auto"
        },
        {
            content: "Escriba un nombre",
            trigger: '.o_form_field[data-bt-testing-name="motivo"]',
            extra_trigger:'.o_form_sheet',
            run: function(actions) {  
                sleep(2000)
                actions.text("Evento de Prueba")
            }          
        },
        {
            content: "Seleccione una fecha",
            trigger: '.o_datepicker_input[data-bt-testing-name="fecha"]',
            run: "text 24/01/2020",
        },
        {
            content: "Guarde el evento",
            trigger: '.o_form_button_save',
            run: "click",
        }        
    ]

    function sleep(milliseconds) {
        var start = new Date().getTime();
        for (var i = 0; i < 1e7; i++) {
            if ((new Date().getTime() - start) > milliseconds) {
                break;
            }
        }
    }

    tour.register(tour_name, options, pasos)
})