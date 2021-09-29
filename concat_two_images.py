# reference: https://note.nkmk.me/en/python-pillow-paste/https://note.nkmk.me/en/python-pillow-concat-images/

import os
import argparse
from PIL import Image


index = 0
success_list = []
fails_list = []
empty_folders = []

parser = argparse.ArgumentParser(description='Merge images from folder.')
parser.add_argument('path_raw_images', metavar='image_folder', help='path to the folder containing raw images.')
parser.add_argument('dir_save', metavar='output_dir', help='path to the folder where output images are stored.')
args = parser.parse_args()

os.makedirs(args.dir_save, exist_ok=True)

for root, dirs, files in os.walk(args.path_raw_images):

    folder = os.path.basename(root)

    if len(files) == 2:

        # Open image:
        st_path = os.path.join(root, files[0])
        st_image = Image.open(st_path)

        nd_path = os.path.join(root, files[1])
        nd_image = Image.open(nd_path)

        # Create an empty image:
        concat = Image.new('RGB', (st_image.width + nd_image.width, max(st_image.height, nd_image.height)))

        # Paste image, biggest first:
        if st_image.height > nd_image.height:
            concat.paste(st_image, (0, 0))
            concat.paste(nd_image, (st_image.width, round((st_image.height - nd_image.height) / 2)))
        else:
            concat.paste(nd_image, (0, 0))
            concat.paste(st_image, (nd_image.width, round((nd_image.height - st_image.height) / 2)))

        # Save image:
        concat.save(os.path.join(args.dir_save, f'{folder}.jpg'))

        success_list.append(os.path.join(args.path_raw_images, folder))
        print(f'{index} - Image Concatenated:', os.path.join(args.dir_save, f'{folder}.jpg'))
        index += 1

    elif root == args.path_raw_images:
        continue

    elif len(files) == 0:
        empty_folders.append(os.path.join(args.path_raw_images, folder))
        print(f'{index} - This folder is empty:', os.path.join(args.path_raw_images, folder))
        index += 1

    else:
        fails_list.append(os.path.join(args.path_raw_images, folder))
        print(f'{index} - Process Failed:', os.path.join(args.path_raw_images, folder))
        index += 1

print(f'\nSUCCESS: {len(success_list)} images')
print(f'FAILS: {len(fails_list)} folders')
print(f'EMPTY FOLDERS: {len(empty_folders)} folders\n')
