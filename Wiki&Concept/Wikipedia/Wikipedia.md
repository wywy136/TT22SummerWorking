# Wikipedia

## Resources

Wikipedia Dump: https://dumps.wikimedia.org/enwiki/latest/

Base url: https://dumps.wikimedia.org/enwiki/

Wikipedia Tools and application

- https://towardsdatascience.com/boosting-natural-language-processing-with-wikipedia-b779103ba396
- https://www.kdnuggets.com/2017/11/building-wikipedia-text-corpus-nlp.html
- https://www.youtube.com/watch?v=z1PolrZCaAU

Python based tools parsing sql.gz files: https://en.wikipedia.org/wiki/Wikipedia:Database_download#Database_schema

Jyputer notebooks about parsing Wikipedia data: https://github.com/WillKoehrsen/wikipedia-data-science/tree/master/notebooks

## Structure

A link in Wikipedia is formed by link and real content. Real content could be a redirection page from the original word.

A disambiguation page contains a list of links to unambiguous pages. Link example: https://en.wikipedia.org/wiki/New_England_(disambiguation)

Some disambiuation page redirects to a normal page, https://en.wikipedia.org/w/index.php?title=Britain_(disambiguation)&redirect=no redirects to https://en.wikipedia.org/wiki/Britain

A normal page: https://en.wikipedia.org/wiki/Data_structure

A normal category: https://en.wikipedia.org/wiki/Category:Data_structures

## Multistream Data Processing

There are two types of dumps to download

- *pages-articles.xml.bz2*
- *pages-articles-multistream.xml.bz2*

Both contain the same xml. But with multistream, it is possible to get an article from the archive without unpacking the whole thing. 

For multistream, you can get an index file, *pages-articles-multistream-index.txt.bz2*. The first field of this index is the number of bytes to seek into the compressed archive *pages-articles-multistream.xml.bz2*, the second is the article ID, the third the article title.

Decompress multistream files with python: https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor

## Parsing

Parse XML: Tool: SAX

Process actual text of the article: mwparserfromhell

- https://mwparserfromhell.readthedocs.io/en/latest/
- https://mwparserfromhell.readthedocs.io/en/latest/api/mwparserfromhell.html#mwparserfromhell.wikicode.Wikicode
- `plain_text = wiki.strip_code().strip()` get the plain text of the wikipedia page

## Multilingual

Huggingface Dataset: https://huggingface.co/datasets/wikipedia
