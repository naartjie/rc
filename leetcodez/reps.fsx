(*
    Determine the total number of repetitions of words in a paragraph.

    paragraph = "The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is, by far, the most important source of energy for life on Earth."

    count_repeated(paragraph) => 11

    "the" is seen 5 times (i.e. 4 repetitions)
    "is" is seen 3 times (i.e. 2 repetitions)
    "of" is seen 3 times (i.e. 2 repetitions)
    "it" is seen 2 times (i.e. 1 repetition)
    "a" is seen 3 times (i.e. 2 repetitions)

    hence number of repetitions is 4+2+2+1+2 = 11
*)

// module Solution

open System.Text.RegularExpressions

let paragraph =
    "The Sun is the star at the center of the Solar System.
     It is a nearly perfect sphere of hot plasma, with internal
     convective motion that generates a magnetic field via a dynamo process.
     It is, by far, the most important source of energy for life on Earth."

let count_repeated paragraph =
    (Regex.Split(paragraph, "\\W+")
        |>Array.map (fun word -> word.ToLower())
    )[0..^1]
    |> Seq.groupBy (fun x -> x)
    |> Seq.map (fun (k, v) -> (Seq.length v) - 1)
    |> Seq.reduce (+)

#if INTERACTIVE
fsi.CommandLineArgs
|> Array.toList
|> List.tail
|> List.toArray
|> run
#else
[<EntryPoint>]
let main argv =
    printfn $"number of repetitions is ${2}"
    0
#endif
