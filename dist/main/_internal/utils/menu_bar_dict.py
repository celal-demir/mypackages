import json
menu_bar_dict = {
    'main_menu_1': {
        'object_name': 'file',
        'text': 'Dosya',
        'sub_menu': {
            'sub1': {
                'text': 'ui',
                'icon': ':/myicons/menubar/ui.png',
                'sub_menu': {
                    'c1': {'text': 'ui Dosya Yolu',
                           'name': 'browse_ui',
                           'icon': ':/myicons/others/2.png',
                           'func': 'browse'
                           },
                    'c2': {'text': 'py Kaydetme Yeri',
                           'name': 'browse_ui_py',
                           'icon': ':/myicons/others/icons8-python-96.png',
                           'func': 'save'
                           }
                }
            },
            'sub2': {
                'text': 'qrc',
                'icon': ':/myicons/menubar/qrc.png',
                'sub_menu': {
                    'c1': {'text': 'qrc Dosya Yolu',
                           'name': 'browse_qrc',
                           'icon': ':/myicons/others/1.png',
                           'func': 'browse'
                           },
                    'c2': {'text': 'py Kaydetme Yeri',
                           'name': 'browse_qrc_py',
                           'icon': ':/myicons/others/icons8-python-96.png',
                           'func': 'save'
                           }
                }
            }
        }
    },
    'main_menu_2': {
        'object_name': 'settings',
        'text': 'Ayarlar',
        'sub_menu': {
            'sub1': {
                'text': 'Tema',
                'icon': ':/myicons/menubar/theme-48.png',
                'sub_menu':
                    {
                        'c1': {
                            'text': 'Aydınlık',
                            'name': 'set_light',
                            'icon': ':/myicons/menubar/sun-30.png',
                            'func': 'theme'
                        },
                        'c2': {
                            'text': 'Karanlık',
                            'name': 'set_dark',
                            'icon': ':/myicons/menubar/night-30.png',
                            'func': 'theme'
                        }
                    }
            },
            'sub2': {
                'text': 'Dil',
                'icon': ':/myicons/menubar/icons8-language-48.png',
                'sub_menu': {

                    'c1': {
                        'text': 'Tükçe',
                        'name': 'set_language1',
                        'icon': ':/myicons/menubar/turkey-48.png',
                        'func': 'lang'
                    },
                    'c2': {
                        'text': 'İngilizce',
                        'name': 'set_language2',
                        'icon': ':/myicons/menubar/united-kingdom-48.png',
                        'func': 'lang'
                    }

                }
            }
        }
    }
}

#json_str = json.dumps(menu_bar_dict, indent=4, ensure_ascii=False)
with open('../statics/menu_bar.json', 'w', encoding='utf-8') as f:
    json.dump(menu_bar_dict, f, indent=4, ensure_ascii=False)
