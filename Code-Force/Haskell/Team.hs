team :: [[Int]] -> Int
team =length . filter (>=2) . fmap sum

main :: IO ()
main = do
    inputs <- getContents
    let (_:numbers) = map read <$> (map words . lines) inputs
    print $ team numbers