# KC Function Builder
KC Function Builder (KCF) is a tool to compose code in Minecraft using Datapacks with an easier to use syntax.

This allows programmers to understand and write their code much easier than just using Minecraft commands.

KCF attempts to essentially turn most features into functions and other variants, so there is little need of actually running a raw command in a small project.

## KCF-Py (Recommended)
KCF-Py uses a Python syntax to compose code. Functions are defined using the `def` keyword, for example.

The logic of composing a KCF code is still the same: there are load and tick functions and simplified expressions for more complex code, such as `trigger`.

KCF-Py's parser is much easier to work with than the original KCF program as it uses a built-in module called `ast` which already implements the abstract syntax tree needed for this project. 

## KCF (Original)
The original KCF uses a custom syntax, combining the syntax of C, JS, Python, and own implementations with the intent of making the coding experience easier for this type of project.

However, the parser is custom made and is much harder to work with, so it will not receive as much updates as the KCF-Py version. 

If you want a simplified programming experience, you can also check out [mcscript](https://mcscript.stevertus.com/), which does a much better job at implementing this intent.