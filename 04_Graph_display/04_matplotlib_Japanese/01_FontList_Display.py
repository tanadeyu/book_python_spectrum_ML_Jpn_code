import matplotlib.font_manager as fm

# Get the list of installed fonts
font_list = [f.name for f in fm.fontManager.ttflist]
#print(font_list)

# Aで始まるフォントを表示します
#a_fonts = [font for font in font_list if font.startswith('A')]
#print(a_fonts)

# Nで始まるフォントを表示します
n_fonts = [font for font in font_list if font.startswith('N')]
print(n_fonts)

# Pで始まるフォントを表示します
p_fonts = [font for font in font_list if font.startswith('P')]
print(p_fonts)

#　リストにArialがあるかどうかを確認する
if 'Arial' in font_list:
    print('Arial font found.')
else:
    print('Arial font not found.')
    

