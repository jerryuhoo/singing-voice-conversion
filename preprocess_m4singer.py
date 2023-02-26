import os
import shutil
from tqdm import tqdm

# Specify the path to the M4Singer dataset
dataset_path = '../m4singer'
output_path = 'dataset_raw'

# Create a list of all singers in the dataset
singers = os.listdir(dataset_path)

# Loop over each singer and extract their WAV files
for singer in tqdm(singers):
    singer_path = os.path.join(dataset_path, singer)
    if os.path.isdir(singer_path):
        # Extract the singer ID and song name from the directory name
        singer_id, song_name = singer.split('#')
        # Create a directory for the singer
        singer_dir = os.path.join(output_path, singer_id)
        os.makedirs(singer_dir, exist_ok=True)
        # Loop over all files in the singer's directory
        for filename in os.listdir(singer_path):
            if filename.endswith('.wav'):
                # Get segment id
                segment_id = os.path.splitext(filename)[0]
                # Create the new filename using the singer ID and song name
                new_filename = singer + '#' + segment_id + '.wav'
                # Copy the WAV file to the singer's directory with the new filename
                src_path = os.path.join(singer_path, filename)
                dst_path = os.path.join(singer_dir, new_filename)
                shutil.copyfile(src_path, dst_path)
