import json

def change_theme(css_path, json_path, index=0):
    with open(json_path, 'r') as file:
        config = json.load(file)
        theme_config = config['themes'][index]['config']

    with open(css_path, 'r+') as file:
        css = file.read()
        for property_name, property_value in theme_config.items():
            css = css.replace(property_name, property_value)
    return css

def change_lang(json_path, index=0):
    config = load_from_json(json_path)
    lang_config = config['words'][index]["config"]
    return lang_config

def load_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)




