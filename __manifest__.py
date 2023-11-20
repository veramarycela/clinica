# -*- coding: utf-8 -*-
{
    'name': "Modulo Clinica",

    'summary': """
        Este modulo sirve para registrar operaciones de la clinica""",

    'description': """
        Este modulo sirve para registrar operaciones de la clinica
    """,
    'author': "ServiTecht",
    'website': "http://www.servitecht.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account'],
    'data': [
            'views/views.xml', 
            'views/views_clinica_cliente_paciente.xml',
            'views/views_clinica_partner.xml',
            'security/ir.model.access.csv',
            'report/factura_clinica_reporte.xml',
            'template/factura_clinica_template.xml',
    ],
   
}
