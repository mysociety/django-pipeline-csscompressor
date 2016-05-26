from csscompressor import compress
from pipeline.compressors import CompressorBase


class CssCompressor(CompressorBase):
    def compress_css(self, css):
        return compress(css)
