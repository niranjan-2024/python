## Welcome to PYTHON files maintained by Niranjan

You can use the [editor on GitHub](https://github.com/niranjan-2024/python/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)

```
### [1.Sieve of eratosthenes](https://github.com/niranjan-2024/python/blob/main/Sieve%20of%20eratosthenes.py)
`def sieve_of_erastosthenes(n):
   prime_list = []
   for i in range(2, n+1):
      if i not in prime_list:
         print(i)
         for j in range(i*i , n+1, i):
            prime_list.append(j)
            
sieve_of_erastosthenes(100)`
For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/niranjan-2024/python/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
