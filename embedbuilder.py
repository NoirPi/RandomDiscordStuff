import discord
from discord.embeds import EmptyEmbed


def embed_builder(**params):
    """
    Args:
        **params:
    """
    title = params.get("title", EmptyEmbed)
    description = params.get("description", EmptyEmbed)
    color = params.get("color", EmptyEmbed)
    url = params.get("url", EmptyEmbed)
    author = params.get("author", "")
    author_url = params.get("author_url", EmptyEmbed)
    author_img = params.get("author_img", EmptyEmbed)
    footer = params.get("footer", "")
    footer_img = params.get("footer_img", EmptyEmbed)
    timestamp = params.get("timestamp", EmptyEmbed)
    image = params.get("image", "")
    thumbnail = params.get("thumbnail", "")
    sections = params.get("sections", params.get("fields", []))
    e = discord.Embed()
    e.title = title
    e.description = description
    e.colour = color
    e.url = url
    if author:
        e.set_author(name=author, url=author_url, icon_url=author_img)
    if footer:
        e.set_footer(text=footer, icon_url=footer_img)
    e.timestamp = timestamp
    e.set_image(url=image)
    e.set_thumbnail(url=thumbnail)
    if sections:
        populate(e, sections)
    return e


def populate(embed: discord.Embed, sections: list):
    """
    Args:
        embed (discord.Embed):
        sections (list):
    """
    for section in sections:
        name = section.get("name", "\uFEFF")
        value = section.get("value", "\uFEFF")
        inline = section.get("inline", True)
        if not name or not value:
            continue
embed.add_field(name=name, value=value, inline=inline)
