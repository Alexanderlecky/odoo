# -*- coding: utf-8 -*-
{
    'name': "kuja_grant",
    'summary': "Grants module",

    'description': """
        "The grants feed is a centralized place for easy discovery of grant opportunities. This will bring more ease (and less time wasted) for organizations in finding potential funding that is the right fit for them - instead of spending hours scrolling online to find them. 
         For the MVP, the grants feed will include a standardized presentation of grant opportunities (scraped from the web) for local and national organizations to filter for the best opportunities. They will be able to save/flag a grant that they are interested in to be able to come back to see the information and access it at another time.  
         An organization, by completing their profile, will be able to see the grants that are a best-fit for them. These grants will be listed at the top of their grant feed and be based on certain information that is listed in the grant AND in their profile."
    """,
    'author': "levi",
    'website': "https://adesoafrica.org",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/grant_data.xml',
        'views/grant_eligibility_view.xml',
        'views/grant_focus_area_view.xml',
        'views/grant_geographic_area_view.xml',
        'views/grant_grant_view.xml',
        'views/grant_res_partner_view.xml',
        'views/grant_menuitem.xml',
        'views/website_grant_template.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
}

