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
        snakemake = mock_snakemake("salt_bae_extractor",
                                    number=3)
    configure_logging(snakemake)


amount_of_pictures = snakemake.wildcards.number

# setup the filename to Snakefile output name
filenames = snakemake.output.picture

# Set up the image URL
image_url = "https://pbs.twimg.com/media/ETl5iUZXsAEv0Jc.jpg"

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    
    for name in filenames:
            with open(name,'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ',name)

else:
    print('Image Couldn\'t be retreived')