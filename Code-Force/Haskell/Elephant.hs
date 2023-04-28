main :: IO ()
main = interact $ show . flip steps 0 . read

steps :: Int -> Int -> Int
steps s acc | s == 0 = acc | otherwise = steps (s - step) (acc + 1)
    where step = head $ (\ xs -> if null xs then [1] else xs) . dropWhile (s < ) $ [5, 4 .. 1]