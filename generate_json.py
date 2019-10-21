import argparse, os, json
from PIL import Image
from tqdm import tqdm
from yolo import YOLO

BATCH = 1000

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dir_path', type=str,
        help='path to directory path, default datasets/test2017', 
        default='datasets/test2017'
    )
    parser.add_argument(
        '--output_dir_path', type=str,
        help='output json directory path, default output',
        default='output'
    )

    return parser.parse_args()

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

yolo = YOLO()

if __name__ == '__main__':
    args = parse_args()

    if not os.path.exists(os.path.join(args.output_dir_path)):
        os.mkdir(os.path.join(args.output_dir_path))

    filenames = os.listdir(os.path.join(args.dir_path))
    batch_files = batch(filenames, BATCH)

    for idx, b in enumerate(batch_files): 
        images = []
        for j, im in tqdm(enumerate(b)):
            if im.endswith(".jpg") or im.endswith(".jpeg") or im.endswith(".bmp") or im.endswith(".png"):
                image = Image.open(os.path.join(args.dir_path, im))

                entities = yolo.detect_image_and_return_entities(image)

                images.append({
                    'filename': im,
                    'entities': entities
                })

        with open(os.path.join(args.output_dir_path, f'{idx+1}.json'), 'w') as json_file:
            json.dump(images, json_file)
