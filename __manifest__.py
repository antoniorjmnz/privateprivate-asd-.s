{
    "name": "Upocubo",
    "summary": "Módulo para gestionar eventos y más...",
    "description": """
Long description of module's purpose
    """,
    "author": "Grupo - Alberto, María, Manuel, Pablo y Antonio",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    "application": True,
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "data/universities.xml",
    ],

    
}
