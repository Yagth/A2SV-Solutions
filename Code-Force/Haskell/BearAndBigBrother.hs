main :: IO ()
main = do
    input <- getLine
    let [a, b] = map read (words input)
        year = length $ takeWhile (uncurry (<=)) (bearSize a b)
    print year

bearSize :: Int -> Int -> [(Int, Int)]
bearSize a b = zip (iterate (*3) a) (iterate (*2) b)