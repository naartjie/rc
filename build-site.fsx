#r "nuget: FSharp.Formatting, 15.0.0"

open System.IO
open FSharp.Formatting.Markdown

(**
# First-level heading
Some more documentation using `Markdown`.
*)

let helloWorld () = printfn "Hello world!"

(**
## Second-level heading
With some more documentation
*)

// let numbers = [ 0 .. 99 ]
// (*** include-value: numbers ***)

let document =
    $"""
# Bootstrapping
## Static shite generator in F#

LOLs aside, this is all I need to get started - a canvas for ideas:

<pre>site.fsx</pre>

```fsharp
{File.ReadAllText(
     Directory.GetCurrentDirectory()
     + "/build-site.fsx"
 )}
"""

document
|> Markdown.Parse
|> Markdown.ToHtml
|> fun html -> File.WriteAllText($"{Directory.GetCurrentDirectory()}/site/new.html", html)
