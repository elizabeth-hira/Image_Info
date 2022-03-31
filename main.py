# import required module
import os
import pandas as pd
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


columns = ['File name', 'size', 'resolution', 'depth', 'compression']
df = pd.DataFrame([], columns=columns)

print('Enter name of final directory:')
[print(x[0]) for x in os.walk("../lab2")]


# assign directory
directory = input()

start_time = datetime.now()
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    image = Image.open(f)
    df = df.append(pd.DataFrame([[filename, image.size, image.info.get('dpi'), image.mode, image.info.get('compression')]],
                                columns=columns), ignore_index=True)

print("time: " + str(datetime.now() - start_time))

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)