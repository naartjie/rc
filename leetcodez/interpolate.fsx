(*
You are given a list of (timestamp, value) tuples representing points in a timeseries. Timestamps are on even 5 second intervals but some intervals may be missing.

Write the function that will linearly interpolate gaps in the timeseries.

Example:

interpolate(points: List[Tuple[int, int]], interval: int) -> List[Tuple[int, int]]

input =                  [(0, 100), (5, 110),            (15, 130),                       (30, 115)]

interpolate(input, 5) -> [(0, 100), (5, 110), (10, 120), (15, 130), (20, 125), (25, 120), (30, 115)]
Visual thinkers may find an illustration helpful, using o for the input points, and + for the added interpolated points:

   130┃          o
   125┃             +
   120┃       +        +
   115┃                   o
   110┃    o
   105┃
   100┃ o
Value ┗━━━━━━━━━━━━━━━━━━━━
        0  5 10 15 20 25 30
        Time
*)

let calcLinear (x: int) (x1: int) (y1: int) (x2: int) (y2: int) =
  // x1 y1 x2 y2 x = y
  // # for (x1, y1), (x2, y2) with x1 < x < x2
  let slope = (y2 - y1) / (x2 - x1)
  let y = y1 + slope * (x - x1)
  y

let interpolate (points: int * int list) =

  let knownXs =
    inputs
    |> Seq.groupBy (fun (x, y) -> x)

  let idx = 0

  Seq.make (fun _ ->
    if knownXs.contains? idx then
      knownXs.get idx
    else
      let prev = findPrev ...
      let next = findNext ...
      calcLinear (time, prev, next)
    )
