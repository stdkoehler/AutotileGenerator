import numpy as np
from itertools import combinations_with_replacement
from PIL import Image

source_folder = './Example/'
tilename = 'dirt_dark'
size = 32

# I: Inner
# T: Top
# B: Bottom
# C: Center
# L: Left
# R: Right
# tyx -> t: Inner/Outer, y: Top/Center/Bottom, x: Left/Center/Right

tiles = ['IBL', 'IBR', 'ITL', 'ITR', 'OBL', 'OBC', 'OBR', 'OCL', 'OC0', 'OCR', 'OTL', 'OTC', 'OTR', 'NNN', 'OC1', 'OC2']

tile_layout = np.array(
    [['OTL', 'OTR', 'OTL', 'OTC', 'OTC', 'OTC', 'OTC', 'OTR', 'OTL', 'OTR', 'OTL', 'OTC', 'OTC', 'OTC', 'OTC', 'OTR'],
     ['OBL', 'OBR', 'OBL', 'OBC', 'OBC', 'OBC', 'OBC', 'OBR', 'OCL', 'OCR', 'OCL', 'OC0', 'OC0', 'OC0', 'OC0', 'OCR'],
     ['OTL', 'OTC', 'OTC', 'OTR', 'OCL', 'IBL', 'OTC', 'OTC', 'OCL', 'OCR', 'OCL', 'OC0', 'OC0', 'OC0', 'OC0', 'OCR'],
     ['OCL', 'ITL', 'ITR', 'OCR', 'OCL', 'ITL', 'ITR', 'ITL', 'OCL', 'OCR', 'OCL', 'OC0', 'OC0', 'OC0', 'OC0', 'OCR'],
     ['OCL', 'IBL', 'IBR', 'OCR', 'IBR', 'IBL', 'IBR', 'OCR', 'OCL', 'OCR', 'OCL', 'OC0', 'OC0', 'OC0', 'OC0', 'OCR'],
     ['OBL', 'OBC', 'OBC', 'OBR', 'OBC', 'OBC', 'ITR', 'OCR', 'OBL', 'OBR', 'OBL', 'OBC', 'OBC', 'OBC', 'OBC', 'OBR'],
     ['OCL', 'OC0', 'OC0', 'OCR', 'OTC', 'OTC', 'OTC', 'OTC', 'OC0', 'OC0', 'OC0', 'OC0', 'OC0', 'IBL', 'IBR', 'OC0'],
     ['OCL', 'ITL', 'ITR', 'OCR', 'OC0', 'ITL', 'ITR', 'OC0', 'OC0', 'ITL', 'ITR', 'OC0', 'ITR', 'ITL', 'ITR', 'ITL'],
     ['OCL', 'IBL', 'IBR', 'OCR', 'OC0', 'IBL', 'IBR', 'OC0', 'OC0', 'IBL', 'IBR', 'OC0', 'IBR', 'IBL', 'IBR', 'IBL'],
     ['OCL', 'OC0', 'OC0', 'OCR', 'OBC', 'OBC', 'OBC', 'OBC', 'OC0', 'OC0', 'OC0', 'OC0', 'OC0', 'ITL', 'ITR', 'OC0'],
     ['IBR', 'IBL', 'OC0', 'OC0', 'OC0', 'IBL', 'IBR', 'OC0', 'OC0', 'IBL', 'IBR', 'OC0', 'IBR', 'IBL', 'NNN', 'NNN'],
     ['OC0', 'OC0', 'ITR', 'ITL', 'OC0', 'ITL', 'ITR', 'OC0', 'ITR', 'OC0', 'OC0', 'ITL', 'ITR', 'ITL', 'NNN', 'NNN'],
     ])

mapping = dict()
for ti in tiles:
    mapping[ti] = Image.open(source_folder + ti + '.png')

# Optional: Create Center Tile variation
width = tile_layout.shape[1]
center_tiles = ['OC0', 'OC1', 'OC2']
n = 4
combs = combinations_with_replacement(center_tiles, n)
tile_variation = np.empty((2,0))
for combi in combs:
    tile_variation = np.hstack([tile_variation, np.array(combi).reshape(2, 2)])

N = int(np.ceil(tile_variation.shape[1]/width))*width - tile_variation.shape[1] #how many do we need to pad?
tile_variation = np.pad(tile_variation, ((0,0),(0,N)), mode='constant', constant_values='NNN')
tile_variation_split = np.hsplit(tile_variation, int(tile_variation.shape[1]/width))
tile_variation = np.vstack(tile_variation_split)

tile_layout = np.vstack([tile_layout, tile_variation])
# End Create Center Tile variation


tile_layout = tile_layout.T

x, y = tile_layout.shape
new_im = Image.new('RGBA', (size * x, size * y), (255, 0, 0, 0))

x_offset = 0
for i, xi in enumerate(tile_layout):
    for j, yi in enumerate(xi):
        new_im.paste(mapping[yi], (size * i, size * j))

new_im.save(source_folder + 'autotile_' + tilename + '.png')
