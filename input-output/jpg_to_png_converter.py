import os
from PIL import Image
import sys

import argparse


# FOR NAMED ARGS, CALL IS LIKE THIS python3 jpg_to_png_converter.py --source=images --target=conversion
# parser = argparse.ArgumentParser(description='Convert images .jpg -> .png')
# parser.add_argument('--source', type=str, help='folder with images to be converted')
# parser.add_argument('--target', type=str, help='target folder to save converted images')
#
# args = parser.parse_args()
# source_dir = args.source
# target_dir = args.target

# FOR POSITIONAL PARAMETERS
source_dir = sys.argv[1]
target_dir = sys.argv[2]

if not os.path.exists(f'./{source_dir}'):
    raise Exception("Source doesn't exist")

if not os.path.exists(f'./{target_dir}'):
    os.makedirs(f'./{target_dir}')

for file in os.listdir(source_dir):
    filename = os.fsdecode(file)
    name, ext = filename.split('.')
    img = Image.open(os.path.join(source_dir, file))
    img.save(os.path.join(target_dir, f'{name}.png'), 'png')

