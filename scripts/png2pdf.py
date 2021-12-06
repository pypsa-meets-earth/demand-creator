
import PIL.Image
import logging
from _helpers import configure_logging
import os

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    if "snakemake" not in globals():
        from _helpers import mock_snakemake
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        snakemake = mock_snakemake("png2pdf",
                                    number=3)
    configure_logging(snakemake)


filepath = snakemake.input.picture
newfilename = snakemake.output.catpdf


im = PIL.Image.open(filepath)

im.save(newfilename, "PDF", quality=100)