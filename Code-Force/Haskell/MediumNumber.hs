import Data.List

main :: IO ()
main = do
    _ <- getLine
    input <- getContents
    let output =unlines $ map (show . medium) (lines input)
    putStrLn output

medium :: String -> Int
medium xs = sort (map read (words xs)) !! 1