from wagtail.images.blocks import ImageChooserBlock as DefaultImageChooserBlock

class ImageChooserBlock(DefaultImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title,
                "original": value.get_rendition("original").attrs_dict,
                "thumbnail": value.get_rendition("fill-120x120").attrs_dict,
            }