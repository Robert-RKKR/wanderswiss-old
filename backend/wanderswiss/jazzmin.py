GLOBAL_JAZZMIN_SETTINGS = {
    'site_title': 'Wander Swiss',
    'site_header': 'Wander Swiss',
    'site_brand': 'Wander Swiss',
    'site_logo': 'ico/logo/logo.svg',
    'login_logo': 'ico/logo/logo.svg',
    'site_logo_classes': 'img-circle',
    'site_icon': 'ico/favicon/favicon-32x32.png',
    'welcome_sign': 'Welcome to the Wander Swiss',
    'copyright': 'Copyright (c) 2023 Robert Tadeusz Kucharski RKKR - Wander Swiss',
    #'search_model': 'auth.User',
    'user_avatar': None,

    # Links to put along the top menu:
    'topmenu_links': [
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Home',  'model': 'inventory.Device', 'permissions': ['auth.view_user']},
        # {'name': 'Tokens',  'model': 'authtoken.token', 'permissions': ['auth.view_user']},
        {'model': 'auth.User', 'permissions': ['auth.view_user']},
    ],

    # 'usermenu_links': [
    #     {'model': 'authtoken.token'},
    #     {'model': 'auth.user'}
    # ],
    'show_sidebar': True,
    'navigation_expanded': False,
    #'hide_apps': ['auth'],
    'hide_apps': ['auth', 'authtoken'],
    'hide_models': [],
    'order_with_respect_to': [
        'inventory',
        'authtoken',
        'connections',
        'management',
        'notifications'],
    'icons': {
        # https://www.w3schools.com/icons/fontawesome5_icons_code.asp
        # Authentication:
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        # Inventory:
        'inventory': 'fas fa-server',
        'inventory.Device': 'fas fa-database',
        'inventory.Host': 'fas fa-desktop',
        'inventory.VHost': 'fas fa-desktop',
        'inventory.Platform': 'fas fa-cube',
        'inventory.Credential': 'fas fa-users',
        'inventory.Region': 'fas fa-globe',
        'inventory.Site': 'fas fa-building',
        # Connections:
        'connections': 'fas fa-paper-plane',
        'connections.Template': 'fas fa-file-word',
        'connections.TemplateExecution': 'far fa-file-word',
        'connections.Policy': 'fas fa-file-powerpoint',
        'connections.PolicyExecution': 'far fa-file-powerpoint',
        # Management:
        'management': 'fas fa-info-circle',
        'management.GlobalSettings': 'fas fa-cog',
        # History:
        'history': 'fas fa-archive',
        'history.Snapshot': 'fas fa-file-archive',
        # Notifications:
        'notifications': 'fas fa-envelope',
        'notifications.ChangeLog': 'fas fa-clock',
        'notifications.Notification': 'fas fa-envelope-open',
        # Celery:
        'django_celery_beat': 'fas fa-sitemap',
        'django_celery_beat.Clocked': 'fas fa-code',
        'django_celery_beat.Crontab': 'fas fa-code',
        'django_celery_beat.Interval': 'fas fa-code',
        'django_celery_beat.PeriodicTask': 'fas fa-code',
        'django_celery_beat.SolarEvent': 'fas fa-code',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    'related_modal_active': False,
    'custom_css': None,
    'custom_js': None,
    'show_ui_builder': False,
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {
        'auth.user': 'collapsible',
        'auth.group': 'vertical_tabs'},
}
