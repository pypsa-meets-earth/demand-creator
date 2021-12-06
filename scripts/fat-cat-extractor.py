## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import logging
from _helpers import configure_logging
import os

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    if "snakemake" not in globals():
        from _helpers import mock_snakemake
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        snakemake = mock_snakemake("fat_cat_extractor")
    configure_logging(snakemake)


# setup the filename to Snakefile output name
filename = snakemake.output.name

# Set up the image URL
image_url = "https://images-na.ssl-images-amazon.com/images/I/A1yWX5VjYJL.png"

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image successfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')