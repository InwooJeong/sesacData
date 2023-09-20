import matplotlib
import matplotlib.font_manager as fm

font_list = [(f.name, f.name) for f in matplotlib.font_manager.fontManager.ttflist if 'Gothic' in f.name]

print(font_list)

# /System/Library/Fonts/Supplemental/AppleGothic.ttf
font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
print(font_name)