#r "nuget: FSharp.Formatting, 15.0.0"

open System.IO
open FSharp.Formatting.Markdown

let document =
    $"""
# Bootstrapping
## Static shite generator in F#

LOLs aside, this is all I need to get started - a canvas for ideas:
```fsharp
{File.ReadAllText(Directory.GetCurrentDirectory() + "/site.fsx")}
"""

document
|> Markdown.Parse
|> Markdown.ToHtml
|> fun html -> File.WriteAllText($"{Directory.GetCurrentDirectory()}/index.html", html)
