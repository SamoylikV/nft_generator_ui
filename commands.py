import os
import shutil
import tkinter as tk
from tkinter import filedialog

os.chdir('..')

def install_():
    try:
        os.system('cmd /C "npm install"')
    except Exception:
        pass


def build_():
    try:
        os.system('cmd /C "npm run build"')
    except Exception:
        pass


def add_layer_(add_layer):
    try:
        layers_tf = False
        last_layer_id = 0
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        layer_name = f'      {{ name: "{add_layer.strip()}" }},'
        contents_list.insert(last_layer_id, layer_name)
        os.chdir('..')
        os.chdir('layers')
        os.makedirs(add_layer)
        os.chdir('..')
        os.chdir('src')
        with open('config.js', 'w') as f:
            f.write('\n'.join(contents_list))
        os.chdir('..')
    except Exception:
        os.chdir('..')


def remove_layer_():
    try:
        layers_tf = False
        last_layer_id = 0
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        os.chdir('..')
        os.chdir('layers')
        remove_layer = filedialog.askdirectory(initialdir=os.getcwd()).split('/')[-1]
        layer_name = f'      {{ name: "{remove_layer}"'
        for _ in contents_list:
            if layer_name in _:
                contents_list.remove(_)
        shutil.rmtree(f'{remove_layer}')
        os.chdir('..')
        os.chdir('src')
        with open('config.js', 'w') as f:
            f.write('\n'.join(contents_list))
        os.chdir('..')
    except Exception:
        os.chdir('..')


def add_file_():
    try:
        root = tk.Tk()
        root.withdraw()
        layers_tf = False
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        os.chdir('..')
        os.chdir('layers')
        layer_select = filedialog.askdirectory(initialdir=os.getcwd()).split('/')[-1]
        path = filedialog.askopenfilename()
        shutil.copyfile(path, layer_select + '/' + path.split('/')[-1])
        os.chdir('..')
    except Exception:
        os.chdir('..')


def remove_file_():
    try:
        root = tk.Tk()
        root.withdraw()
        layers_tf = False
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        os.chdir('..')
        os.chdir('layers')
        layer_select = filedialog.askdirectory(initialdir=os.getcwd()).split('/')[-1]
        path = filedialog.askopenfilenames(initialdir=f"{layer_select}")
        for _ in path:
            os.remove(_)
        os.chdir('..')
    except Exception:
        os.chdir('..')


def select_mode_():
    try:
        mode_list = []
        layers_tf = False
        layer_id = 0
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        os.chdir('..')
        os.chdir('constants')
        with open('blend_mode.js') as f:
            modes = f.read()
        modes_list = modes.split('\n')
        for _ in modes_list:
            if '};' in _:
                break
            if "{" not in _ or "}" in _:
                mode_list.append(_.split(': ')[-1][1:-2])
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        os.chdir('..')
        os.chdir('layers')
        layer_select = filedialog.askdirectory(initialdir=os.getcwd()).split('/')[-1]
        os.chdir('..')
        os.chdir('modes')
        mode_select = filedialog.askopenfilenames(initialdir=os.getcwd())[0].split('/')[-1][:-3]
        layer_name_mode = f'      {{ name: "{layer_select}", options: {{ blend: MODE.{mode_select}}}}},'
        for _ in contents_list:
            if layer_select in _:
                layer_id = contents_list.index(_)
        contents_list[layer_id] = layer_name_mode
        os.chdir('..')
        os.chdir('src')
        with open('config.js', 'w') as f:
            f.write('\n'.join(contents_list))
        os.chdir('..')
    except Exception:
        os.chdir('..')


def change_rarity_(rarity):
    try:
        root = tk.Tk()
        root.withdraw()
        layers_tf = False
        os.chdir('src')
        with open('config.js') as f:
            contents = f.read()
        contents_list = contents.split('\n')
        for _ in contents_list:
            if 'name' not in _ and layers_tf is True:
                layers_tf = False
                last_layer_id = (contents_list.index(_))
                break
            if 'layersOrder' in _:
                layers_tf = True
        os.chdir('..')
        os.chdir('layers')
        layer_select = filedialog.askdirectory(initialdir=os.getcwd()).split('/')[-1]
        path = filedialog.askopenfilename()
        os.chdir(layer_select)
        os.rename(path.split('/')[-1],
                  f'{path.split("/")[-1].split("#")[0]}#{rarity}.{path.split("/")[-1].split(".")[-1]}')
        os.chdir('..')
        os.chdir('..')
    except Exception:
        os.chdir('..')
