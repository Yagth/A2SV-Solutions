main :: IO ()
main = do
    input <- getContents
    let (_:problems) = lines input
        opinionStr = map words problems
        opinions = (map . map) read opinionStr
        results = map sum opinions
        descision = foldl (\acc result -> if result >= 2 then acc + 1 else acc) 0 results
    print descision