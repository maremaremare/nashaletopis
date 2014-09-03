from .transliterate import transliterate
from taggit.models import Tag, TaggedItem


class TagCyrillic(Tag):

    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        slug = tag.lower().replace(' ', '-')
        if i is not None:
            slug += '-%d' % i
        return transliterate(slug)


class TaggedItemCyrillic(TaggedItem):

    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return TagCyrillic
