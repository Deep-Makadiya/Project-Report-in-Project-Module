# -*- coding: utf-8 -*-
{
    'name': "Demo Report",

    'summary': """Printing a Report into the project module """,

    'description': """Printing a report into the project module.In the report 
    the printed a project name,company,Responsible,Tags and the task which is 
    present into the project . THis all things is display into the report .""",
    'author': "Cravit",
    'website': "https://www.cravit.nl",
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '17.0.1.0.0',
    'depends': ['base', 'mail','project'],

    # always loaded
    'data': [
        'report/project_template.xml',
        'report/project_report.xml',
    ],
    'installable': True,
    'application': False,
}
